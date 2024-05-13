trace <- function(A) {
  n <- dim(A)[1] # get dimension of matrix
  tr <- 0 # initialize trace value
  
  # Loop over the diagonal elements of the supplied matrix and add the element to tr
  for (k in 1:n) {
    l <- A[k,k]
    tr <- tr + l
  }
  return(tr[[1]])
}


C=matrix(c(-sqrt(13)/(2*sqrt(2)),sqrt(13)/(2*sqrt(2)),sqrt(13)/(2*sqrt(2)),sqrt(3)/(3),sqrt(3)/(3),
           sqrt(13)/(2*sqrt(2)),sqrt(13)/(2*sqrt(2)),sqrt(13)/(2*sqrt(2)),sqrt(3)/(3),sqrt(3)/(3),
           sqrt(13)/(2*sqrt(2)),sqrt(13)/(2*sqrt(2)),sqrt(13)/(2*sqrt(2)),sqrt(3)/(3),sqrt(3)/(3),
           -sqrt(2)/(2*sqrt(13)),sqrt(2)/(2*sqrt(13)),sqrt(2)/(2*sqrt(13)),0,0,
           -sqrt(2)/(2*sqrt(13)),sqrt(2)/(2*sqrt(13)),-sqrt(2)/(2*sqrt(13)),0,0),nrow=5,ncol=5,byrow=TRUE)



Lamba=diag(5)
Lamba[1,1]= -1/2
Lamba[2,2]= 1/2
Lamba[3,3]= 1/2
Lamba[4,4]= 1
Lamba[5,5]= 1


LambaT=diag(5)

LambaT[1,1]= -0.5i
LambaT[2,2]= 0.5i
LambaT[3,3]= 1/2
LambaT[4,4]= 1
LambaT[5,5]= 1


P= t(C)%*%Lamba^4%*%C
P2= t(C)%*%(Lamba^18)%*%C

Ct1=matrix(c(0.549342-0.227545i,0.5-0.5i,sqrt(2/7),sqrt(7)/7,sqrt(7)/7,
             0.274671-0.1137725i,1+1i,sqrt(2/28),sqrt(7)/7,sqrt(7)/7,
             0.274671-0.1137725i,1+1i,0.5*sqrt(2/7),sqrt(7)/7,sqrt(7)/7,
             0.5826653-0.2413477i,1i*sqrt(2)/2,sqrt(2/7),2*sqrt(2/7),2*sqrt(2/7),
             0.5826653-0.2413477i,1i*sqrt(2)/2,sqrt(2/7),2*sqrt(2/7),-2*sqrt(2/7)),nrow=5,ncol=5,byrow=TRUE)

Ctau1=matrix(c(0.549342,0.5,sqrt(2/7),sqr(7)/7,sqr(7)/7,
             0.274671,1,sqrt(2/28),sqr(7)/7,sqr(7)/7,
             0.274671,1,0.5sqrt(2/7),sqr(7)/7,sqr(7)/7,
             0.5826653,sqrt(2)/2,sqrt(2/7),2*sqr(2/7),2*sqr(2/7),
             0.5826653,sqrt(2)/2,sqrt(2/7),2*sqr(2/7),-2*sqr(2/7)),nrow=5,ncol=5,byrow=TRUE)


Ptau1=t(Ct1)%*%LambaT^4%*%Ct1
Ptau2=t(Ct1)%*%LambaT^18%*%Ct1


Pt1= diag(5)
Pt2= diag(5)
PtA= diag(5)

#Some mysterious computations
for(i in 1:5){
  for(j in 1:5){
    PtA[i,j]=(sqrt(Re(Ptau1[i,j])^2+Im(Ptau1[i,j])^2))/sqrt(Re(trace(t(Ptau1)%*%Ptau1))^2+Im(trace(t(Ptau1)%*%Ptau1))^2)
  }
}

PtA=Re(PtA)
PtA

#Some less mysterious computations

for(i in 1:5){
 for(j in 1:5){
   Pt1[i,j]=(sqrt(Re(Ptau1[i,j])^2+Im(Ptau1[i,j])^2))
   }
}


Pt1=Re(Pt1)

for(i in 1:5){
  for(j in 1:5){
    Pt1[i,j]= Re(Pt1[i,j])/sqrt(t(Re(Pt1[,j]))%*%Re(Pt1[,j]))
  }
}


Pt1

Pt1-PtA
#Well Well Well

for(i in 1:5){
  for(j in 1:5){
    Pt2[i,j]=(sqrt(Re(Ptau2[i,j])^2+Im(Ptau2[i,j])^2))/sqrt(t(Pt2[,j])%*%Pt2[,j])
  }
}



G= diag(5)
for(i in 1:5){for( i in 1:5){G[i,j]=Ptau1[i,j]/trace(t(Ptau1)%*%Ptau1)}}

G
G1=Re(G)
G2=sqrt(Re(G)^2+Im(G)^2)
G1
G2
