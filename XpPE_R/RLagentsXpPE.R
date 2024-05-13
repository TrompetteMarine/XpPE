 set.seed(1)
k =vector("numeric",length(x))
alpha = runif(1,0,1)
gamma = runif(100,0,1)
x = rnorm(100,3,4)

for(i in 1:length(x)){
  k= (1-exp(gamma[i]*x[i]))/(1-exp(x[i]))
}


u2= function(argument){
  return(argument+alpha*mean(argument)-(1-alpha)*exp(argument-mean(argument)))
}

u3= function(argument){
  return(argument+alpha*mean(argument)+(1-alpha)*exp(argument-mean(argument)))
}


u <- function(argument) {
  v <- numeric(length(argument))
  for (i in 1:length(argument)) {
    if (argument[i] < mean(argument)) {
      v[i] <- u2(argument[i])
    } else if (argument[i] > mean(argument)) {
      v[i] <- u3(argument[i])
    } else {
      v[i] <- u2(argument[i])
    }
  }
  return(v)
}



Ut <- function(argument) {
  v <- numeric(length(argument))
  for (i in 1:length(argument)) {
    pers = mean(argument[-i])
    if (argument[i] < (1+gamma)*pers) {
      v[i] <- u2(argument[i])
    } else if (argument[i] > pers) {
      v[i] <- u3(argument[i])
    } else {
      v[i] <- u2(argument[i])
    }
  }
  return(v)
}
plot(u2(k))
plot(Ut(k))

plot(u(k))