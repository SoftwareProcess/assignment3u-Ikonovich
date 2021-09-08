# Outward facing method(s)
def collapse(value = None):
    
    if (isinstance(value,str) and (value.isnumeric()) and (len(value) < 51)):
    
        storedValue = value;
        
        while len(storedValue) > 1:
            tempValue = 0;
            
            for i in range(len(storedValue)):
                
                tempValue += int(storedValue[i])
                storedValue = str(tempValue)
            
        return storedValue
    
    else: 
        return None
            
        
        






# Inward facing methods
