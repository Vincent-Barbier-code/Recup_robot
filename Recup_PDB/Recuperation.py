import urllib2
from os import mkdir, chdir

# with open("independent_training.txt", 'r') as fichier1,open("dataset",'w') as fichier2 :
# 	lignes = fichier1.readlines()
# 	for code_pdb in lignes:
# 		code_pdb.strip()
# 		print(code_pdb)
# 		u = urllib2.urlopen("http://www.pdb.org/pdb/files/" + code_pdb + "pdb")
# 		pdb_lines = u.readlines()
# 		u.close()
# 		for i in pdb_lines:
# 		 	print i

# code_pdb = "1BTA"
# u = urllib2.urlopen("http://www.pdb.org/pdb/files/" + code_pdb + "pdb")
# pdb_lines = u.read()
# u.close()
# for i in pdb_lines:
# 	print i

# with open("independent_training.txt", 'r') as fichier1,open("dataset",'w') as fichier2 :
# 		lignes = fichier1.readlines()
# 		for ligne in lignes:
# 			print(lignes)

dossier = input("nom de dossier ou vous souhaitez mettre les fichiers (entre guillemets) : ")

try:
   os.mkdir(dossier)
except:
    print('Dossier deja existant')



liste_pdb = []
with open("independent_training.txt", 'r') as fichier1:
	lignes = fichier1.readlines()
	for code_pdb in lignes:
		code_pdb = code_pdb[0:4]
		liste_pdb.append(code_pdb)
			
liste_mauvais = []
for pdb in liste_pdb:
	try:
		u = urllib2.urlopen("http://files.rcsb.org/download/" + pdb + ".pdb")
		contenu_pdb = u.read()
		u.close()
		f = open( pdb + ".pdb","w")
		f.write(contenu_pdb)
		f.close()
	except:
		liste_mauvais.append(pdb)


f = open("pdb_non_fonctionnel","w")
for code_pdb in liste_mauvais:
	f.write(code_pdb + "\n")
f.close()			

# for pdb in liste_pdb:
# 	print(pdb)
	# pdb = "1A62A"
	# u = urllib2.urlopen("http://files.rcsb.org/download/1A62A.pdb")
	# contenu_pdb = u.read()
	# u.close()
	# print(contenu_pdb)
	# f = open("dataset.txt","w")
	# f.write(contenu_pdb)
	# f.close()
