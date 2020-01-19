from collections import deque
from lib.graph import create_graph


def search(start, end):
    if start == end:
        return True

    queue = deque()

    start.visited = True
    queue.append(start)

    while queue:
        node = queue.popleft()
        node.visited = True
        for n in node.adjacent:
            if not n.visited:
                if n == end:
                    return True
                else:
                    n.visited = True
                    queue.append(n)
    return False


if __name__ == '__main__':
    g = create_graph()
    print(search(g.nodes[2], g.nodes[2]))
