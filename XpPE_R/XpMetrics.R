
library(readr)
library(MASS)
library(rTensor)
library(bootstrap)
XpDset_clear_df <- read_csv("Desktop/XpDset_clear_df.csv")
df=XpDset_clear_df 
#Notes

#Mvt :votes 1-10 X1-X10
#avg: group avg decision (majority rule) X1.1-X10.1
#lvc: leader vote check X1.2-X10.2
#ald: leader decision X1?3-X10.3

#Compute leader overconfidence :
n=648
t=10
overconfidence = matrix(nrow=n,ncol=t)
vote=data.frame(df$X1,df$X2,df$X3,df$X4,df$X5,df$X6,df$X7,df$X8,df$X9,df$X10)
avg= data.frame(df$X1.1,df$X2.1,df$X3.1,df$X4.1,df$X5.1,df$X6.1,df$X7.1,df$X8.1,df$X9.1,df$X10.1)
lvc= data.frame(df$X1.2,df$X2.2,df$X3.2,df$X4.2,df$X5.2,df$X6.2,df$X7.2,df$X8.2,df$X9.2,df$X10.2)
ald= data.frame(df$X1.3,df$X2.3,df$X3.3,df$X4.3,df$X5.3,df$X6.3,df$X7.3,df$X8.3,df$X9.3,df$X10.3)
df$male=ifelse(df$gender==2,1,0)
df$female=ifelse(df$gender==1,1,0)
df$tr=ifelse(df$Treatment==1,1,0)
df$control=ifelse(df$Treatment==1,0,1)
dset=data.frame(overconfidence,vote,avg,lvc,ald)
for(i in 1:t){
  for(j in 1:n){
  overconfidence[j,i] = ifelse(df$Leader[j]==1 & lvc[j,i]==0,1,0)
  }
}


Cov= as.matrix(data.frame(overconfidence[,1],overconfidence[,t],df$exp,df$male,df$female,df$payoff,df$tr,df$control),nrow=n,ncol=8)
y= as.matrix(data.frame(lvc,ald))

glm(y~Cov)
#Overconfidence on Leader decision OLS Style

A=ginv(t(as.matrix(overconfidence))%*%(as.matrix(overconfidence)))%*%t(as.matrix(overconfidence))
beta1 = t(A%*%y)
Q=data.frame(overconfidence,df$exp,df$gender,df$Treatment,df$payoff,lvc,ald)
C= ginv(t(Cov)%*%Cov)%*%t(Cov)
BETA= C%*%y

Model = Cov%*%BETA + rnorm(n,mean(y-Cov%*%BETA),sd(y-Cov%*%BETA))

#Diffusion stuff
B=eigen(beta1)
D= Re(B$vectors)

fcast2 = function(X){
  return(sum(X))}
fcast3 = function(X){return(sd(X))}


sum(BETA[1,])
BootVector= vector("numeric",8)
BootVector2= vector("numeric",8)
BsD=vector("numeric",8)
BsM=vector("numeric",8)
N=100
rowSums(BETA)

sd(BETA[,1])
sd

for(i in 1: 8){
  BootVector[i]=mean(bootstrap(BETA[i,],theta=fcast2,nboot=100)$thetastar)
  BootVector2[i]=mean(bootstrap(BETA[i,],theta=fcast3,nboot=100)$thetastar)
  BsM[i]= rowSums(BETA)[i]
  BsD[i]= sd(BETA[,i])
}

Bn = data.frame(BETA)
lmboot= bootstrap(BETA,theta=fcast2,nboot=100)
lmbca= bcanon(BETA,theta=fcast2,nboot=100)

ci = c(lmbca$confpoints[1,2],lmbca$confpoints[8,2])

BootVector
BootVector2

t =vector("numeric",8)
for(i in 1:8){
  t[i]= BootVector[i] / BootVector2[i]
}


dnorm(t)