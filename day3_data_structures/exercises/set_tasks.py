print(" --- Duplicate Silme ---")

thisset = {"apple", "banana", "cherry", "apple"}
thisset.add("banana")
print(thisset)

print("\n//////////////////\n")
print(" --- union / intersection ---")

x = {"apple", "banana", "cherry"}
y = {"microsoft", "apple", "google"}

intersection_result = x & y 
print("intersection: ", intersection_result)

union_result = x | y 
print("union: ", union_result)