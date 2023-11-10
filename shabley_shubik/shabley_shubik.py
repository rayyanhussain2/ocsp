
def priority(value, l, states):
    sum = 0
    for i in l:
        sum += i.get("Seats")
        if sum > value:
            i["Key Player"] += 1
            return

def worker(params):
    value, permutation, states = params
    priority(value, permutation, states)

def heapPermutation(a, size, value, states):
    if size == 1:
        worker((value, a, states))
        return

    jobs = []
    for i in range(size):
        new_permutation = a.copy()
        heapPermutation(new_permutation, size - 1, value, states)
        if size & 1:
            a[0], a[size - 1] = a[size - 1], a[0]
        else:
            a[i], a[size - 1] = a[size - 1], a[i]


def main_caller(states,value):
    import multiprocessing
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)
    heapPermutation(states, len(states), value, states)
    pool.close()