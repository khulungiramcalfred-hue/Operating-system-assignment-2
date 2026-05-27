def priority_scheduling(processes):
    processes = sorted(processes, key=lambda x: (x["arrival"], x["priority"]))

    time = 0
    completed = []
    ready = processes[:]

    while ready:
        available = [p for p in ready if p["arrival"] <= time]

        if not available:
            time += 1
            continue

        highest = min(available, key=lambda x: x["priority"])
        ready.remove(highest)

        start = time
        finish = time + highest["burst"]

        waiting = start - highest["arrival"]
        turnaround = finish - highest["arrival"]

        completed.append({
            "pid": highest["pid"],
            "start": start,
            "finish": finish,
            "waiting": waiting,
            "turnaround": turnaround
        })

        time = finish

    return completed