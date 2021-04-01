import os
import sys
# en premier chemin all puis chemin natifs 
liste = []
i = 0
os.system("rm all_TMscore.txt")
with open(sys.argv[1],"r") as fichier1, open(sys.argv[2],"r") as fichier2: # la liste avec les chemins jusqu'au liste
	chemins = fichier1.readlines()
	chemins_nat = fichier2.readlines()
	for chemin_nat in chemins_nat:
		chemin_nat = chemin_nat[:-1]
		cp_pdb = chemin_nat.split("/")
		print(cp_pdb)

		if len(cp_pdb)>1:
			cp_pdb = cp_pdb[-2]
			
			for chemin in chemins:
				chemin = chemin[:-1]
				pdb = chemin.split("/")
				pdb = pdb[-2]
				if cp_pdb == pdb:
					os.system("~/Desktop/TMscore/TMscore" + " " + chemin_nat + " " + chemin + " " + ">>" + " " + "all_TMscore.txt")
				

	fichier3 = open("all_TMscore.txt","r")
	fichier4 = open("Resultat_TMscore","w")
	lignes = fichier3.readlines()
	for	ligne in lignes:
		if ligne.startswith("Structure2"):
			nom = ligne.split()
			nom = nom[1]
			nom = nom.split("/")
			nom = nom[-2] + "_" + nom[-1]
			fichier4.write(nom + " ")

		if ligne.startswith("RMSD"):
			RMSD = ligne.split()
			RMSD = RMSD[5]

			fichier4.write(RMSD + " ")
			
		if ligne.startswith("TM-score"):
			TM = ligne.split()
			TM = TM[2]
			
			fichier4.write(TM + " ")

		if ligne.startswith("MaxSub"):
			MaxSub = ligne.split()
			MaxSub = MaxSub[1]
			
			fichier4.write(MaxSub + " ")

		if ligne.startswith("GDT-TS"):
			GDT_TS = ligne.split()
			GDT_TS = GDT_TS[1]
			
			fichier4.write(GDT_TS + " ")

		if ligne.startswith("GDT-HA"):
			GDT_HA = ligne.split()
			GDT_HA = GDT_HA[1]
			
			fichier4.write(GDT_HA + "\n")	
		
		#with open(sys.argv[2],"a") as fichier2:


#2J1VA_native.pdb





#os.system("~/Desktop/TMscore/TMscore ~/mypmfs/3Drobot/3DRobot_set/1BYIA/native.pdb ~/mypmfs/3Drobot/3DRobot_set/1BYIA/decoy0_1.pdb  ")
# os.popen().read()