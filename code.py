
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

print(cool(50,2,3))
