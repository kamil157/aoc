import re

with open('2022/inputs/day07.txt') as f:
    lines = f.read().split('\n')


class Directory:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.dirs = []
        self.parent = self

    def add_dir(self, name):
        new_dir = Directory(name)
        new_dir.set_parent(self)
        self.dirs.append(new_dir)
        return new_dir

    def set_parent(self, parent):
        self.parent = parent

    def get_dir(self, name):
        return [dir for dir in self.dirs if dir.name == name][0]

    def add_file(self, size):
        self.size += size

    def get_size(self):
        size = self.size
        for child in self.dirs:
            size += child.get_size()
        return size

    def __repr__(self):
        return f"{self.name, self.size, self.get_size(), self.dirs}"


def part1():
    dirs = []
    for i in range(len(lines)):
        line = lines[i]
        if line.startswith('$'):
            if match := re.match('\\$ cd (.+)', line):
                name = match[1]
                if name == '/':
                    root = Directory(name)
                    dirs.append(root)
                    current = root
                elif name == '..':
                    current = current.parent
                else:
                    new_directory = current.get_dir(name)
                    current = new_directory

            if line == "$ ls":
                try:
                    while not lines[i + 1].startswith('$'):
                        i += 1
                        line = lines[i]
                        if match := re.match('dir (.+)', line):
                            name = match[1]
                            dirs.append(current.add_dir(name))
                        elif match := re.match('(\\d+) .+', line):
                            size = int(match[1])
                            current.add_file(size)
                except IndexError:
                    pass
            i += 1

    sizes = [dir.get_size() for dir in dirs]

    # part1
    small = [size for size in sizes if size < 100000]
    print(sum(small))

    # part2
    total = 70000000
    required = 30000000
    free = total - root.get_size()
    missing = required - free

    for size in sorted(sizes):
        if size > missing:
            return size


print(part1())
