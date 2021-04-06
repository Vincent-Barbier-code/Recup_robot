import os
import sys
nom = []
rmsd = []
TM = []
Delta_TM = 0
cmp = 0
correct = 0
total = 0 
seuil1 = sys.argv[1]
seuil2 = sys.argv[2]

a=0
with open("Resultat_TMscore.txt","r") as fichier1 :
	lignes = fichier1.readlines()
	for ligne in lignes :
		
		ligne.strip()
		ligne = ligne.split()
		nom.append(ligne[0]) 
		rmsd.append(float(ligne[1]))
		TM.append(float(ligne[2]))
	
	for i in range(1,len(TM)):
		print(nom[i])
		for y in range(0,i):
			Delta_TM = abs(TM[i]-TM[y])
			if Delta_TM < seuil1:
				a+=1
				if TM[i] > TM[y]:
					Emax = TM[y]
					Delta_E = (TM[y]-TM[i])
				if TM[i] < TM[y]:
					Emax = TM[i]
					Delta_E = (TM[i]-TM[y])
				else:
					pass
				diff_rel = Delta_E/Emax
				if diff_rel < seuil2:
					correct += 1
					total += 1
				else:
					total += 1
			else:
				correct += 1
				total += 1 	
	Acc = correct/total			 
	print(Acc)	
	print(a)
		#Delta_TM = abs()

#for i in range(len(fichier-1)):
#	pass