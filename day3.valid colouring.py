    
graph = {
    'A':['B','C','D'],
    'B':['A','C'],
    'C':['A','B','D'],
    'D':['A','C']
}

colors = ['Red', 'Green', 'Blue']
solution = {}

def is_safe(node, color):
    for neighbor in graph[node]:
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True

def solve(index=0):
    if index == len(graph):
        return True
    node = list(graph.keys())[index]
    for color in colors:
        if is_safe(node, color):
            solution[node] = color
            if solve(index + 1):
                return True
            solution.pop(node)
    return False

if solve():
    print("Valid Coloring:")
    for node, color in solution.items():
        print(node, "->", color)
else:
    print("No valid coloring found")
