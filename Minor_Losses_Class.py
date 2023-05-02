class MinorLosses:
    #use for every flow outlet of the bucket(four)
    #determines minor loss for every pipe component in that outlet of flow
    def __init__(self, velocity, k_list, num_list):
        self.velocity = velocity  # Velocity of the
        self.k_list = k_list  # List of minor loss coefficients for every 
        self.num_list = num_list # List of number of components for each fitti
        
    def calculate_minor_loss(self):
        # Calculates the total minor loss due to all components in the pipe
        minor_loss = sum([k * (self.velocity**2 / (2 * g)) * num for k, num in zip(self.k_list, self.num_list)])
        return minor_loss