# Outward facing method(s)
def collapse(value = None):
    
        tempValue = 0;
            
        for i in range(len(storedValue)):
                
            tempValue += int(storedValue[i])
            
        storedValue = str(tempValue)