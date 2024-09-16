#the following code implements gradent desent and gives the equation for cost function by using which we can predect the cost of houses.
import numpy as np 
import matplotlib.pyplot as plt 
def multi_variable(price,price_pre):
    # when u have more than one feature to fit a model based on the distrubution of the data
    # make a eqn which closely relates to the given data
    
def error(price,price_pre):
    cost=np.sum((price-price_pre)**2/len(price))
    return cost
def gradient_decent(x,y,it=1000,learrning_rate=0.001,n):
    learrning_rate=0.00001
    price=y
    #slope=0.01
    #intercept=0.01
     n=float(len(x))
    var = np.full((1,n+1),0.001)
   
    previous_cost=None
    for i in range(it):
        price_pre=slope*x+intercept
        cost = error(price,price_pre)
        if(previous_cost is not None and previous_cost-cost<=1e-6): break
        previous_cost=cost
        #derivative section
        for i in range n:
            # list of slopes of size n+1 where l[0]=1 always
             der_var[i]=-2/n*sum(x[i]*(price-price_pre))
             #intercept_derivative=-2/n*sum(price-price_pre)
        var[i]=var[i]-learning_rate*(der_var[i])
        #intercept=intercept-learning_rate*(intercept_derivative)
    print(f"slope:{slope},intercept{intercept}")
def main():
     
    # Data
    X = np.array([32.50234527, 53.42680403, 61.53035803, 47.47563963, 59.81320787,
           55.14218841, 52.21179669, 39.29956669, 48.10504169, 52.55001444,
           45.41973014, 54.35163488, 44.1640495 , 58.16847072, 56.72720806,
           48.95588857, 44.68719623, 60.29732685, 45.61864377, 38.81681754])
    Y = np.array([31.70700585, 68.77759598, 62.5623823 , 71.54663223, 87.23092513,
           78.21151827, 79.64197305, 59.17148932, 75.3312423 , 71.30087989,
           55.16567715, 82.47884676, 62.00892325, 75.39287043, 81.43619216,
           60.72360244, 82.89250373, 97.37989686, 48.84715332, 56.87721319])
    gradient_decent(X,Y)
if __name__=='__main__':
    main()
