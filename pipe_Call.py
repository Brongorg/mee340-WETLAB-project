def pipeCall():
    pipe_type = input("Enter pipe type: ")
    diameter = float(input("Enter diameter of {} pipe (in meters): ".format(pipe_type)))
    length = float(input("Enter length of {} pipe (in meters): ".format(pipe_type)))
    epsilon = float(input("Enter epsilon of {} pipe (in millimeter): ".format(pipe_type)))
    num_pipes = int(input("Enter number of {} pipes: ".format(pipe_type)))
    cross_sectional_area = (3.14159 * (diameter ** 2)) / 4
    pipe_info = {
        "type": pipe_type,
        "diameter": diameter,
        "length": length,
        "epsilon": epsilon,
        "num_pipes": num_pipes,
        "cross_sectional_area": cross_sectional_area  
    }
    return pipe_info