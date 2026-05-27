import matplotlib.pyplot as plt


def plot_comparison(data):
    algorithms = list(data.keys())
    waiting = [data[a]["avg_waiting"] for a in algorithms]
    turnaround = [data[a]["avg_turnaround"] for a in algorithms]

    # ---------------------------
    # WAITING TIME GRAPH
    # ---------------------------
    plt.figure()
    plt.bar(algorithms, waiting)
    plt.title("Average Waiting Time Comparison")
    plt.xlabel("Algorithms")
    plt.ylabel("Time")
    plt.show()

    # ---------------------------
    # TURNAROUND TIME GRAPH
    # ---------------------------
    plt.figure()
    plt.bar(algorithms, turnaround)
    plt.title("Average Turnaround Time Comparison")
    plt.xlabel("Algorithms")
    plt.ylabel("Time")
    plt.show()