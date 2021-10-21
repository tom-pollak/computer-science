class Castle:
    """Castle node in map"""

    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.castles = {}
        self.straight_line_dist = {}

    def generate_arcs(self, graph):
        for i, arc in enumerate(graph[self][0]):
            if arc in [0, None]:
                continue
            castle = list(graph)[i]
            self.castles[castle] = arc

        # self.castles = {
        #     k: v for k, v in sorted(self.castles.items(), key=lambda x: x[1])
        # }

    def generate_heuristics(self, heuristic):
        for i, dist in enumerate(heuristic[self]):
            castle = list(heuristic)[i]
            self.straight_line_dist[castle] = dist / 5

    def bfs(self, goal, queue=None, visited=None, dist_from_home=0):
        print(self.name, dist_from_home)
        best_dist = None
        if queue is None:
            queue = []
        if visited is None:
            visited = []
        visited.append(self)

        while True:
            if self.name == goal:
                return dist_from_home

            for connected_castle, arc in zip(self.castles, self.castles.values()):
                if connected_castle in visited:
                    continue

                rel_height = connected_castle.height - self.height
                if rel_height < 0:
                    rel_height = 0
                time_to_walk = (dist_from_home + arc) / 5 + rel_height / 600

                try:
                    c_index = [c[0] for c in queue].index(connected_castle)
                except ValueError:
                    queue.append([connected_castle, time_to_walk])
                    continue
                # queue[c_index][1] = min(queue[c_index][1], time_to_walk)
                queue[c_index][1] = min(
                    queue[c_index][1] + self.straight_line_dist[connected_castle],
                    time_to_walk + self.straight_line_dist[self],
                )
            if len(queue) == 0:
                return best_dist

            queue.sort(key=lambda x: x[1] + x[0] + self.straight_line_dist)
            next_castle, arc = queue.pop(0)
            dist = next_castle.bfs(goal, queue, visited, arc)

            if dist is None:
                pass
            elif best_dist is None or dist < best_dist:
                best_dist = dist
        return best_dist


heuristic = {
    "A": [0, 3, 3, 3, 7, 7, 11, 11, 15, 15],
    "B": [3, 0, 7, 3, 7, 3, 7, 11, 11, 15],
    "C": [3, 7, 0, 3, 3, 11, 15, 7, 15, 15],
    "D": [3, 3, 3, 0, 3, 7, 7, 7, 15, 15],
    "E": [7, 7, 3, 3, 0, 11, 7, 3, 11, 11],
    "F": [7, 3, 11, 7, 11, 0, 3, 7, 3, 7],
    "G": [11, 7, 15, 7, 7, 3, 3, 3, 3],
    "H": [11, 11, 7, 7, 3, 7, 3, 0, 7, 3],
    "I": [15, 11, 15, 11, 7, 3, 3, 7, 0, 3],
    "J": [15, 15, 15, 15, 11, 7, 3, 3, 3, 0],
}

graph = {
    "A": [[0, 5, 5, 5, None, None, None, None, None, None], 0],
    "B": [[5, 0, None, None, None, 5, None, None, None, None], 200],
    "C": [[5, None, 0, None, 5, None, None, None, None, None], 600],
    "D": [[5, None, None, 0, 5, 10, None, None, None, None], 100],
    "E": [[None, None, 5, 5, 0, None, 10, 5, None, None], 300],
    "F": [[None, 5, None, 10, None, 0, None, None, 5, None], 300],
    "G": [[None, None, None, None, 10, None, 0, 5, None, 5], 100],
    "H": [[None, None, None, None, 5, None, 5, 0, None, 5], 500],
    "I": [[None, None, None, None, None, 5, None, None, 0, 5], 400],
    "J": [[None, None, None, None, None, None, 5, 5, 5, 0], 500],
}

castles = []

for castle, height in zip(list(graph.keys()), [x for _, x in list(graph.values())]):
    new_castle = Castle(castle, height)
    castles.append(new_castle)

graph = {k: v for k, v in zip(castles, graph.values())}
heuristic = {k: v for k, v in zip(castles, heuristic.values())}

for castle in graph:
    castle.generate_arcs(graph)
    castle.generate_heuristics(heuristic)


A = list(graph)[0]
print(A.bfs("J"))
