class AVLNode:
    def __init__(self, val):
        self.value = val
        self.l_child = None
        self.r_child = None
        self.parent = None
        self.balance_factor = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, node, val):
        if self.root:
            if node:
                if val > node.value:
                    node.r_child = self.insert(node.r_child, val)
                    node.r_child.parent = node
                    return node
                elif val < node.value:
                    node.l_child = self.insert(node.l_child, val)
                    node.l_child.parent = node
                    return node
            else:
                node = AVLNode(val)
                return node
        else:
            self.root = AVLNode(val)

    def rotate_left(self, node1, node2):  # node2 原来是 node1 的父节点
        if node1.l_child:
            node2.r_child = node1.l_child
            node1.l_child.parent = node2
        node1.l_child = node2
        node2.parent = node1

        node1.balance_factor = 0
        node2.balance_factor = 0

        return node1

    def rotate_right(self, node1, node2):  # node2 原来是 node1 的父节点
        # node1.parent = node2.parent
        if node1.r_child:
            node2.l_child = node1.r_child
            node1.r_child.parent = node2
        node2.parent = node1
        node1.r_child = node2

        node1.balance_factor = 0
        node2.balance_factor = 0

        return node1

    def rotate_right_left(self, p, c):
        g = c.l_child

        if g.r_child:
            c.l_child = g.r_child
            g.r_child.parent = c

        g.r_child = c
        c.parent = g
        p.r_child = g
        g.parent = p

        if g.l_child:
            p.r_child = g.l_child
            g.l_child.parent = p

        g.l_child = p
        p.parent = g
        if g.balance_factor == -1:
            p.balance_factor = 0
            c.balance_factor = 1
            g.balance_factor = -1
        elif g.balance_factor == 1:
            c.balance_factor = 0
            p.balance_factor = -1
            g.balance_factor = 1
        else:
            g.balance_factor = 0
            p.balance_factor = 0
            c.balance_factor = 0

    def rotate_left_right(self, p, c):
        g = c.r_child

        if g.l_child:
            c.r_child = g.l_child
            g.l_child.parent = c

        g.l_child = c
        c.parent = g
        p.l_child = g
        g.parent = p

        if g.r_child:
            p.l_child = g.r_child
            g.r_child.parent = p

        g.r_child = p
        p.parent = g
        if g.balance_factor == -1:
            p.balance_factor = 1
            c.balance_factor = 0
            g.balance_factor = -1
        elif g.balance_factor == 1:
            c.balance_factor = -1
            p.balance_factor = 0
            g.balance_factor = 1
        else:
            g.balance_factor = 0
            p.balance_factor = 0
            c.balance_factor = 0

    def in_order(self, node):
        if node:
            self.in_order(node.l_child)
            print(node.value, end=', ')
            self.in_order(node.r_child)


if __name__ == '__main__':
    avl = AVLTree()
    for i in [7, 5, 9, 1, 4, 3, 6, 8, 2]:
        avl.insert(avl.root, i)
    avl.in_order(avl.root)
