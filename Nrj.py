import sys
nrj = []
pdb_dec = []
i=0
dic = {}
cmp = 0
#  Parsing recupère nom pdb_decoy puis pseudo-Energy
if len(sys.argv) != 3:
    sys.exit("ERREUR : il faut exactement deux arguments.")
print(sys.argv[1])
with open(sys.argv[1],'r') as fichier1,open(sys.argv[2],'w') as fichier2:
		lignes = fichier1.readlines()
		for ligne in lignes:
			ligne.strip()
			if ligne.startswith("Now"):
				pdb_dec = ligne.split()
				pdb_dec = pdb_dec[2]
				pdb_dec = pdb_dec.split("/")
				pdb_dec = pdb_dec[-2] +"_" + pdb_dec[-1]
				#print("a", pdb_dec)
			if ligne.startswith("Pseudo-energy"):
				nrj = ligne.split()
				if len(nrj) == 3:
					nrj = nrj[2]
					#print("b",pdb_dec)
				else:
					sys.stderr.write("erreur pour le pdb" + pdb_dec + "\n" )
			
			if(type(nrj)) is str:
				#print("c",pdb_dec)

				fichier2.write(pdb_dec + " " + nrj +"\n")
				nrj = None

