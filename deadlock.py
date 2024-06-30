def is_safe(processes, avail, max_matrix, alloc):
    num_processes = len(processes)
    num_resources = len(avail)

    work = avail[:]
    finish = [False] * num_processes

    safe_sequence = []

    while len(safe_sequence) < num_processes:
        found = False
        for i in range(num_processes):
            if not finish[i]:
                exec_possible = True
                for j in range(num_resources):
                    if max_matrix[i][j] - alloc[i][j] > work[j]:
                        exec_possible = False
                        break
                
                if exec_possible:
                    for k in range(num_resources):
                        work[k] += alloc[i][k]
                    safe_sequence.append(processes[i])
                    finish[i] = True
                    found = True

        if not found:
            print("System is not in a safe state!")
            return False, []

    print("System is in a safe state. Safe sequence is:", safe_sequence)
    return True, safe_sequence

def main():
    processes = [0, 1, 2, 3, 4]
    avail = [3, 3, 2] 
    max_matrix = [
        [7, 9, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 4, 3]
    ]  # Maximum demand of each process
    alloc = [
        [0, 3, 0],
        [2, 1, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]  # Currently allocated resources to each process

    is_safe(processes, avail, max_matrix, alloc)

if __name__ == "__main__":
    main()
