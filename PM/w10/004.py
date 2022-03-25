import gc

counter = 0

collected = gc.collect()
print(f"Collected {collected} objects.")

for i in range(10):
    x = {}
    x[counter + 1] = x
    counter += 1
    print(x)

collected = gc.collect()
print(f"Collected {collected} objects.")