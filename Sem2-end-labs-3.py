# Author RTS 1/28/22

def remainder(dividend,divisor): 
    while divisor <= dividend:   # making sure divisor is lessthan or = than the dividen 
      dividend = dividend - divisor# dividen - divisor = dividen 
    return dividend # Return the final dividend 


fin_remainder=remainder(10,2)
print(fin_remainder)
