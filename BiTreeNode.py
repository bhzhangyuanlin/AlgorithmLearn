class BiNode:
    def __init__(self, val):
        self.value = val
        self.l_child = None
        self.r_child = None
        self.parent = None


class BiSearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node, val):
        if not self.root:
            self.root = BiNode(val)
            return

        if not node:
            node = BiNode(val)
            return node
        elif val < node.value:
            node.l_child = self.insert(node.l_child, val)
            node.l_child.parent = node
            return node

        elif val > node.value:
            node.r_child = self.insert(node.r_child, val)
            node.r_child.parent = node
            return node

    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = BiNode(val)
        else:
            while True:
                if val < p.value:
                    if not p.l_child:
                        p.l_child = BiNode(val)
                        p.l_child.parent = p
                        break
                    else:
                        p = p.l_child
                elif val > p.value:
                    if not p.r_child:
                        p.r_child = BiNode(val)
                        p.r_child.parent = p
                        break
                    else:
                        p = p.r_child

    def search(self, node, val):
        if self.root is None:
            return None
        else:
            if node is None:
                return None
            else:
                if node.value < val:
                    return self.search(node.r_child, val)
                elif node.value > val:
                    return self.search(node.l_child, val)
                else:
                    return node

    def search_no_rec(self, val):
        if self.root is None:
            return None
        else:
            node = self.root
            while True:
                if node is None:
                    return None
                elif val > node.value:
                    node = node.r_child
                elif val < node.value:
                    node = node.l_child
                else:
                    return node

    def delete(self, root, val):
        node = self.search(root, val)
        while node:
            if root.value == val:
                root_flag = True
            else:
                root_flag = False
            if not node.l_child and not node.r_child:
                if root_flag:
                    self.root = None
                    return
                if node.parent.l_child == node:
                    node.parent.l_child = None
                    node.parent = None
                else:
                    node.parent.r_child = None
                    node.parent = None
            elif node.l_child and node.r_child is None:
                if root_flag:
                    root.root = node.l_child
                    node.l_child = None
                    node.l_child.parent = None

                if node.parent.l_child == node:
                    node.parent.l_child = node.l_child
                    node.l_child.parent = node.parent
                else:
                    node.parent.r_child = node.l_child
                    node.l_child.parent = node.parent
            elif node.l_child is None and node.r_child:
                if root_flag:
                    root.root = node.r_child
                    node.r_child = None
                    node.r_child.parent = None

                if node.parent.l_child == node:
                    node.parent.l_child = node.r_child
                    node.r_child.parent = node.parent
                else:
                    node.parent.r_child = node.r_child
                    node.r_child.parent = node.parent
            else:
                if root_flag:
                    self.root = node.r_child
                    node.r_child.l_child = node.l_child
                    node.l_child.parent = node.r_child
                    return

                min_rchild_node = node.r_child
                while True:
                    if min_rchild_node is None:
                         break
                    else:
                        min_rchild_node = min_rchild_node.l_child

                min_rchild_node.parent.l_child = min_rchild_node.r_child
                min_rchild_node.r_child.parent = min_rchild_node.parent

                node.value = min_rchild_node.value
            return
        raise ValueError

    def pre_order(self, root):
        if root:
            print(root.value, end=', ')
            self.pre_order(root.l_child)
            self.pre_order(root.r_child)

    def in_order(self, root):
        if root:
            self.in_order(root.l_child)
            print(root.value, end=', ')
            self.in_order(root.r_child)

    def post_order(self, root):
        if root:
            self.post_order(root.l_child)
            self.post_order(root.r_child)
            print(root.value, end=', ')


if __name__ == '__main__':
    bst = BiSearchTree()
    li = [5, 7, 4, 9]
    for i in li:
        bst.insert(bst.root, i)
    # bst.pre_order(bst.root)
    # print('\n')
    # bst.in_order(bst.root)
    # print('\n')
    # bst.post_order(bst.root)
    # print(bst.search(bst.root, 6))
    # print(bst.search(bst.root, 11))
    # print(bst.search_no_rec(6))
    # print(bst.search_no_rec(11))
    bst.in_order(bst.root)
    bst.delete(bst.root, 5)
    print('\n')
    # bst.insert(bst.root, 6)
    bst.in_order(bst.root)
