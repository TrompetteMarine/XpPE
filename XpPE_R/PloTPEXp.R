library(ggplot2)

y1 = BETA[,1:10]
y2 = BETA[,11:21]
x  = seq(from=0,to=10,by=0.5)

m$y =(c(-y1[1,],-y2[1,]))
m$id = 1:21
m$Group = ifelse(male$id<= 10, "Treatment","Control")
m$x= c(rep(1:10,times=2,each=1),NA)

ggplot(data=male, aes(x,y))+
  geom_smooth(aes(fill=Group))+
  ylab("Diffused Overconfidence")+
  xlab("Number Of Trials")+
  theme(legend.position = c(0.8,0.5),legend.title = element_blank(),legend.background = element_blank())

b=data.frame(1:21)
b$y =(c(y1[2,],y2[2,]))
b$id = 1:21
b$Group = ifelse(male$id<= 10, "Treatment","Control")
b$x= c(rep(1:10,times=2,each=1),NA)

ggplot(data=b, aes(x,y))+
  geom_smooth(aes(fill=Group))+
  ylab("Diffused Overconfidence")+
  xlab("Number Of Trials")+
  theme(legend.position = c(0.3,0.9),legend.title = element_blank(),legend.background = element_blank())

c=data.frame(1:21)
c$y =(c(y1[3,],y2[3,]))
c$id = 1:21
c$Group = ifelse(male$id<= 10, "Treatment","Control")
c$x= c(rep(1:10,times=2,each=1),NA)

ggplot(data=c, aes(x,y))+
  geom_smooth(aes(fill=Group))+
  ylab("Diffused Overconfidence")+
  xlab("Number Of Trials")+
  theme(legend.position = c(0.8,0.9),legend.title = element_blank(),legend.background = element_blank())

d=data.frame(1:21)
d$y =(c(y1[4,],y2[4,]))
d$id = 1:21
d$Group = ifelse(male$id<= 10, "Treatment","Control")
d$x= c(rep(1:10,times=2,each=1),NA)

ggplot(data=d, aes(x,y))+
  geom_smooth(aes(fill=Group))+
  ylab("Diffused Overconfidence")+
  xlab("Number Of Trials")+
  theme(legend.position = c(0.8,0.9),legend.title = element_blank(),legend.background = element_blank())


e=data.frame(1:21)
e$y =(c(y1[5,],y2[5,]))
e$id = 1:21
e$Group = ifelse(male$id<= 10, "Treatment","Control")
e$x= c(rep(1:10,times=2,each=1),NA)

ggplot(data=e, aes(x,y))+
  geom_smooth(aes(fill=Group))+
  ylab("Diffused Overconfidence")+
  xlab("Number Of Trials")+
  theme(legend.position = c(0.8,0.9),legend.title = element_blank(),legend.background = element_blank())

f=data.frame(1:21)
f$y =(c(y1[6,],y2[6,]))
f$id = 1:21
f$Group = ifelse(male$id<= 10, "Treatment","Control")
f$x= c(rep(1:10,times=2,each=1),NA)

ggplot(data=f, aes(x,y))+
  geom_smooth(aes(fill=Group))+
  ylab("Diffused Overconfidence")+
  xlab("Number Of Trials")+
  theme(legend.position = c(0.8,0.9),legend.title = element_blank(),legend.background = element_blank())

g=data.frame(1:21)
g$y =(c(y1[7,],y2[7,]))
g$id = 1:21
g$Group = ifelse(male$id<= 10, "Treatment","Control")
g$x= c(rep(1:10,times=2,each=1),NA)

ggplot(data=g, aes(x,y))+
  geom_smooth(aes(fill=Group))+
  ylab("Diffused Overconfidence")+
  xlab("Number Of Trials")+
  theme(legend.position = c(0.8,0.9),legend.title = element_blank(),legend.background = element_blank())

h=data.frame(1:21)
h$y =(c(y1[8,],y2[8,]))
h$id = 1:21
h$Group = ifelse(male$id<= 10, "Treatment","Control")
h$x= c(rep(1:10,times=2,each=1),NA)

ggplot(data=h, aes(x,y))+
  geom_smooth(aes(fill=Group))+
  ylab("Diffused Overconfidence")+
  xlab("Number Of Trials")+
  theme(legend.position = c(0.8,0.4),legend.title = element_blank(),legend.background = element_blank())

