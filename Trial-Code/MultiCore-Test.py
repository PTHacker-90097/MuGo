'''
@@@
'''
import multiprocessing as mp
import time

def count_to_ten(process_id: int) -> None:
    """Task executed by a worker process on a separate CPU core."""
    for i in range(1, 11):
        print(f"Core/Process #{process_id} counting: {i}")
        # Small sleep to clearly demonstrate interleaving across cores
        time.sleep(0.01)

if __name__ == "__main__":
    # Determine available physical/logical CPU cores
    num_cores = mp.cpu_count()
    print(f"Spawning worker processes across {num_cores} available cores...\n")

    processes = []

    # 1. Spawn a process for each core
    for p_id in range(num_cores):
        p = mp.Process(target=count_to_ten, args=(p_id,))
        processes.append(p)
        p.start()  # Launches execution on an available CPU core

    # 2. Wait for all processes to complete before continuing
    for p in processes:
        p.join()

    print("\nAll cores finished counting to 10!")