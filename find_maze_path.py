maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Node:
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.dirs = []
        self.check_dirs()

    def check_dirs(self):
        if maze[self.x - 1][self.y] == 0:
            self.up = True
        else:
            self.up = False
        if maze[self.x + 1][self.y] == 0:
            self.down = True
        else:
            self.down = False
        if maze[self.x][self.y - 1] == 0:
            self.left = True
        else:
            self.left = False
        if maze[self.x][self.y + 1] == 0:
            self.right = True
        else:
            self.right = False
        self.make_dirs_list()

    def make_dirs_list(self):
        self.dirs = [
            (self.x - 1, self.y) if self.up else None,
            (self.x + 1, self.y) if self.down else None,
            (self.x, self.y - 1) if self.left else None,
            (self.x, self.y + 1) if self.right else None
        ]

def maze_path(x0, y0, x1, y1):
    stack = []
    init_node = Node(x0, y0)
    stack.append(init_node)
    while len(stack) > 0:
        cur_node = stack[-1]
        cur_node.check_dirs()
        if cur_node.x == x1 and cur_node.y == y1:
            for i in stack:
                print((i.x, i.y))
            return 0
        else:
            for i in cur_node.dirs:
                if i:
                    next_node = Node(i[0], i[1])
                    stack.append(next_node)
                    maze[cur_node.x][cur_node.y] = 2
                    break
            else:
                maze[cur_node.x][cur_node.y] = 2
                stack.pop()
    print("无解")


if __name__ == '__main__':
    maze_path(1, 1, 8, 8)
