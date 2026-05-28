def sjf(processes):

    processes = sorted(processes, key=lambda x: (x["arrival"], x["burst"]))

    time = 0
    results = []

    completed = []

    while len(completed) < len(processes):

        available = []

        for p in processes:
            if p not in completed and p["arrival"] <= time:
                available.append(p)

        if not available:
            time += 1
            continue

        process = min(available, key=lambda x: x["burst"])

        start = time
        finish = start + process["burst"]

        waiting = start - process["arrival"]
        turnaround = finish - process["arrival"]

        results.append({
            "pid": process["pid"],
            "start": start,
            "finish": finish,
            "waiting": waiting,
            "turnaround": turnaround
        })

        time = finish
        completed.append(process)

    return results