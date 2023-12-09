graph1 = {'A': {'B', 'C'},
          'B': {'A', 'D', 'E'},
          'C': {'A', 'F'},
          'D': {'B'},
          'E': {'B', 'F'},
          'F': {'C', 'E'}
          }
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited

visited = dfs(graph1, 'A', [])
print(visited)
