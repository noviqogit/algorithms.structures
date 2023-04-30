n, m, q = map(int, input().split())

servers = {i: [1 for _ in range(m)] for i in range(1, n + 1)}

resets = {i: 1 for i in range(1, n + 1)}

active_servers = {i: m for i in range(1, n + 1)}

metrics = {i: m for i in range(1, n + 1)}


def reset(center):
    i = int(center)
    resets[i] += 1
    active_servers[i] = m
    servers[i] = [1 for _ in range(m)]
    metrics[i] = resets[i] * active_servers[i]


def disable(center, server):
    i, j = int(center), int(server) - 1
    if servers[i][j]:
        servers[i][j] = 0
        active_servers[i] -= 1
        metrics[i] = resets[i] * active_servers[i]


def getmax():
    server, value = 1, 0
    for i, metric in metrics.items():
        if metric > value:
            server, value = i, metric
    print(server)


def getmin():
    server, value = 1, float('inf')
    for i, metric in metrics.items():
        if metric == 0:
            server = i
            break
        if metric < value:
            server, value = i, metric
    print(server)


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
