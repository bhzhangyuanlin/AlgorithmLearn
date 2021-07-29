from collections import deque

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
    def __init__(self, x, y, come_from):
        self.x = x
        self.y = y
        self.come_from = come_from
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.dirs = [None] * 4
        self.check_available_dirs()

    def check_available_dirs(self):
        if maze[self.x + 1][self.y] == 0:
            self.down = True
        else:
            self.down = False
        if maze[self.x][self.y + 1] == 0:
            self.right = True
        else:
            self.right = False
        if maze[self.x][self.y - 1] == 0:
            self.left = True
        else:
            self.left = False
        if maze[self.x - 1][self.y] == 0:
            self.up = True
        else:
            self.up = False
        self.set_dirs()

    def set_dirs(self):
        self.dirs = [None if not self.down else (self.x + 1, self.y),
                     None if not self.right else (self.x, self.y + 1),
                     None if not self.left else (self.x, self.y - 1),
                     None if not self.up else (self.x - 1, self.y)]


class Solution:
    def __init__(self):
        self.queue = deque()
        self.real_path = []
        self.path_choice = []

    def find_path(self, x0, y0, x1, y1):
        init_node = Node(x0, y0, -1)
        self.queue.append(init_node)
        while len(self.queue) > 0:
            cur_node = self.queue.popleft()
            self.path_choice.append(cur_node)
            if cur_node.x == x1 and cur_node.y == y1:
                temp_node = cur_node
                while temp_node.come_from != -1:
                    self.real_path.append(self.path_choice[temp_node.come_from])
                    temp_node = self.path_choice[temp_node.come_from]
                self.real_path.reverse()
                self.real_path.append(cur_node)
                for i in self.real_path:
                    print((i.x, i.y))
                break
            cur_node.check_available_dirs()
            maze[cur_node.x][cur_node.y] = 2
            for i in cur_node.dirs:
                if i:
                    self.queue.append(Node(i[0], i[1], len(self.path_choice) - 1))

        else:
            print("没有路")

            
if __name__ == '__main__':
    s = Solution()
    s.find_path(1, 1, 5, 7)
