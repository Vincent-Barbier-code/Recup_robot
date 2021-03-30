install.packages("Hmisc")
install.packages("pheatmap")
library(heatmaply)
library(Hmisc)
Resultat_RMSD <- read.table("./Resultat_RMSD", row.names=1, quote="\"", comment.char="")
Resultat_nrj <- read.table("./Resultat_nrj.txt", row.names=1, quote="\"", comment.char="")

table =(cbind(Resultat_nrj,Resultat_RMSD))




colnames(table) = c("nrj","rmsd")


plot(table$nrj, table$rmsd,xlab = "nrj", ylab = "rmsd")
text(x = 50,y = 600,col = "red",labels = sprintf("r = %3.2f",cor(table$nrj,table$rmsd)))
modele = lm(table$nrj ~ table$rmsd)
summary(modele)
abline(modele, col = "red", lwd = 2)

par(mfrow = c(2,2))

x=0
y=0
for (i in 1:200) {
  a = toString(i)
  b = paste("Nrj-Rmsd_plot",a,".png",sep = "")
  png(b)
  x <- (i-1)*301
  y <- i *301
  print(x)
  plot(table$nrj[x:y], table$rmsd[x:y],xlab = "nrj", ylab = "rmsd")
  text(x = 50,y = 600,col = "red",labels = sprintf("r = %3.2f",cor(table$nrj,table$rmsd)))
  abline(modele, col = "red", lwd = 2)
  dev.off()
}

cor(table$nrj, table$rmsd, method=c("pearson", "kendall", "spearman"))



data_cor <- cor(table)



corrplot::corrplot(data_cor,tl.cex = 0.5)






r <- cor(table$nrj, table$rmsd) 
test <- cor.test(table$nrj, table$rmsd) 

panel.cor_simple <- function(x, y, digits=2, prefix="", cex.cor) 
{
  usr <- par("usr"); on.exit(par(usr)) 
  par(usr = c(0, 1, 0, 1)) 
  r <- cor(x, y) 
  txt <- format(c(r, 0.123456789), digits=digits)[1] 
  txt <- paste(prefix, txt, sep="") 
  if(missing(cex.cor)) cex <- 0.8/strwidth(txt) 
  
  test <- cor.test(x,y) 
  # borrowed from printCoefmat
  Signif <- symnum(test$p.value, corr = FALSE, na = FALSE, 
                   cutpoints = c(0, 0.001, 0.01, 0.05, 0.1, 1),
                   symbols = c("***", "**", "*", ".", " ")) 
  
  text(0.5, 0.5, txt, cex = cex * abs(r)) 
  text(.8, .8, Signif, cex=cex, col=2) 
} 

a <- panel.cor_simple(table$nrj,table$rmsd)
pairs(r, lower.panel=panel.smooth, upper.panel=panel.cor_simple) 
M <- cor(table)


col <- colorRampPalette(c("#BB4444", "#EE9988", "#FFFFFF", "#77AADD", "#4477AA"))

corrplot(M, method="color", col=col(200), 
         type="upper",
         addCoef.col = "black") 



cor(table)
rcorr(Resultat_RMSD, type=c("pearson","spearman"))

cor(Resultat_nrj, Resultat_RMSD, method = c("pearson", "kendall", "spearman"))

help(scale)

