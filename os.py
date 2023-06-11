import os

os.mkdir('data')

file = os.open('data/server.js', 'w')
file.write('const string = "Tejas"')
file.close()




