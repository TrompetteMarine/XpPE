library(lattice)
library(randomForest)
library(pals)
library(np)
set.seed(12345)
##Read historical data 144 x 10 into data frame x
)
dim(XpDset_clear_df) 

x.var <- colnames(XpDset_clear_df)[3:12]
y.var <- colnames(XpDset_clear_df)[37:46]
xx.historical <- round(XpDset_clear_df[,c("id",x.var,y.var)],3)

rf.models <- list()
R2        <- NULL
for (i in (1:length(y.var)) )   {    
  # rf modeling; add models to list rf.models
  rf.models[[i]] <- randomForest(
    formula(paste(y.var[i],"~",paste(x.var,collapse="+"),  
                  sep="")),data=XpDset_clear_df) 
  R2     <- c(R2, round(cor(predict(rf.models[[i]]),
                            XpDset_clear_df[,y.var[i]])^2,2))
}
names(R2) <- y.var
R2


locfit(y.var ~ x.var,
      regtype = "ll",
      bwmethod = "cv.aic",
      gradients = TRUE,
      data = xx.historical)



tnsr <- rand_tensor(c(6,6,6,5))
tnsr2 <- rand_tensor(c(5,4,10,4))
tnsr3 <- rand_tensor(c(6,4,10,3))
tuckerD <- tucker(tnsr,ranks=c(2,2,2,2))
tuckerD2 <- tucker(tnsr2,ranks=c(2,2,2,2))
tuckerD3 <- tucker(tnsr3,ranks=c(2,2,2,2))

plot(tuckerD$all_resids)
plot(tuckerD2$all_resids)
plot(tuckerD3$all_resids)

tnsr <- as.tensor(as.matrix(C,overconfidence,vote,BETTA),drop=TRUE)
tuckerD4 = tucker(tnsr,ranks=c(2,2,2,2))
plot(tuckerD4$all_resids)