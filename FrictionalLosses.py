import Pipe_Info

def returnMajorLoss(pipeCount):
    






    return 1


def ReturnMinorLoss(input):
    
    if(input == 'A'): #90 degrees elbow Bend
        print("Flanged = 0", '\n', "Threaded = 1")
        select = int(input())
        if(select == 0):
            return(0.3)
        elif(select == 1):
            return(0.9)
        else:
            return(-1)
    
    elif(input == "B"): #90 Degrees Miter Bend
        print("Vaneless = 0", '\n', "Vanned = 1")
        select = int(input())
        if(select == 0):
            return(1.1)
        elif(select == 1):
            return(0.2)
        else:
            return(-1)

    elif(input == "C"): #45 Degrees threaded Elbow Bend
        return(0.4)
    
    elif(input == "D"): #180 Degrees Return Bend
        print("Flanged = 0", '\n', "Threaded = 1")
        select = int(input())
        if(select == 0):
            return(0.1)
        elif(select == 1):
            return(1.5)
        else:
            return(-1)
    
    elif(input == "E"): #Tee Branch Flow
        print("Flanged = 0", '\n', "Threaded = 1")
        select = int(input())
        if(select == 0):
            return(1.0)
        elif(select == 1):
            return(2.0)
        else:
            return(-1)
    
    elif(input == "F"): #Tee Line Flow
        print("Flanged = 0", '\n', "Threaded = 1")
        select = int(input())
        if(select == 0):
            return(0.2)
        elif(select == 1):
            return(0.9)
        else:
            return(-1)
    
    elif(input == "G"): #Threaded Union
        return (0.08)
    
    elif(input == "H"):
        return 1
    
    else:
        return -1
    


