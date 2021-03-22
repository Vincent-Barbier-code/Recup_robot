import sys
nrj = []
pdb_dec = []
i=0
dic = {}
if len(sys.argv) != 3:
    sys.exit("ERREUR : il faut exactement deux arguments.")

with open(sys.argv[1],'r') as fichier1, open(sys.argv[2],'w') as fichier2:
	lignes = fichier1.readlines()
	for ligne in lignes:
		ligne.strip()
		if ligne.startswith("Now"):
			pdb_dec = ligne.split()
			pdb_dec = pdb_dec[2]
			pdb_dec = pdb_dec.split("/")
			pdb_dec = pdb_dec[-2] +"_" + pdb_dec[-1]
			
		if ligne.startswith("Pseudo-energy"):
			nrj = ligne.split()
			nrj = nrj[2]
			if (pdb_dec is None)|(nrj is None) :
				sys.stderr.write(ligne)

				
			fichier2.write(pdb_dec +" " + nrj +"\n")

		

