# Author RTS 1/28/22

def open_senior(data):  
    rest = [] # Blank list
    for index in data:    
      if index[0] >= 55 and index[1] > 7: # Setting peramiters 
        rest.append("Senior")     
      else:
        rest.append("Open") # if not append open
    return rest # Return final


new=open_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]])

print(new)