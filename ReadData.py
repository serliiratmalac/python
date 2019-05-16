
def readFile2(fileName):
    data = open(fileName, "r", encoding="utf8")

    output = []
    for line in data.read(): #kalimat berbentuk list panjang kemudian dilakukan enter per kalimat
        line = line.split(";")
        output.append([" ".join(line[1:-1]), line[-1]]) # [label, Text Sentiment]
    return output

