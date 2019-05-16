arrtext       = []
arrtextun     = []
arrtextcount  = []

txt = ["bandung jakarta medan bandung sumatera kalimantan medan papua"]
arrtext   = txt.split(" ");

#push teks unik
for(var x = 0; x < arrtext.length; x++)
{
  if(!arrtextun.includes(arrtext[x]))
  {
    arrtextun.push(arrtext[x])
  }
}
console.log(arrtextun);

for(var y = 0; y < arrtextun.length; y++)
{
  var num = 0;
  for(var z = 0; z < arrtext.length; z++)
  {
    if(arrtextun[y] == arrtext[z])
    {
      num++;
    }
  }
  arrtextcount.push(num);
}
console.log(arrtextcount);