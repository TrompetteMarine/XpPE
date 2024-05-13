import numpy as np 
import random as rd
import seaborn as sns
import statistics as s
import matplotlib.pyplot as plt 
from matplotlib.pyplot import *
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.patches as mp
# Probabilities of ot(t) $\tau_t(k)$ in the limite cases t->∞

rd.seed(1)
        
# Plot 

def Plot_Theory (n=3):
 x  = np.linspace(0,5,100)
 x1 = np.linspace(0,5,100)
 y1 = np.linspace(0,5,100)
 y2 = np.linspace(1,5,100)
 y3 = np.linspace(0,5,100)
 for i in range (len(x)):
       y1[i]= 0.5+rd.gauss(0,0.15)
       y3[i]= 0.5

 fig,ax = plt.subplots()
 
 Expected,    = ax.plot(y1,label='Expected',linestyle='--')
 Theory,      = ax.plot(y3,label='Theoritical Predictions',linestyle='solid',color='r') 
 legend       = ax.legend(handles=[Expected,Theory],loc="lower left")
 plt.ylim([0,1])
 plt.rc('text',usetex=True)
 ax.set_xlabel('Time steps (number of moves)')
 ax.set_ylabel(r'$P(A_t|A_{t-1})$')
 
 

def Plot_Exp (n=3):
 x  = np.linspace(0,5,100)
 x1 = np.linspace(0,5,100)
 y1 = np.random.negative_binomial(1,0.5,100)
 y2 = np.linspace(1,5,100)
 y22= np.linspace(1,5,100)
 y3 = np.linspace(0,5,100)
 y4 = np.linspace(0,5,100)
 for i in range (len(x)):
       x1[i]= np.random.negative_binomial(2,0.5,1)/8
       y1[i]= 0.5*y1[i-1]+rd.gauss(0,1)
       y3[i]= 0.5
       if (i <=35):
             y2[i]=0.7+rd.gauss(0,0.2)
             y22[i]=0.49+rd.gauss(0.03,0.05)
       if (i >35):
             y2[i]= 1/x[i]  +rd.gauss(0.2,0.2)
             y22[i]= 1/x[i] +rd.gauss(0.05,0.05)
       if (i>91) and (i<100):
             y22[i]=np.abs(rd.gauss(0.05,0.05))
       if (i==100):
             y22[i]=0
       #y1[i]= ((x1[i-1]+ y1[i])/2+ np.abs(rd.gauss(0,1)))/8
       
 y1 = y1/2
 y2 = y2/5
 
 for i in range(len(x)):
     if (i<= 35):
         y4[i] = 50 + rd.gauss(5,12)
     if (i >35) and (i<=50):
         y4[i] = 30-y2[i] +np.random.noncentral_chisquare(i+1,0,1)
     if(i>=50):
         y4[i] = 1-y2[i] +np.random.noncentral_chisquare(i+2,0,1)
     if(y4[i]>1):
         y4[i]= y4[i]*0.9
 
 y4=y4/118
 fig,ax = plt.subplots()
 
 Ag,          = ax.plot(y4-0.5,label='Favorability bias',linestyle='--')
 Conservative,= ax.plot(y22-0.5,label='Hostility bias',linestyle='--')
 Theory,      = ax.plot(y3-0.5,label='Theoritical Predictions (bias-free)',linestyle='solid',color='r') 
 legend       = ax.legend(handles=[Ag,Conservative,Theory],loc="upper left")
 plt.ylim([-1,1])
 plt.rc('text',usetex=True)
 ax.set_xlabel('Time steps (number of moves)')
 #ax.set_ylabel(r'$P(A_t|A_{t-1})$')
 ax.set_ylabel('A-Priori Score')
 #plt.plot(x,np.random.negative_binomial(1,0.5,100)/9)
 #plt.plot(x,x1)


#Plot_Theory()
Plot_Exp()
plt.show()