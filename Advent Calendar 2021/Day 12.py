# from functools import cache

with open('Day_12_Input.txt', "r") as f:
    myinput = (f.read().splitlines())

caves = {}
visited = []
paths = []
pathcur = ['start']
for i in myinput:
    [a, b] = i.split('-')
    if a not in caves:
        caves[a] = []
    if b not in caves:
        caves[b] = []
    caves[a].append(b)
    caves[b].append(a)

print(caves)


def pathpart1(graph, src, dst, visited):
    for neighbor in graph[src]:
        if neighbor.islower() and neighbor not in visited:
            visited.append(neighbor)
        if neighbor in visited and neighbor in pathcur:
            continue
        elif neighbor == dst:
            pathcur.append(neighbor)
            paths.append(pathcur.copy())
            pathcur.pop()
        else:
            pathcur.append(neighbor)
            pathpart1(graph, neighbor, dst, visited)
    pathcur.pop()


pathpart1(caves, 'start', 'end', visited)

print(len(paths))
#print(paths)
