def calculate_average(results):
    total_waiting = sum(r["waiting"] for r in results)
    total_turnaround = sum(r["turnaround"] for r in results)

    n = len(results)

    return {
        "avg_waiting": total_waiting / n,
        "avg_turnaround": total_turnaround / n
    }


def compare_algorithms(fcfs, sjf, rr, priority):
    return {
        "FCFS": calculate_average(fcfs),
        "SJF": calculate_average(sjf),
        "RR": rr,  # RR is different format (we improve later)
        "PRIORITY": calculate_average(priority)
    }