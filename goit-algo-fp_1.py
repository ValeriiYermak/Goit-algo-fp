"""
Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку необхідно:
написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
"""

import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next

            if not sorted_head or sorted_head.data >= current.data:
                current.next = sorted_head
                sorted_head = current
            else:
                search = sorted_head
                while search.next and search.next.data < current.data:
                    search = search.next
                current.next = search.next
                search.next = current

            current = next_node

        self.head = sorted_head


def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    return dummy.next


def create_random_list(size):
    """Створює список з випадковими числами заданого розміру"""
    llist = LinkedList()
    for _ in range(size):
        llist.append(random.randint(-1, 101))
    return llist


if __name__ == "__main__":
    # Створення першого випадкового списку
    size1 = 8  # Розмір першого списку
    llist1 = create_random_list(size1)
    print(f"Перший список (розмір {size1}):")
    llist1.print_list()

    # Сортування першого списку
    llist1.insertion_sort()
    print("Відсортований перший список:")
    llist1.print_list()

    # Створення другого випадкового списку
    size2 = 6  # Розмір другого списку
    llist2 = create_random_list(size2)
    print(f"\nДругий список (розмір {size2}):")
    llist2.print_list()

    # Сортування другого списку
    llist2.insertion_sort()
    print("Відсортований другий список:")
    llist2.print_list()

    # Об'єднання відсортованих списків
    merged_head = merge_sorted_lists(llist1.head, llist2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head

    print("\nОб'єднаний відсортований список:")
    merged_list.print_list()

    # Демонстрація реверсування
    print("\nДемонстрація реверсування на першому списку:")
    print("До реверсування:")
    llist1.print_list()
    llist1.reverse()
    print("Після реверсування:")
    llist1.print_list()
