from datetime import datetime

# record current timestamp
start = datetime.now()

# create loop-setup for testing
test_list = []
a = 0
for i in range(1000):
    test_list.append(i)
print(test_list)

# record loop end timestamp
end = datetime.now()

# find difference loop start and end time and display
duration = (end - start).total_seconds() * 10 ** 3
print(f"The time of execution of above program is : {duration:.03f}ms")
