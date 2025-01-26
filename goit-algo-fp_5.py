"""
Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, яка візуалізує
обходи дерева: у глибину та в ширину.
Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0).
Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. Кожен вузол при його
відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.

👉🏻 Примітка. Використовуйте стек та чергу, НЕ рекурсію
"""
import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys
from collections import deque

from openpyxl.styles.builtins import title


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, highlight=None, interactive=False, title="Binary Tree Visualization"):
    """
    Візуалізація дерева. Якщо interactive=True, оновлює графік у інтерактивному режимі.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [highlight.get(node[0], node[1]['color']) for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.clf()  # Очищення попереднього графіка
    plt.title(title) # Встановлення заголовка
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=500, node_color=colors)

    if interactive:
        plt.pause(0.5)  # Коротка пауза для оновлення графіка
    else:
        plt.show()


def build_tree_from_heap(heap):
    if not heap:
        return None

    nodes = [Node(key) for key in heap]
    for i in range(len(heap)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(heap):
            nodes[i].left = nodes[left_index]

        if right_index < len(heap):
            nodes[i].right = nodes[right_index]

    return nodes[0]


def generate_colors(n):
    """Генерує градієнт кольорів від темного до світлого."""
    colors = []
    for i in range(n):
        hue = i / n
        lightness = 0.4 + 0.4 * (i / n)  # Від 40% до 80% яскравості
        rgb = colorsys.hls_to_rgb(hue, lightness, 1)
        colors.append(f'#{int(rgb[0] * 255):02x}{int(rgb[1] * 255):02x}{int(rgb[2] * 255):02x}')
    return colors


def dfs(tree_root):
    """Обхід в глибину з використанням стека."""
    if not tree_root:
        return

    plt.ion()  # Увімкнути інтерактивний режим
    stack = [tree_root]
    visited = []
    colors = generate_colors(len(binary_heap))
    highlight = {}

    step = 0
    while stack:
        node = stack.pop()
        if node:
            visited.append(node.val)
            highlight[node.id] = colors[step]
            step += 1
            draw_tree(tree_root, highlight, interactive=True, title="Binary Tree Visualization DFS")

            # Додаємо правий і лівий вузли в стек (правий додається першим, щоб лівий був на вершині)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    plt.ioff()  # Вимкнути інтерактивний режим
    plt.show()


def bfs(tree_root):
    """Обхід в ширину з використанням черги."""
    if not tree_root:
        return

    plt.ion()  # Увімкнути інтерактивний режим
    queue = deque([tree_root])
    visited = []
    colors = generate_colors(len(binary_heap))
    highlight = {}

    step = 0
    while queue:
        node = queue.popleft()
        if node:
            visited.append(node.val)
            highlight[node.id] = colors[step]
            step += 1
            draw_tree(tree_root, highlight, interactive=True, title="Binary Tree Visualization BFS")

            # Додаємо лівий і правий вузли в чергу
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    plt.ioff()  # Вимкнути інтерактивний режим
    plt.show()


# Приклад бінарної купи
binary_heap = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
heap_tree_root = build_tree_from_heap(binary_heap)

print("Обхід у глибину (DFS):")
dfs(heap_tree_root)

print("\nОбхід у ширину (BFS):")
bfs(heap_tree_root)

