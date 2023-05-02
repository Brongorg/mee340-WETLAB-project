class pipe_Info: 

    # Initializes Variables
    #Accepts string, float, float, float , string)
    pipeType = None
    diameter = None
    length = None
    surfaceRoughness = None
    crossSectionalArea = None

    #Creates a Paramaterized constructor for the class
    def __init__(self, pT, d, l, sR, fN):
        self.pipeType = pT
        self. diameter = d
        self.length = l
        self.surfaceRoughness = sR
        self.crossSectionalArea= (3.14159*(d**2))/4

        #Class function to display information
    def displayClassInfo(self):
        print("pipeType: ", str(self.pipeType), '\n',
              "Surface Roughness: ", str(self.surfaceRoughness), '\n',
              "diameter: ", str(self.diameter), '\n',
              "length: ", str(self.pipeType), '\n',
              "Area: ", str(self.crossSectionalArea), '\n' )

