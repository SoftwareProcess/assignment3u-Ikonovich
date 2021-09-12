# Outward facing method(s)
def collapse(value = None):
    
    if (isinstance(value,str) and (len(value) < 51) and (value.isnumeric()) ):
        
        storedValue = value
        
        while (len(storedValue) > 1):
            tempValue = 0;
                
            for i in range(len(storedValue)):
                    
                tempValue += int(storedValue[i])
                
            storedValue = str(tempValue)
            
        return storedValue