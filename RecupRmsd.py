import sys

liste = []
with open(sys.argv[1],"r") as fichier1: # la liste avec les chemins jusqu'au liste Rmsd
	chemins = fichier1.readlines()
	fichier3 = open(sys.argv[2],"w")
	for chemin in chemins:
		chemin = chemin[:-1]
		pdb = chemin.split("/")
		pdb = pdb[-2]
		#print(pdb)
		with open(chemin,"r") as fichier2:
			lignes = fichier2.readlines()
			for ligne in lignes:
				ligne.strip()
				ligne = ligne.split()
				if (ligne[0] != "NAME"):
					if len(ligne) == 2:
						fichier3.write(pdb + "_" + ligne[0] + " " + ligne[1] +"\n")
						ligne = None
					else:
						sys.stderr.write("erreur pour le pdb" + pdb + "\n" )
				#print(ligne)
fichier3.close()
"""
if len(sys.argv) != 3:
    sys.exit("ERREUR : il faut exactement deux arguments.")
print(sys.argv[1])
with open(sys.argv[1],'r') as fichier1,open(sys.argv[2],'w') as fichier2:*/ """