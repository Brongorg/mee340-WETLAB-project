import numpy as np
import math

def grouptask2(maxh=0.675,minh=0.03,dh=0.015,
               height=0.75,top=1.5,bottom=0.8,
               g=9.81,nu=1.05*(10**-6),
               L=[8.00,12.00],D=[0.05,0.03],eps=[0,0],
               alpha=0.05):
    
    #Minor loss is a sum of losses from area contractions, sharp entrance and other turns, and ball valve, respectively
    #Default Values are set to solve Problem 1 in Group Task #2
    
    minh = minh - 0.0000000001                     #correction for np.arange to include endpoint
    h = np.arange(maxh,minh,-dh)            #Define array to contain all values of height (h) given dh
               
    deltaRMax = (top-bottom)/2              #Define array to contain radii toward finding volume in each subdivision
    radii = []

    for i in h:
        radii.append((bottom/2)+((deltaRMax/height)*i))
        
        
    Vol = []                                #Calculate Volume for each height division

    for i in radii:
        Vol.append(math.pi*(i**2)*dh)
        
        
    #Find Vave (Velocity at exit of piping) for each volume division
    #Note that major losses and pipe dimensions are only coming from the problems 
    #May need adjustments for actual lab
    
    Vave = []

    #Calculate major losses and select Vave for each h and volume division
    #Calculate total minor losses beforehand:
    
    minorLossContraction = float(input("Enter total minor loss from area contractions: "))
    minorLossTurns = float(input("Enter total minor loss from turns: "))
    
    minorLoss=minorLossContraction + minorLossTurns+ 0.5 + 1000*0.05/9.81
    #0.5 from sharp entry
    #last term from ball valve
    
    for x in h:
        Vguess = math.sqrt(2*g*x)   #start off with an ideal jet exit velocity
        flag = 1
    
        while (flag == 1):
            Re=[]
            F=[]
            Ratios=[]
            
            for a in D:
                Re.append(Vguess*a/nu)
                
            #For the purposes of shortening time for final calculation, the Haaland Equation will be implemented.
            
            i=0 #index counter
            for b in Re:
                F.append((1/(-1.8*math.log10(((eps[i]/(3.7*D[i]))**1.11)+(6.9/b)))**2))
                i=i+1
                
            i=0 #index counter
            for c in F:
                Ratios.append(c*L[i]/D[i])
                i=i+1
                
            
            Vresult = math.sqrt((2*g*x)/(1+sum(Ratios)+minorLoss))  #Update new V for error testing
            errorTest = (Vguess-Vresult)/(Vresult)
        
            if (errorTest > -alpha and errorTest < alpha):  #error estimation: if change in height is sufficiently low, use current V as Vave for the height
                Vave.append(Vresult)
                flag = 0
            else:
                Vguess = Vresult #Reset/Update Vguess
    
    
    #Obtain deltaT array to compute time to deplete each division

    print(D)
    area = (math.pi/4)*(D[len(D)-1]**2)
    
    #Replace D2 by D_(final pipe number)
    
    deltaT = []
    i = 0  #index counter

    for j in Vave:
        deltaT.append(Vol[i]/(j*area))
        i = i+1
        
        
    #Find total time (in seconds) to deplete tank by summing elements in deltaT

    total = sum(deltaT)
    print(total)
