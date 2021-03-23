install.packages("heatmaply")
install.packages("pheatmap")
library(heatmaply)

Resultat_RMSD <- read.table("~/mypmfs/3Drobot/Traitement_R/Resultat_RMSD", row.names=1, quote="\"", comment.char="")
Resultat_nrj <- read.table("~/mypmfs/3Drobot/Traitement_R/Resultat_nrj.txt", row.names=1, quote="\"", comment.char="")

table =(cbind(Resultat_RMSD, Resultat_nrj))


plot(x = Resultat_RMSD$V2, y = Resultat_nrj$V2)

help(scale)

