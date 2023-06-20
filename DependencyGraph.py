import copy

class DependencyGraph:
    def __init__(self):
        self.graph = {}

    def add_dependency(self, item, depends_on):
        if item not in self.graph:
            self.graph[item] = set()
        if depends_on:
            self.graph[item].update(depends_on)

    def remove_dependency(self, item):
        if item in self.graph:
            del self.graph[item]
        for depends in self.graph.values():
            depends.discard(item)

    def get_dependencies(self, item):
        current_dependencies = copy.deepcopy(self.graph[item])       
        dependencies = set(current_dependencies)
        while current_dependencies:
            cur_dependent = current_dependencies.pop()
            dependencies.update(self.graph[cur_dependent])
            current_dependencies.update(self.graph[cur_dependent])
        return dependencies

    def get_dependents(self, item):
        dependents = set()
        items = {item}
        while items:
            cur_item = items.pop()
            for key, depends in self.graph.items():
                if cur_item in depends:
                    dependents.add(key)
                    items.add(key)
        return dependents
    
dependencyGraph = DependencyGraph()

if __name__ == "__main__":
    # Example usage:
    graph = DependencyGraph()

    graph.add_dependency('A', ['B', 'C'])
    graph.add_dependency('B', ['D'])
    graph.add_dependency('C', ['D', 'E'])
    graph.add_dependency('D', ['E'])
    graph.add_dependency('E', [])

    print(graph.get_dependencies('A'))  # Output: {'B', 'C', 'D','E'}
    print(graph.get_dependents('D'))  # Output: ['A', 'B', 'C']