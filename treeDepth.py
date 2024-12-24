class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = []
            if end not in self.graph_dict:
                self.graph_dict[end] = []
            self.graph_dict[start] = [end]
            self.graph_dict[end] = [start]
