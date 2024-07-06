import time
input("Press Enter key to start stopwatch: ")
start_time=time.time()
print("Time Started!!!")
input("Press Enter key to stop stopwatch: ")
total_time=time.time()-start_time
print("Time Stopped!!!")

print(f"Total time taken :{total_time:.2f}")

