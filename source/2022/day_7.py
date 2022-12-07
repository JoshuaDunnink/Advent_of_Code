import re
import collections


def navigation():
    with open("input/2022/day_7", "r") as file:
        return [line.strip("\n") for line in file.readlines()]


class Directory:
    def __init__(self, name: str):
        self.name = name
        self.content = {}
        self.size = 0

    def add(self, item):
        if not self.content.get(item.name):
            self.content.update({item.name: item})

    def get_size(self):
        self.size = 0
        for item in self.content.values():
            self.size += item.get_size()
        return self.size

    def get(self, value):
        return self.content.get(value)

    def get_sub_dirs(self):
        dirs = []
        for value in self.content.values():
            if type(value) == Directory:
                dirs.append(value)

        unpacked_dirs = []
        for dir in dirs:
            for value in dir.content.values():
                if type(value) == Directory:
                    unpacked_dirs.append(value)
                    unpacked_dirs.extend(value.get_sub_dirs())
        dirs.extend(unpacked_dirs)
        return dirs


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size


class Filesystem:
    def __init__(self):
        self.index = {}
        self.current_directory = []

    def determine_size(self):
        self.index.get("/").get_size()

    def add_dir(self, directory: Directory):
        current_directory = self.ls()
        if not current_directory.get(directory.name):
            current_directory.add(directory)

    def add_file(self, file: File):
        current_directory = self.ls()
        if not current_directory.content.get(file.name):
            current_directory.add(file)

    def cd(self, input):
        match input:
            case "/":
                self.current_directory = ["/"]
                if not self.ls():
                    self.index.update({input: Directory(input)})
            case "..":
                self.current_directory.pop()
            case _:
                self.current_directory.append(input)
                if not self.ls():
                    self.index.update({input: Directory(input)})

    def ls(self) -> Directory:
        directory = self.index
        for dir in self.current_directory:
            directory = directory.get(dir)
        return directory

    def get_dirs(self):
        dirs = []
        for value in self.index.values():
            if type(value) == Directory:
                dirs.extend(value.get_sub_dirs())
        return dirs


def compose_filesystem_from_input():
    filesystem = Filesystem()
    for line in navigation():
        decomposed_line = line.split(" ")
        if decomposed_line[0] == "$":
            if decomposed_line[1] == "cd":
                filesystem.cd(decomposed_line[2])
            elif decomposed_line[1] == "ls":
                pass
        elif decomposed_line[0] == "dir":
            filesystem.add_dir(Directory(name=decomposed_line[1]))
        elif re.match("\d", decomposed_line[0]):
            filesystem.add_file(
                File(name=decomposed_line[1], size=int(decomposed_line[0]))
            )
    filesystem.determine_size()
    return filesystem


def part_1(filesystem):
    directories = filesystem.get_dirs()

    combined_size = 0
    for dir in directories:
        if dir.size <= 100000:
            combined_size += dir.size

    print(combined_size)


filesystem = compose_filesystem_from_input()
part_1(filesystem)
