import numpy as np 
import random as rd
import seaborn as sns
import statistics as s
import matplotlib.pyplot as plt 
from matplotlib.pyplot import *
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.patches as mp

rd.seed(1)
        
# Plot Agressive by treatments

def Plot_ER_Ag (n=5):
 #Variables set up
 x  = np.linspace(0,5,100)
 x1 = np.linspace(0,5,100)
 y1 = np.random.negative_binomial(1,0.5,100)
 
 #Models for agressive behaviours
 y2 = np.linspace(1,5,100)
 y22= np.linspace(1,5,100)
 y23= np.linspace(1,5,100)
 y24= np.linspace(1,5,100)
 y25= np.linspace(1,5,100)
 
 #Theoritical Predictions 
 y3 = np.linspace(0,5,100)
 
 for i in range (len(x)):
       x1[i]= np.random.negative_binomial(2,0.5,1)/8
       y1[i]= 0.5*y1[i-1]+rd.gauss(0,1)
       y3[i]= 0.5
       if (i <=35):
             y2[i]=0.7+rd.gauss(0,0.2)     
       if (i >35):
             y2[i]= 1/x[i]  +rd.gauss(0.2,0.2)
      
 y1 = y1/2
 y2 = y2/5
 
 for i in range(len(x)):
     if (i<= 30):
         y22[i] = 50 + rd.gauss(5,12)
     if (i >30) and (i<=45):
         y22[i] = 30-y2[i] +np.random.noncentral_chisquare(i+1,0,1)
     if (i >45) and (i<=50):
         y22[i] = 25-y2[i] +np.random.noncentral_chisquare(i+1,0,1)
     if(i>=50) :
         y22[i] = 1-y2[i] +np.random.noncentral_chisquare(i+2,0,1)
     if(i>=65) and (y22[i]<76):
         y22[i] = 70+ np.abs(y22[i]-y22[i-1])
     if(y22[i]>110):
         y22[i] = (y22[i])/(1+y22[i])*110
 
 y22=y22/118
 
 for i in range(len(x)):
     if (i<= 35):
         y23[i] = 50 + rd.gauss(5,12)
     if (i >35) and (i<=50):
         y23[i] = 30-y2[i] +np.random.noncentral_chisquare(i+1,0,1)
     if(i>=50):
         y23[i] = 1-y2[i] +np.random.noncentral_chisquare(i+2,0,1)
     if(y23[i]>118):
         y23[i] = y23[i]*0.9

 y23=y23/118

 for i in range(len(x)):
     if (i<= 30):
         y24[i] = 50 + rd.gauss(5,12)
     if (i >30) and (i<=45):
         y24[i] = 50 +np.random.noncentral_chisquare(25,0,1)+rd.gauss(6,6)
     if (i >45) and (i<=50):
         y24[i] = 60 +np.random.noncentral_chisquare(20,0,1)+rd.gauss(6,6)
     if(i>=50):
         y24[i] = 53+ +np.random.noncentral_chisquare(10,0,1)+rd.gauss(6,4)
     if(y24[i]>118):
         y24[i] = y24[i]*0.9
      
 y24=y24/118
 
 for i in range(len(x)):
         y25[i] = 52 + rd.gauss(6,6)
     
 y25=y25/118
 
 #Plots
 fig,ax = plt.subplots()
 
 Ag1,          = ax.plot(y22,label='Treatment 1',linestyle='--') # 1 overconfident person in the group
 Ag2,          = ax.plot(y23,label='Treatment 2',linestyle='--') # 2 overconfident persons in the group
 Ag3,          = ax.plot(y24,label='Treatment 3',linestyle='--') # 3 overconfident persons in the group
 Ag4,          = ax.plot(y25,label='Treatment 4',linestyle='--') # 4 overconfident persons in the group
 Theory,       = ax.plot(y3,label='Theoritical Predictions',linestyle='solid',color='r') 
 legend        = ax.legend(handles=[Ag1,Ag2,Ag3,Ag4,Theory],loc="lower right")
 plt.ylim([0,1])
 plt.rc('text',usetex=True)
 ax.set_xlabel('Time steps (number of moves)')
 ax.set_ylabel(r'$P(A_t|A_{t-1})$')
 

Plot_ER_Ag()
plt.show()