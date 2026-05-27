import argparse
import random
from tabulate import tabulate

from python_scheduler.algorithms.fcfs import fcfs
from python_scheduler.algorithms.sjf import sjf
from python_scheduler.algorithms.priority import priority_scheduling
from python_scheduler.algorithms.round_robin import round_robin
from python_scheduler.metrics import compare_algorithms


# ----------------------------
# PROCESS GENERATOR
# ----------------------------
def generate_processes(n):
    processes = []
    for i in range(n):
        processes.append({
            "pid": i + 1,
            "arrival": random.randint(0, 5),
            "burst": random.randint(1, 10),
            "priority": random.randint(1, 5)
        })
    return processes


# ----------------------------
# PRINT TABLE FUNCTION
# ----------------------------
def print_table(results):
    table = []

    for r in results:
        table.append([
            r["pid"],
            r["start"],
            r["finish"],
            r["waiting"],
            r["turnaround"]
        ])

    print("\n=== SCHEDULING RESULT TABLE ===")

    print(tabulate(
        table,
        headers=["PID", "Start", "Finish", "Waiting", "Turnaround"],
        tablefmt="grid"
    ))


# ----------------------------
# MAIN CONTROLLER
# ----------------------------
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--random", type=int, default=5)
    parser.add_argument("--quantum", type=int, default=2)
    parser.add_argument("--algo", type=str, default="fcfs")

    args = parser.parse_args()

    processes = generate_processes(args.random)

    print("\n=== EduOS Controller ===")
    print("Algorithm:", args.algo)

    print("\nGenerated Processes:")
    for p in processes:
        print(p)

    # ----------------------------
    # COMPARISON MODE
    # ----------------------------
    if args.algo == "compare":
        print("\n=== COMPARISON MODE ===")

        fcfs_result = fcfs(processes)
        sjf_result = sjf(processes)
        rr_result = round_robin(processes, args.quantum)
        priority_result = priority_scheduling(processes)

        comparison = compare_algorithms(
            fcfs_result,
            sjf_result,
            rr_result,
            priority_result
        )

        print("\n=== COMPARISON RESULTS ===")

        for algo, stats in comparison.items():
            print(f"\n{algo}")
            print("Average Waiting Time:", stats["avg_waiting"])
            print("Average Turnaround Time:", stats["avg_turnaround"])

        return

    # ----------------------------
    # SINGLE ALGORITHM MODE
    # ----------------------------
    if args.algo == "fcfs":
        print("\n--- FCFS ---")
        result = fcfs(processes)

    elif args.algo == "sjf":
        print("\n--- SJF ---")
        result = sjf(processes)

    elif args.algo == "priority":
        print("\n--- PRIORITY ---")
        result = priority_scheduling(processes)

    elif args.algo == "rr":
        print("\n--- ROUND ROBIN ---")
        result = round_robin(processes, args.quantum)

    else:
        print("Invalid algorithm")
        return

    # ----------------------------
    # CLEAN OUTPUT
    # ----------------------------
    print_table(result)


if __name__ == "__main__":
    main()