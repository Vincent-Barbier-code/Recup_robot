#install.packages("Hmisc")
#install.packages("pheatmap")
#library(heatmaply)
#library(Hmisc)
Resultat_RMSD <- read.table("./Resultat_RMSD", quote="\"", comment.char="")
Resultat_nrj <- read.table("./Resultat_nrjCB.txt", quote="\"", comment.char="")
table_TM <- read.table("./Resultat_TMscore.txt", quote="\"", comment.char="")
table = merge(Resultat_nrj,Resultat_RMSD,by = "V1")
table = merge(table,table_TM,by = "V1")


table = table[,-1]

colnames(table) = c("nrj","rmsd_exp","rmsd_hyp","TM-score","MawSub","GDT-TS","GDT-HA")

liste_mauvais = list()
liste_bon = list()
for (i in 1:length(table$rmsd_exp)) {
  difference = 0
  difference =  abs(table$rmsd_exp[i] - table$rmsd_hyp[i])
  print(difference)
  if(difference > 0.02){
    liste1 <- list(row.names(table)[i])
    liste_mauvais <- append(liste_mauvais,liste1)
  }
  else{
    liste1 <- list(row.names(table)[i]) 
    liste_bon <- append(liste_bon,liste1)
  }
}

plot(table$nrj, table$`TM-score`,xlab = "nrj", ylab = "rmsd")
text(x = 50,y = 600,col = "red",labels = sprintf("r = %3.2f",cor(table$nrj,table$rmsd)))
modele = lm(table$nrj ~ table$`TM-score`,data = table)
plot(table$nrj~table$`TM-score`,pch = 16,data = table)
abline(modele, col = "red",lwd = 2)
summary(modele)
# TM
x=0
y=0
Regression <- function(ligne1,ligne2,stringnom,xnom,ynom){
  for (i in 1:200) {
    a = toString(i)
    b = paste(stringnom,a,".png",sep = "")
    png(b)
    x <- (i-1)*301
    y <- i *301
    print(x)
    pearson = cor(ligne1[x:y], ligne2[x:y], method="pearson")
    kendall = cor(ligne1[x:y], ligne2[x:y], method="kendall")
    spearman = cor(ligne1[x:y], ligne2[x:y], method="spearman")
    
    pearson = round(pearson,4)
    kendall = round(kendall,4)
    spearman = round(spearman,4)
    
    # Equation de la droite de regression : 
    modele = lm(ligne1[x:y] ~ ligne2[x:y],data = table)
    plot(ligne1[x:y] ~ ligne2[x:y], pch = 16, data = table,xlab = xnom, ylab = ynom)
    abline(modele, col = "red",lwd = 2)
    
    mtext(text = pearson,adj = 0, side = 1, line = 4)
    mtext(text = kendall,adj = 0.5, side = 1, line = 4)
    mtext(text = spearman,adj = 1, side = 1, line = 4)
    
    dev.off()
  }
}
#Regression(table$nrj,table$`TM-score`,"Reg_nrj-TMscore","TM-score","Pseudo-Energie")
Regression(table$nrj,table$rmsd_exp,"Reg_nrj-Rmsd","Rmsd","Pseudo-Energie")




Acc = correct/tot
Acc <- function(){
  for (i in 1:length(table$`TM-score`-1)) {
    for (y in 1:length(table$`TM-score`-i)) {
      Delta_TM = table$`TM-score[i]` - table$`TM-score`[y+1])
      print(Delta_TM)
      print(table$`TM-score`[i])
    }
  }
}
table$`TM-score`[2]
 Acc()

# 
# 
# data_cor <- cor(table)
# 
# 
# 
# corrplot::corrplot(data_cor,tl.cex = 0.5)
# 
# 
# 
# 
# 
# 
# r <- cor(table$nrj, table$rmsd) 
# test <- cor.test(table$nrj, table$rmsd) 
# 
# panel.cor_simple <- function(x, y, digits=2, prefix="", cex.cor) 
# {
#   usr <- par("usr"); on.exit(par(usr)) 
#   par(usr = c(0, 1, 0, 1)) 
#   r <- cor(x, y) 
#   txt <- format(c(r, 0.123456789), digits=digits)[1] 
#   txt <- paste(prefix, txt, sep="") 
#   if(missing(cex.cor)) cex <- 0.8/strwidth(txt) 
#   
#   test <- cor.test(x,y) 
#   # borrowed from printCoefmat
#   Signif <- symnum(test$p.value, corr = FALSE, na = FALSE, 
#                    cutpoints = c(0, 0.001, 0.01, 0.05, 0.1, 1),
#                    symbols = c("***", "**", "*", ".", " ")) 
#   
#   text(0.5, 0.5, txt, cex = cex * abs(r)) 
#   text(.8, .8, Signif, cex=cex, col=2) 
# } 
# 
# a <- panel.cor_simple(table$nrj,table$rmsd)
# pairs(r, lower.panel=panel.smooth, upper.panel=panel.cor_simple) 
# M <- cor(table)
# 
# 
# col <- colorRampPalette(c("#BB4444", "#EE9988", "#FFFFFF", "#77AADD", "#4477AA"))
# 
# corrplot(M, method="color", col=col(200), 
#          type="uppel = "black") 
# 
# 
# 
# cor(table)
# rcorr(Resultat_RMSD, type=c("pearson","spearman"))
# 
# cor(Resultat_nrj, Resultat_RMSD, method = c("pearson", "kendall", "spearman"))
# 
# help(scale)
# r",
#          addCoef.co
