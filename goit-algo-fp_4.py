import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Колір вузла для візуалізації
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Рекурсивна функція для побудови зв’язків між вузлами та їх позиціювання у просторі.
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Додаємо вузол до графа
        if node.left:
            graph.add_edge(node.id, node.left.id) # Додаємо ребро до лівого нащадка
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id) # Додаємо ребро до правого нащадка
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    """
    Функція для візуалізації дерева на основі його кореневого вузла.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Мітки для вузлів

    plt.figure(figsize=(8, 5))
    plt.title("The tree of binary heap (maximum/minimum)")
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=500, node_color=colors)
    plt.show()


def build_tree_from_heap(heap):
    """
    Функція для побудови дерева із бінарної купи.
    Аргумент:
        heap (list): Бінарна купа у вигляді списку.
    Повертає:
        Node: Кореневий вузол дерева.
    """
    if not heap:
        return None

    # Створення списку вузлів із значень купи
    nodes = [Node(key) for key in heap]

    # Зв'язуємо вузли відповідно до структури бінарної купи
    for i in range(len(heap)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(heap):
            nodes[i].left = nodes[left_index]

        if right_index < len(heap):
            nodes[i].right = nodes[right_index]

    return nodes[0]  # Повертаємо кореневий вузол дерева


# Приклад бінарної купи
binary_heap = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # Масив, що представляє бінарну купу
binary_heap2= list(reversed(binary_heap)) # Створюємо зворотний список
print(f' The values of the binary heap_maximum : {binary_heap}') # Показуємо значення бінарної купи (binary_heap)
print(f' The values of the binary heap_minimum: {binary_heap2}') # Показуємо значення бінарної купи (binary_heap)

# Побудова дерева
heap_tree_root_max = build_tree_from_heap(binary_heap) # Побудова дерева з купи
heap_tree_root_min = build_tree_from_heap(binary_heap2) # Побудова дерева з купи

# Візуалізація дерева
draw_tree(heap_tree_root_max)
draw_tree(heap_tree_root_min)