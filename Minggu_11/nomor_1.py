f = open('nama_kelompok.txt','r')
text = f.read()
text = text.replace('\n','')
f1 = open('nama_kelompok.txt','w')
f1.write(text)