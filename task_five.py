import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_heap_tree(heap, index=0):
    if index >= len(heap):
        return None

    node = Node(heap[index])

    left_index = 2 * index + 1
    right_index = 2 * index + 2

    node.left = build_heap_tree(heap, left_index)
    node.right = build_heap_tree(heap, right_index)

    return node


def generate_colors(n):
    colors = []
    for i in range(n):
        intensity = int(50 + (205 * i / max(1, n - 1)))
        colors.append(f"#{intensity:02x}{intensity:02x}{255:02x}")
    return colors


def bfs_visualization(root):
    queue = deque([root])
    visited = []
    
    while queue:
        node = queue.popleft()
        visited.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    colors = generate_colors(len(visited))

    for i, node in enumerate(visited):
        node.color = colors[i]
        draw_tree(root)


def dfs_visualization(root):
    stack = [root]
    visited = []

    while stack:
        node = stack.pop()
        visited.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    colors = generate_colors(len(visited))

    for i, node in enumerate(visited):
        node.color = colors[i]
        draw_tree(root)


heap = [1, 3, 6, 5, 9, 8, 10]
root = build_heap_tree(heap)

# Обхід у ширину
bfs_visualization(root)

# Обхід у глибину
dfs_visualization(root)
