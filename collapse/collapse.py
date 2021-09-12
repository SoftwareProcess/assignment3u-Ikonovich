# Outward facing method(s)
def collapse(value = None):
        
        storedValue = value
        tempValue = 0;
            
        for i in range(len(storedValue)):
                
            tempValue += int(storedValue[i])
            
        return str(tempValue)