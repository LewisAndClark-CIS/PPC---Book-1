import time
import random
endTime  = 30
start = time.time()

while True: 
    currTime  = time.time() - start
    print(random.randint(0,100))
    time.sleep(3)
    if currTime  >= endTime:
         break
    
#Completed: Yes
#Errors: None
#Solved: N/A
#Difficult: Ending after 30 sedonds
