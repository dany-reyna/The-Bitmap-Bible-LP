from enum import Enum


class Project:
    class State(Enum):
        BLANK = 0
        PARTIAL = 1
        COMPLETE = 2

    def __init__(self, name):
        self.name = name
        self.children = []
        self.map = {}
        self.state = Project.State.BLANK

    def add_neighbor(self, node):
        if node.name not in self.map:
            self.children.append(node)
            self.map[node.name] = node

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


def build_graph(projects, dependencies):
    graph = Graph()

    for p in projects:
        graph.get_or_create_node(p)

    for d in dependencies:
        graph.add_edge(d[0], d[1])
    return graph


def do_dfs(project, stack):
    if project.state == Project.State.PARTIAL:
        return False

    if project.state == Project.State.BLANK:
        project.state = Project.State.PARTIAL

        for c in project.children:
            if not do_dfs(c, stack):
                return False

        project.state = Project.State.COMPLETE
        stack.append(project)

    return True


def order_projects(projects):
    stack = []
    for p in projects:
        if p.state == Project.State.BLANK:
            if not do_dfs(p, stack):
                return None
    return stack


if __name__ == '__main__':
    my_projects = ['a', 'b', 'c', 'd', 'e', 'f']
    my_deps = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

    g = build_graph(my_projects, my_deps)
    print(order_projects(g.nodes))
