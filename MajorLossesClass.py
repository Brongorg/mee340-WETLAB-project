from scipy.optimize import root_scalar
import math

class MajorLosses:
    def __init__(self, density, diameter, roughness, length, dyn_visc,maxh,minh):
        self.density = density
        self.diameter = diameter
        self.roughness = roughness
        self.length = length
        self.dyn_visc = dyn_visc
        self.maxh = maxh
        self.minh = minh


            
            

    def calculate_Time(self):
           
        
       
        minh = minh - 0.0000001 
        h = np.arange(maxh,minh,-dh) 

        Vol = [] 
        for i in [h]:
            Vol.append(length*width*dh)

        Vave = []
        for x in [h]: 
            Vguess = math.sqrt(2*g*x) 
            flag = 1

            while (flag == 1):
                hf = 0 
                for i in range(len(ENTER DIMATER ARRAY)):
                    Re = Vguess*D[i]/nu   # CALL dimater LOCATION
                    F = (1/-1.8*math.log10(6.9/Re))**2
                    hf += F*L[i]/D[i]*((Vguess**2)/(2*g))# CALL dimater AND LENGTH LOCATION
                Vresult = math.sqrt((2*g*x)/(1+hf+minorLoss))#CALL MINOR LOSS FUNCTION
                errorTest = (Vguess-Vresult)/(Vresult)

                if (errorTest > -alpha and errorTest < alpha): #error estimation: if change in height is sufficiently low, use current V as Vave for the height
                    Vave.append(Vresult)
                    flag = 0
                else:
                    Vguess = Vresult #Reset/Update Vguess 

            return Vave

        area = #LENGTH * WIDTH 
        deltaT = []
        i = 0 #index counter
        for j in Vave:
            deltaT.append(Vol[i]/(j*area))
            i = i+1


        #Find total time (in seconds) to deplete tank by summing elements in deltaT
        total = sum(deltaT)
        print(total)