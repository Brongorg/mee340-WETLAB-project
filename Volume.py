def grouptask2volume(maxh=0.675,minh=0.03,dh=0.015,height=0.75,top=1.5,bottom=0.8):
    
    #Default values are currently set to find volume in Problem 1
    #For Problem 2, shape of reservoir changes to rectangular; need to change Vol[] accordingly
    #For Problem 3, change in dh is required when calling the function
    
    minh = minh - 0.001                     #correction for np.arange to include endpoint
    h = np.arange(maxh,minh,-dh)            #Define array to contain all values of height (h) given dh
               
    deltaRMax = (top-bottom)/2              #Define array to contain radii toward finding volume in each subdivision
    radii = []

    for i in h:
        radii.append((bottom/2)+((deltaRMax/height)*i))
        
        
    Vol = []                                #Calculate Volume for each height division

    for i in radii:
        Vol.append(math.pi*(i**2)*dh)
