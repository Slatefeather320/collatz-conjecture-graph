import matplotlib.pyplot as plt

def cool(x, e, o): #user can define what happens when the number is odd or even (devide by 2 and multiply by 3 by default)
    result = []
    cooling = True
    while cooling:
        if x%2==0:
            x /= e 
        else:
            x = (x*o)+1
        
        if x in result: #breaks the loop when numbers start repeating
            cooling = False
        result.append(x) 
    gy = result
    gx = range(0,len(gy))
    plt.plot(gx, gy)
    plt.xlabel('Iteration')
    plt.ylabel('Value')
    plt.show()

cool(100,2,3) #put whatever number you want to generate a graph of here. 
