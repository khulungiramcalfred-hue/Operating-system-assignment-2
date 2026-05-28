def calculate_average(results):

    total_waiting = 0
    total_turnaround = 0

    for r in results:
        total_waiting += r["waiting"]
        total_turnaround += r["turnaround"]

    n = len(results)

    return {
        "avg_waiting": round(total_waiting / n, 2),
        "avg_turnaround": round(total_turnaround / n, 2)
    }


def compare_algorithms(fcfs_result,
                       sjf_result,
                       rr_result,
                       priority_result):

    comparison = {
        "FCFS": calculate_average(fcfs_result),
        "SJF": calculate_average(sjf_result),
        "RR": calculate_average(rr_result),
        "PRIORITY": calculate_average(priority_result)
    }

    return comparison