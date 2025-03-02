import time
import math

num = int(input())  
ms = int(input())   

time.sleep(ms / 1000)  
print(f"Square root of {num} after {ms} milliseconds is {math.sqrt(num)}")