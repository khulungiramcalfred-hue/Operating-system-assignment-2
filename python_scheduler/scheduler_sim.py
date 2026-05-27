import matplotlib.pyplot as plt
import argparse
import random

def generate_processes(n):
    processes = []
    for i in range(n):
        processes.append({
            "pid": i + 1,
            "arrival": random.randint(0, 5),
            "burst": random.randint(1, 10)
        })
    return processes

# FCFS ALGORITHM
def fcfs(processes):
    processes.sort(key=lambda x: x["arrival"])

    time = 0
    results = []

    for p in processes:
        if time < p["arrival"]:
            time = p["arrival"]

        start = time
        finish = time + p["burst"]

        waiting = start - p["arrival"]
        turnaround = finish - p["arrival"]

        results.append({
            "pid": p["pid"],
            "start": start,
            "finish": finish,
            "waiting": waiting,
            "turnaround": turnaround
        })

        time = finish

    return results

# GANTT CHART FUNCTION
def gantt_chart(results):
    process_ids = [r["pid"] for r in results]
    start_times = [r["start"] for r in results]
    durations = [r["finish"] - r["start"] for r in results]

    plt.barh(process_ids, durations, left=start_times)
    plt.xlabel("Time")
    plt.ylabel("Process ID")
    plt.title("FCFS Gantt Chart")
    plt.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--random", type=int, default=5)

    args = parser.parse_args()

    print("\n=== EduOS Scheduler Simulator (FCFS) ===")

    processes = generate_processes(args.random)

    print("\nGenerated Processes:")
    for p in processes:
        print(p)

    results = fcfs(processes)

    print("\nFCFS Results:")
    for r in results:
        print(r)

    # CALL GRAPH HERE (correct place)
    gantt_chart(results)

if __name__ == "__main__":
    main()