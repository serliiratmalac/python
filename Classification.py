

def build_counts(self, pol_list, sent_list):
    wordnet_lemmatizer = WordNetLemmatizer()
    cnt_pos = Counter()
    cnt_neg = Counter()
      pol_list.extend(sent_list)
    stops = set(stopwords.words('english'))
    for pol in pol_list:
        pos = [wordnet_lemmatizer.lemmatize(x) for x in pol[0].split(' ') 
                if (pol[1] == 'positive' or pol[1] == 'uncertain-positive' 
                    or pol[1] == 'both' or pol[1] == 'sentiment-pos') 
                    and x not in stops]
        neg = [wordnet_lemmatizer.lemmatize(x) for x in pol[0].split(' ') 
                if (pol[1] == 'negative' or pol[1] == 'uncertain-negative' 
                    or pol[1] == 'both' or pol[1] == 'sentiment-neg') 
                    and x not in stops] 

        for word in pos:
            cnt_pos[word] += 1
        for word in neg:
            cnt_neg[word] += 1     
    return cnt_pos, cnt_neg

def train(self):
    self.features = {}
    self.features['posFeatures'] = {}
    self.features['negFeatures'] = {}

    # Gathering a priori probabilities by class
    self.priorLogPos = math.log(self.pos_count/self.doc_count)
    self.priorLogNeg = math.log(self.neg_count/self.doc_count)

    """
    Each for loop below is calculating probabilities of each feature
    for each class.
    Backslashes in calculations are added for readiblity and serve as 
    line breaks.
    """
    for word, count in self.pos.items():
        self.features['posFeatures'][word] = math.log((count + 1) \
                                        /(self.pos_count + self.doc_count))
        
    for word, count in self.neg.items():
        self.features['negFeatures'][word] = math.log((count + 1) \
                                        /(self.neg_count + self.doc_count))

def test(self, document):
    wordnet_lemmatizer = WordNetLemmatizer()
    document = [wordnet_lemmatizer.lemmatize(x) for x in document.split(" ")]
    pos_val = self.priorLogPos
    neg_val = self.priorLogNeg
   
    # Smoothed probabilities are calculated below, these are used when a 
    # word in the test document is not found in the given class but is found
    # in another class's feature dict
    smooth_pos = math.log(1/(self.pos_count + self.doc_count))
    smooth_neg = math.log(1/(self.neg_count + self.doc_count))

    for feature in self.features:
        if feature == 'posFeatures':
            for word in document:
                if word in self.features['posFeatures']:
                    pos_val += self.features['posFeatures'][word]
                elif word in self.features['negFeatures'] or self.features['neutralFeatures']:
                    pos_val += smooth_pos
        elif feature == 'negFeatures':
            for word in document:
                if word in self.features['negFeatures']:
                    neg_val += self.features['negFeatures'][word]
                elif word in self.features['posFeatures'] or self.features['neutralFeatures']:
                    neg_val += smooth_neg
        

    if pos_val > neg_val and pos_val > neutral_val:
        return ('positive', pos_val)
    elif neg_val > pos_val and neg_val > neutral_val:
        return ('negative', neg_val)
    elif neutral_val > pos_val and neutral_val > neg_val:
        return ('neutral', neutral_val)
    else:
        return ('positive', pos_val)

        
def __init__(self, pos, neg):
    self.pos_count = MPQA.count(pos)
    self.neg_count = MPQA.count(neg)
    self.doc_count = self.pos_count + self.neg_count
    self.pos = pos
    self.neg = neg
   