import sys

filename = sys.argv[1] 
with open(filename) as data:
    depth_measurements = [ line.strip() for line in data]
count = 0
for i in range(0, len(depth_measurements)-1):
    difference = int(depth_measurements[i]) - int(depth_measurements[i+1])
    if difference < 0:
        count+=1
print(count)