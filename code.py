def cool(x):
    result = []
    cooling = True
    while cooling:
        if x%2==0:
            x /= 2 
        else:
            x = (x*3)+1
        
        if x in result: #breaks the loop when numbers start repeating
            cooling = False
        result.append(int(x)) 
    return result

print(cool(50))
