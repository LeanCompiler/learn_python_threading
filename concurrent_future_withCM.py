import time
import concurrent.futures

# note start time
start = time.perf_counter()


# function to sleep for one second
def sleep_one_second(seconds):
    print(f"ima slep for {seconds} seconds ok?")
    time.sleep(seconds)
    return f"i'm up in {seconds} seconds"


"""
The 'ThreadPoolExecutor' context manager implicitly waits for all tasks to complete before exiting,
ensuring the finish time calculation reflects the actual time taken for task completion.
This behavior is similar to an implicit join().

The 'with' context manager is responsible for ensuring that all tasks are completed before the program proceeds 
beyond the with block. The as_completed() function is used for handling the results as they become available, 
but it doesn't affect the waiting behavior of the ThreadPoolExecutor.

Future Object from .submit():-
A Future object represents the result of an asynchronous computation. Here's a more detailed explanation. 
Future object provides a way to monitor and interact with the result of an asynchronous operation that has not 
yet completed. It can be used to check if the operation is done, wait for its completion, and retrieve the result 
(or exception) once it is available.
"""

# CM - context manager
with concurrent.futures.ThreadPoolExecutor() as executor:
    # single
    """
    # submit returns a future object
          f1 = executor.submit(sleep_one_second, 1)
          print(f1.result())
    """

    # multiple - with submit
    """
    results = [executor.submit(sleep_one_second, 1) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())
    """

    # multiple - with submit & different seconds
    """
    secs = [3, 5, 1, 4, 2]
    # submit submits/starts the threads in the exact order as given
    #  submit returns a future object, here stored as iterable
    results = [executor.submit(sleep_one_second, sec) for sec in secs]

    #  as_completed prints in the order of completion
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    """

    # multiple - with map
    """
    secs = [1, 2, 5, 4, 3]
    #  map returns the return result in the order of given
    results = executor.map(sleep_one_second, secs)

    # prints in the order of given
    # seems as if 5,4,3 finished at once, but they haven't
    for result in results:
        print(result)
    """

# calculate finish time
finish = time.perf_counter()
print(f"\n Finished in {(finish - start)} seconds(s).")
