import numpy as np 
import random as rd
import seaborn as sns
import statistics as s
import matplotlib.pyplot as plt 
from matplotlib.pyplot import *
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.patches as mp

rd.seed(1)

def Plot_ER_nAg (n=5):
 x  = np.linspace(0,5,100)
 y  = np.linspace(1,5,100)
 x1 = np.linspace(0,5,100)
 y1 = np.linspace(1,5,100)
 y2 = np.linspace(1,5,100)
 y3 = np.linspace(1,5,100)
 y4 = np.linspace(0,5,100)
 yT = np.linspace(0,5,100)
 
 for i in range (len(x)):
       x1[i]= np.random.negative_binomial(2,0.5,1)/8
       yT[i]= 0.5
       if (i <=25):
             y1[i]=0.5 +rd.gauss(0,0.02)
             y2[i]=0.49+rd.gauss(0.03,0.05)
             y3[i]=0.52+rd.gauss(0,0.02)
             y4[i]=0.55+rd.gauss(0.03,0.05)
       if (i >25) and (i<=35):
             y1[i]=0.45 +rd.gauss(0,0.02)
             y2[i]=0.49+rd.gauss(0.03,0.05)
             y3[i]=0.52+rd.gauss(0,0.02)
             y4[i]= 1/(x[i])    +rd.gauss(0.05,0.05)
       if (i >35) and (i<=91):
             y1[i]= 1/(1.5*x[i])   +rd.gauss(0.02,0.02)
             y2[i]= 1/(x[i])       +rd.gauss(0.05,0.05)+0.1
             y3[i]= 1/(x[i])       +rd.gauss(0.05,0.05)+0.1
             y4[i]= 1/(x[i]**2)    +rd.gauss(0.05,0.05)
       if (i>91) and (i<100):
             y1[i]=np.abs(rd.gauss(0.08,0.05))+0.03
             y2[i]=np.abs(rd.gauss(0.3,0.05))+0.05
             y3[i]=np.abs(rd.gauss(0.3,0.04))+0.05
             y4[i]=np.abs(rd.gauss(0,0.05))
       if (i==100):
             y1[i]=0.1
             y2[i]=0.37
             y3[i]=0.35
             y4[i]=0
       #y1[i]= ((x1[i-1]+ y1[i])/2+ np.abs(rd.gauss(0,1)))/8
       
 
 fig,ax = plt.subplots()
 
 nAg1,          = ax.plot(y1,label='Treatment 1',linestyle='--')
 nAg2,          = ax.plot(y2,label='Treatment 2',linestyle='--')
 nAg3,          = ax.plot(y3,label='Treatment 3',linestyle='--')
 nAg4,          = ax.plot(y4,label='Treatment 4',linestyle='--')
 Theory,        = ax.plot(yT,label='Theoritical Predictions',linestyle='solid',color='r') 
 legend         = ax.legend(handles=[nAg1,nAg2,nAg3,nAg4,Theory],loc="upper right")
 plt.ylim([0,1])
 plt.rc('text',usetex=True)
 ax.set_xlabel('Time steps (number of moves)')
 ax.set_ylabel(r'$P(A_t|A_{t-1})$')
 #plt.plot(x,np.random.negative_binomial(1,0.5,100)/9)
 #plt.plot(x,x1)
 
Plot_ER_nAg()
plt.show()