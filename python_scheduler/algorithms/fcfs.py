def fcfs(processes):
    processes = sorted(processes, key=lambda x: x["arrival"])

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