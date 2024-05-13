X = 1:10
n =c(18,12,10,8,6,6,5,3,2,2)
N= sum(n)
p= n/N
v=vector("numeric",10)
for(i in 1:10){
  v[i]=p[i]*X[i]
}

mu=sum(v)
v2= rnorm(10,mu,sd(v))

plot(density(v))
plot(density(v2))
density(X*p)

