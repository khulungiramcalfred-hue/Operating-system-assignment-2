def sjf(processes):
    processes = sorted(processes, key=lambda x: (x["arrival"], x["burst"]))

    time = 0
    completed = []
    ready = processes[:]

    while ready:
        available = [p for p in ready if p["arrival"] <= time]

        if not available:
            time += 1
            continue

        shortest = min(available, key=lambda x: x["burst"])
        ready.remove(shortest)

        start = time
        finish = time + shortest["burst"]

        waiting = start - shortest["arrival"]
        turnaround = finish - shortest["arrival"]

        completed.append({
            "pid": shortest["pid"],
            "start": start,
            "finish": finish,
            "waiting": waiting,
            "turnaround": turnaround
        })

        time = finish

    return completed