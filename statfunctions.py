# Definition of functions for the calculation of the various statistical estimates in section "Descriptive Statistics"

def genMean(x, m):

    """ Calculation of a generalized mean """

    S = 0

    for value in x:
        mean = value**m
        S += mean

    mean_x = (1./len(x) * S)**(1./m)

    return mean_x

################################

def residual(x):
    
    """ Calculate the residual (x_i - mean_x) """
    
    mean_x = genMean(M, m)
    res = []
    
    for value in x:
        res.append(value - mean_x)
    
    return res

################################

def variance(x):
    
    """ Calculate the variance of x """

    mean_x = genMean(M, m)
    S = 0

    for value in x:
        sigma = (value - mean_x)**2
        S += sigma

    var = (1./(len(x)-1)) * S

    return var

################################

def covariance(x, y):
    
    """ Calculate the covariance of x """
    
    if len(x) != len(y):
        print "X and Y arrays MUST have equal lenght!"
        return
    
    n = len(x)
    
#    x_bar = mySum(x)/n
#    y_bar = mySum(y)/n

    S = 0
    
    res_x = residual(x)
    res_y = residual(y)
    
    for i in range(n):
        S += res_x[i] * res_y[i]
    
    return (1./(n-1)) * S