import timeit 
import multiprocessing


def time_insertion(total_iterations, queue):
    time = timeit.timeit(
        "b = a[:]; insertion_sort(b, n)", # overhead is required else sort the same array multiple times
        setup="from insertion_sort import insertion_sort; import numpy as np; import random as rd; a = np.array([rd.randint(0, 1000000) for _ in range(10000)]); n = len(a)",
        number=total_iterations
    )

    queue.put(time / total_iterations)


def time_shell(total_iterations, queue):
    time = timeit.timeit(
        "b = a[:]; shell_sort(b, n)",
        setup="from shell_sort import shell_sort; import numpy as np; import random as rd; a = np.array([rd.randint(0, 1000000) for _ in range(10000)]); n = len(a)",
        number=total_iterations
    )
    
    queue.put(time / total_iterations)


def main():
    total_iterations = 5 # total number of times to run sort. might take a while depending on how high this number is
    insertion_time = multiprocessing.Queue()
    shell_time = multiprocessing.Queue()

    insertion_process = multiprocessing.Process(target=time_insertion, args=(total_iterations, insertion_time))
    shell_process = multiprocessing.Process(target=time_shell, args=(total_iterations, shell_time))

    insertion_process.start()
    shell_process.start()
    insertion_process.join()
    shell_process.join()

    insertion = insertion_time.get()
    shell = shell_time.get()
    print("Average insertion sort time:", insertion, "seconds")
    print("Average shell sort time:", shell, "seconds")
    with open("times.txt", "w") as f:
        f.write(f"Average insertion sort time: {insertion} seconds\n")
        f.write(f"Average shell sort time: {shell} seconds\n")
    


if __name__ == "__main__":
    try:
        import numpy
    except ImportError:
        print("Please install numpy before running")
        exit()
    main()