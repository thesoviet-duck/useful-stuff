from datetime import datetime

# record the current timestamp
start = datetime.now()

## EXAMPLE CODE ##
test_list = []
a = 0
for i in range(1000):
    test_list.append(i)
print(test_list)
## END OF EXAMPLE CODE ##

# record loop end timestamp
end = datetime.now()

# find the difference between loop start and end time and display it
duration = (end - start).total_seconds() * 10 ** 3
# this will display in seconds rounded to 3 significant figures
print(f"\n\nThe runtime of the program is program is: {duration*0.001:.02f}s")
# uncomment the below code if you want to show in milliseconds
#print(f"\n\nThe runtime of the program is program is: {duration:.03f}ms")
