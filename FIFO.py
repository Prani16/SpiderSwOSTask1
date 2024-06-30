class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

def waittime(processes):
    total_waiting_time = 0
    for i in range(1, len(processes)):
        processes[i].waiting_time = processes[i-1].waiting_time + processes[i-1].burst_time
        total_waiting_time += processes[i].waiting_time
    return total_waiting_time / len(processes)

def turnaround_time(processes):
    total_turnaround_time = 0
    for process in processes:
        process.turnaround_time = process.waiting_time + process.burst_time
        total_turnaround_time += process.turnaround_time
    return total_turnaround_time / len(processes)

def main():
    # Process list
    pl = [Process(100, 16), Process(101, 18), Process(103, 7), Process(104, 3),Process(105, 6)]

    avg_waiting_time = waittime(pl)
    avg_turnaround_time = turnaround_time(pl)

    print("Process ID\tBurst Time\tWaiting Time\tTurnaround Time")
    for process in pl:
        print(f"{process.pid}\t\t{process.burst_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

if __name__ == "__main__":
    main()
