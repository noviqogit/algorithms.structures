n, m, q = map(int, input().split())

# first value in every center uses to count resets
centres = {i: [1 for _ in range(m + 1)] for i in range(1, n + 1)}

active_servers = {i: m for i in range(1, n + 1)}

metrics = {i: m for i in range(1, n + 1)}


def reset(center):
    i = int(center)
    resets = centres[i][0]
    centres[i] = [1 for _ in range(m + 1)]
    centres[i][0] += resets
    active_servers[i] = m
    metrics[i] = centres[i][0] * m


def disable(center, server):
    i, j = int(center), int(server)
    if centres[i][j]:
        centres[i][j] = 0
        active_servers[i] -= 1
        metrics[i] = centres[i][0] * active_servers[i]


def getmax():
    pairs = sorted(metrics.items(), key=lambda x: (x[1], x[0]))
    i, j = pairs[-1]
    to_check = pairs[::-1]
    for _i, _j in to_check:
        if _j < j:
            break
        i = _i
    print(i)


def getmin():
    pairs = sorted(metrics.items(), key=lambda x: (x[1], x[0]))
    print(pairs[0][0])


events = {
    'RESET': reset,
    'DISABLE': disable,
    'GETMAX': getmax,
    'GETMIN': getmin
}

for _ in range(q):
    event = input().split()
    func = events[event[0]]
    args = event[1:]
    func(*args) if args else func()
