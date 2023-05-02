def ReturnMinorLoss(entry):
    
    if(entry == 'A'): #90 degrees elbow Bend
        print("Flanged = 0", '\n', "Threaded = 1")
        select = int(input())
        if(select == 0):
            return(0.3)
        elif(select == 1):
            return(0.9)
        else:
            return(-1)
        
    elif(entry == "B"): #90 Degrees Miter Bend
        print("Vaneless = 0", '\n', "Vanned = 1")
        select = int(input())
        if(select == 0):
            return(1.1)
        elif(select == 1):
            return(0.2)
        else:
            return(-1)

    elif(entry == "C"): #45 Degrees threaded Elbow Bend
        return(0.4)
    
    elif(entry == "D"): #180 Degrees Return Bend
        print("Flanged = 0", '\n', "Threaded = 1")
        select = int(input())
        if(select == 0):
            return(0.1)
        elif(select == 1):
            return(1.5)
        else:
            return(-1)
    
    elif(entry == "E"): #Tee Branch Flow
        print("Flanged = 0", '\n', "Threaded = 1")
        select = int(input())
        if(select == 0):
            return(1.0)
        elif(select == 1):
            return(2.0)
        else:
            return(-1)
    
    elif(entry == "F"): #Tee Line Flow
        print("Flanged = 0", '\n', "Threaded = 1")
        select = int(input())
        if(select == 0):
            return(0.2)
        elif(select == 1):
            return(0.9)
        else:
            return(-1)
    
    elif(entry == "G"): #Threaded Union
        return (0.08)
    
    elif(entry == "H"):
        return 1
    
    else:
        return -1