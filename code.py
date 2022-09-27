import matplotlib.pyplot as plt

def cool(x, e, o): 
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
    return result

y = cool(100,2,3)
x = range(0,len(y))
plt.xlabel('Iteration')
plt.ylabel('Value')
plt.plot(x,y)
plt.show()
