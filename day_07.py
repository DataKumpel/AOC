from aoc_utility import get_puzzle_input


MAX_DISK_SPACE = 70_000_000
UPDATE_SIZE = 30_000_000


class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size


class Folder:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.parent: "Folder" = None
        self.subfolders: list["Folder"] = []
        self.files: list[File] = []
    
    def __repr__(self) -> str:
        return f"Folder[{self.name}, {self.size}]"

    def add_folder(self, folder: "Folder") -> None:
        folder.parent = self
        self.subfolders.append(folder)

    def add_file(self, file: File) -> None:
        self.files.append(file)

    def get_folder(self, foldername: str) -> "Folder":
        for folder in self.subfolders:
            if folder.name == foldername:
                return folder
    
    @property
    def size(self) -> int:
        s = 0
        for folder in self.subfolders:
            s += folder.size
        for file in self.files:
            s += file.size
        return s


def reconstruct_hierarchy(commands: list[str]) -> Folder:
    root = Folder("root")
    cwd = root

    for cmd in commands:
        if cmd.startswith("cd"):
            dest = cmd.split()[-1]
            if dest == "/":
                cwd = root
            elif dest == "..":
                cwd = cwd.parent
            else:
                cwd = cwd.get_folder(dest)
            continue

        if cmd.startswith("ls"):
            contents = cmd.split("\n")[1:]
            for content in contents:
                content = content.split()
                if content[0] == "dir":
                    cwd.add_folder(Folder(content[1]))
                else:
                    cwd.add_file(File(name=content[1], size=int(content[0])))
    
    return root


def find_folders_with_size(
        root: Folder, 
        max_size: int = 100_000,
    ) -> list[Folder]:
    folder_list = []
    for folder in root.subfolders:
        if folder.size <= max_size:
            folder_list.append(folder)
        folder_list.extend(find_folders_with_size(folder))
    return folder_list


def flatten_folders(root: Folder) -> list[Folder]:
    folder_list = []
    for folder in root.subfolders:
        folder_list.append(folder)
        folder_list.extend(flatten_folders(folder))
    return folder_list


def main():
    commands = get_puzzle_input(7).lstrip("$ ").split("\n$ ")
    root = reconstruct_hierarchy(commands)
    fit_folders = find_folders_with_size(root)

    sum_sizes = 0
    for folder in fit_folders:
        sum_sizes += folder.size
    
    print(f"{sum_sizes=}")

    #=== Part II ==============================================================

    space_to_free = UPDATE_SIZE - (MAX_DISK_SPACE - root.size)
    print(f"{space_to_free=}")
    folders = flatten_folders(root)
    print(folders)
    min_folder = root
    for folder in folders:
        if folder.size >= space_to_free and folder.size < min_folder.size:
            min_folder = folder
    
    print(f"{min_folder=}")


if __name__ == "__main__":
    main()

