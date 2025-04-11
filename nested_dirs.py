import os

def create_nested_dirs(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        raise Exception ("File already exists")


if __name__ == "__main__":
    dir_path = 'C:/Users/HP/Desktop/pathA/pathB/pathC'
    create_nested_dirs(dir_path)