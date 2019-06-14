import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Put all list 1 in a dictionary, O(n)
duplicates = []
names1_dict = {}
for name_1 in names_1:
    names1_dict[name_1] = 0

# Check each item in list 2 against the dictionary, O(n)
for name in names_2:
    if name in names1_dict:
        duplicates.append(name)

end_time = time.time()

duplicates = sorted(duplicates)
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
# Total time complexity, O(2n) -> O(n). Total runtime: 0.00639 seconds.




# Stretch goal.  I restart all the processes to get their collective time.
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# I first sort the name lists, which is O(nlog(n))
names_1 = sorted(names_1)
names_2 = sorted(names_2)

# First I just ran a simple "is in" statement, which I thought might benefit from
# the list sortedness.  Total runtime: 1.786 seconds

# for name in names_2:
#     if name in names_1:
#         duplicates.append(name)


# Then I coded up a simple binary search, which definitely uses the list sortedness
# in order to search in an additional nlog(n).  This brings the overall time to 
# O(2nlog(n)) -> O(nlog(n)).  Total runtime: 0.0907 seconds, just one order of
# magnitude worse than the dictionary solution from before.

for name in names_2:
    start = 0
    end = len(names_1)
    middle = start + (end-start) // 2

    while end-start > 1:
        middle = start + (end-start) // 2 # middle index
        
        # If that's the answer, end
        if name == names_1[middle]:
            duplicates.append(name)
            break
        
        elif name < names_1[middle]:
            end = middle

        else:
            start = middle


end_time = time.time()
duplicates = sorted(duplicates)
print()
print (f"Stretch runtime: {end_time - start_time} seconds")
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
