from collections import deque


def round_robin(processes, quantum=2):

    queue = deque()

    time = 0
    results = []

    remaining_processes = []

    # Copy processes and add remaining burst time
    for p in processes:
        process = p.copy()
        process["remaining"] = process["burst"]
        remaining_processes.append(process)

    # Sort by arrival time
    remaining_processes.sort(key=lambda x: x["arrival"])

    while remaining_processes or queue:

        # Add arrived processes to queue
        while remaining_processes and remaining_processes[0]["arrival"] <= time:
            queue.append(remaining_processes.pop(0))

        # If queue empty, move time forward
        if not queue:
            time += 1
            continue

        process = queue.popleft()

        start = time

        # Execute process for quantum or remaining time
        execution_time = min(quantum, process["remaining"])

        time += execution_time

        process["remaining"] -= execution_time

        finish = time

        results.append({
            "pid": process["pid"],
            "start": start,
            "finish": finish,
            "waiting": start - process["arrival"],
            "turnaround": finish - process["arrival"]
        })

        # Add newly arrived processes
        while remaining_processes and remaining_processes[0]["arrival"] <= time:
            queue.append(remaining_processes.pop(0))

        # Re-add process if not finished
        if process["remaining"] > 0:
            queue.append(process)

    return results