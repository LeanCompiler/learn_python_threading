import time
import threading

# note start time
start = time.perf_counter()


# function to sleep for one second
def sleep_one_second():
    print("ima slep")
    time.sleep(1)
    print("i'm up. where am i??")


threads = []
for _ in range(5):
    t = threading.Thread(target=sleep_one_second)
    threads.append(t)
    t.start()

# for thread in threads:
#     # waits for the threads to finish before moving on
#     thread.join()

# calculate finish time
finish = time.perf_counter()
print(f"\n Finished in {(finish - start)} seconds(s).")
