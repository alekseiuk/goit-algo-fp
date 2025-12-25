class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev 
            prev = current
            current = next_node
        self.head = prev


    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


def merge_sort(head: Node) -> Node:
    if head is None or head.next is None:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    right = slow.next
    slow.next = None

    left_sorted = merge_sort(head)
    right_sorted = merge_sort(right)

    return merge_sorted_lists(left_sorted, right_sorted)


def merge_sorted_lists(left: Node, right: Node) -> Node:
    if not left:
        return right
    if not right:
        return left

    if left.data <= right.data:
        left.next = merge_sorted_lists(left.next, right)
        return left
    else:
        right.next = merge_sorted_lists(left, right.next)
        return right



llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(1)
llist.insert_at_beginning(3)
llist.insert_at_beginning(5)

# Вставляємо вузли в кінець
llist.insert_at_end(7)
llist.insert_at_end(9)

print("Невідсортований список:")
llist.print_list()

print("Зворотний порядок:")
llist.reverse()
llist.print_list()

print("Відсортований список:")
llist.head = merge_sort(llist.head)
llist.print_list()

print("Злиття двох відсортованих списків:")
llist2 = LinkedList()
llist2.insert_at_beginning(2)
llist2.insert_at_beginning(4)
llist2.insert_at_beginning(6)
llist2.insert_at_end(8)
llist2.insert_at_end(10)

llist2.head = merge_sort(llist2.head)

merged_list = LinkedList()
merged_list.head = merge_sorted_lists(llist.head, llist2.head)
merged_list.print_list()