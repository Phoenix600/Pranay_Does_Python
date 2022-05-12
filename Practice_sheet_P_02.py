def getDigitalRoot(x) :
    if x  < 10 : 
        return x
    x = int(x%10) + int(getDigitalRoot(x/10))
    return  x if x < 10 else getDigitalRoot(x)

print(round(getDigitalRoot(1729)))
print(round(getDigitalRoot(45893)))
print(round(getDigitalRoot(121212)))
print(getDigitalRoot(45893))

