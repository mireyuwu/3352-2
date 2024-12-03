import random
import math
import matplotlib.pyplot as plt
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self._min_value_node(node.right)
            node.key = min_node.key
            node.right = self._delete(node.right, min_node.key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            min_node = self._min_value_node(node.right)
            node.key = min_node.key
            node.right = self._delete(node.right, min_node.key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)

    def _balance(self, node):
        balance_factor = self._get_balance(node)
        if balance_factor > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance_factor < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _rotate_left(self, z):
        y = z.right
        z.right = y.left
        y.left = z
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, z):
        y = z.left
        z.left = y.right
        y.right = z
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def height(self):
        """Возвращает высоту дерева"""
        return self._get_height(self.root)

class RBNode:
    def __init__(self, key, color="red"):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None, color="black")
        self.root = self.NIL

    def insert(self, key):
        node = RBNode(key)
        node.left = self.NIL
        node.right = self.NIL
        self._insert(node)

    def _insert(self, node):
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if not parent:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        node.color = "red"
        self._fix_insert(node)

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    uncle.color = "black"
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    uncle.color = "black"
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._left_rotate(node.parent.parent)
        self.root.color = "black"

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def height(self):
        """Возвращает высоту красно-черного дерева"""
        return self._height(self.root)

    def _height(self, node):
        if node is None or node == self.NIL:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))


class BinarySearchTreeWithHeight(BinarySearchTree):
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def dfs_pre_order(self):
        """Pre-order обход (DFS): корень -> левый -> правый"""
        result = []
        self._dfs_pre_order(self.root, result)
        return result

    def _dfs_pre_order(self, node, result):
        if node:
            result.append(node.key)  # Добавляем узел
            self._dfs_pre_order(node.left, result)  # Обход левого поддерева
            self._dfs_pre_order(node.right, result)  # Обход правого поддерева

    def dfs_in_order(self):
        """In-order обход (DFS): левый -> корень -> правый"""
        result = []
        self._dfs_in_order(self.root, result)
        return result

    def _dfs_in_order(self, node, result):
        if node:
            self._dfs_in_order(node.left, result)  # Обход левого поддерева
            result.append(node.key)  # Добавляем узел
            self._dfs_in_order(node.right, result)  # Обход правого поддерева

    def dfs_post_order(self):
        """Post-order обход (DFS): левый -> правый -> корень"""
        result = []
        self._dfs_post_order(self.root, result)
        return result

    def _dfs_post_order(self, node, result):
        if node:
            self._dfs_post_order(node.left, result)  # Обход левого поддерева
            self._dfs_post_order(node.right, result)  # Обход правого поддерева
            result.append(node.key)  # Добавляем узел

    def bfs(self):
        """Обход в ширину (BFS): уровень за уровнем"""
        result = []
        if not self.root:
            return result

        queue = deque([self.root])  # Используем очередь
        while queue:
            node = queue.popleft()
            result.append(node.key)  # Добавляем узел
            if node.left:
                queue.append(node.left)  # Добавляем левое поддерево
            if node.right:
                queue.append(node.right)  # Добавляем правое поддерево
        return result


class AVLTreeWithHeight(AVLTree):
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if not node:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))


class RedBlackTreeWithHeight(RedBlackTree):
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if not node or node.key is None:  # Обработка NIL-узлов
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))


def experiment():
    num_keys = [1,10,20,30, 40, 50, 90,100,150, 200,250, 300,350, 400,450, 500,550,600,650,700,750, 800,850,900,950,1000, 1024]  # Количество ключей для эксперимента
    results = {
        "BST_Random": [],
        "AVL_Ordered": [],
        "RB_Ordered": []
    }

    for n in num_keys:
        # Случайные ключи для BST
        random_keys = random.sample(range(1, n * 10), n)
        bst_tree_random = BinarySearchTreeWithHeight()
        for key in random_keys:
            bst_tree_random.insert(key)
        results["BST_Random"].append((n, bst_tree_random.height()))

        # Упорядоченные ключи для AVL и RB
        ordered_keys = list(range(1, n + 1))

        # AVL Ordered
        avl_tree_ordered = AVLTreeWithHeight()
        for key in ordered_keys:
            avl_tree_ordered.insert(key)
        results["AVL_Ordered"].append((n, avl_tree_ordered.height()))

        # RB Ordered
        rb_tree_ordered = RedBlackTreeWithHeight()
        for key in ordered_keys:
            rb_tree_ordered.insert(key)
        results["RB_Ordered"].append((n, rb_tree_ordered.height()))

    return results


def plot_results(results):
    plt.figure(figsize=(10, 6))
    num_keys = [n for n, _ in results["BST_Random"]]

    # Построение высот для каждого типа дерева
    for tree_type, data in results.items():
        heights = [height for _, height in data]
        label = f"{tree_type.replace('_', ' ')} Tree"
        plt.plot(num_keys, heights, marker='o', label=label)

    # # Теоретические зависимости
    # x = range(10, max(num_keys) + 1, 10)
    # plt.plot(x, [math.log2(k) for k in x], linestyle="--", label="log2(n) (AVL/RB Теория)")
    # plt.plot(x, x, linestyle="--", label="n (BST Теория)")

    # Настройки графика
    plt.title('Высота деревьев поиска в зависимости от числа узлов')
    plt.xlabel('Количество узлов')
    plt.ylabel('Высота дерева')
    plt.legend()
    plt.grid(True)
    plt.show()

from collections import deque


class BinarySearchTreeWithTraversal(BinarySearchTreeWithHeight):
    def dfs(self):
        """Обход в глубину (DFS)"""
        result = []
        self._dfs(self.root, result)
        return result

    def _dfs(self, node, result):
        if node:
            result.append(node.key)  # Прямой порядок обхода (preorder)
            self._dfs(node.left, result)
            self._dfs(node.right, result)

    def bfs(self):
        """Обход в ширину (BFS)"""
        result = []
        if not self.root:
            return result

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


if __name__ == "__main__":
    results = experiment()
    bst = BinarySearchTreeWithTraversal()
    #keys = [71, 34, 12, 6, 23, 49, 11, 92, 54, 1]
    #keys = [45, 3, 88, 17, 62, 94, 29, 56, 81, 12]
    keys = [79, 23, 90, 69, 85, 10, 4, 85, 61, 83]
    for key in keys:
        bst.insert(key)
    print("DFS Pre-order:", bst.dfs_pre_order())
    print("DFS In-order:", bst.dfs_in_order())
    print("DFS Post-order:", bst.dfs_post_order())
    print("BFS:", bst.bfs())

    # Вывод результатов
    for tree_type, data in results.items():
        print(f"\n{tree_type} Tree:")
        for n, height in data:
            print(f"Количество ключей: {n}, Высота дерева: {height}")

    # Построение графиков
    plot_results(results)



