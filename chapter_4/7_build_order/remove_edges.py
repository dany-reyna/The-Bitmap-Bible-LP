class Project:
    def __init__(self, name):
        self.name = name
        self.incoming_edges = 0
        self.children = []
        self.map = {}

    def add_neighbor(self, node):
        if node.name not in self.map:
            self.children.append(node)
            self.map[node.name] = node
            node.incoming_edges += 1

    def __repr__(self):
        return self.name


class Graph:
    def __init__(self):
        self.nodes = []
        self.map = {}

    def get_or_create_node(self, name):
        if name not in self.map:
            node = Project(name)
            self.nodes.append(node)
            self.map[name] = node

        return self.map[name]

    def add_edge(self, start_name, end_name):
        start = self.get_or_create_node(start_name)
        end = self.get_or_create_node(end_name)
        start.add_neighbor(end)


def add_non_dependent(order_array, projects, offset):
    for p in projects:
        if p.incoming_edges == 0:
            order_array[offset] = p
            offset += 1
    return offset


def build_graph(projects, dependencies):
    graph = Graph()

    for p in projects:
        graph.get_or_create_node(p)

    for d in dependencies:
        graph.add_edge(d[0], d[1])
    return graph


def order_projects(projects):
    order_array = [None] * len(projects)

    end_of_list = add_non_dependent(order_array, projects, 0)

    to_be_processed = 0
    while to_be_processed < len(order_array):
        current = order_array[to_be_processed]

        # Dependency cycle
        if current is None:
            return None

        for c in current.children:
            c.incoming_edges -= 1

        end_of_list = add_non_dependent(order_array, current.children, end_of_list)
        to_be_processed += 1

    return order_array


if __name__ == '__main__':
    my_projects = ['a', 'b', 'c', 'd', 'e', 'f']
    my_deps = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

    g = build_graph(my_projects, my_deps)
    print(order_projects(g.nodes))
