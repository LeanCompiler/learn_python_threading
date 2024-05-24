import time
import concurrent.futures

# Note start time
start = time.perf_counter()


# Function to sleep for one second
def sleep_one_second(seconds):
    print(f"ima slep for {seconds} seconds ok?")
    time.sleep(seconds)
    print("i'm up. where tf am i??")


# Submit tasks to the ThreadPoolExecutor but do not wait for them to complete
# Same as without .join() in classic threading
executor = concurrent.futures.ThreadPoolExecutor()
results = [executor.submit(sleep_one_second, 1) for _ in range(10)]

# Calculate finish time without waiting for futures to complete
finish = time.perf_counter()
print(f"\n Finished in {(finish - start)} seconds(s).")

# Shutdown the executor without waiting for tasks to complete
executor.shutdown(wait=False)
