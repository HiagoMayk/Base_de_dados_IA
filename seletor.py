from random import randint

arquivo = open('base.txt', 'r')
texto = arquivo.readlines()

for j in range(524 - 472):
	index = randint(0, len(texto))
	texto = texto[:index] + texto[index+1:]

arquivo = open('proteina10.txt', 'w')
arquivo.writelines(texto)
arquivo.close()

arquivo = open('base.txt', 'r')
texto = arquivo.readlines()

for j in range(524 - 393):
	index = randint(0, len(texto))
	texto = texto[:index] + texto[index+1:]

arquivo = open('proteina25.txt', 'w')
arquivo.writelines(texto)
arquivo.close()

arquivo = open('base.txt', 'r')
texto = arquivo.readlines()

for j in range(524 - 262):
	index = randint(0, len(texto))
	texto = texto[:index] + texto[index+1:]

arquivo = open('proteina50.txt', 'w')
arquivo.writelines(texto)
arquivo.close()

arquivo = open('base.txt', 'r')
texto = arquivo.readlines()

for j in range(524 - 131):
	index = randint(0, len(texto))
	texto = texto[:index] + texto[index+1:]

arquivo = open('proteina75.txt', 'w')
arquivo.writelines(texto)
arquivo.close()
