import os

def create_multiple_dirs(*args):
    for dir in args:
        if not os.path.exists(dir):
            os.makedirs(dir)
        else:
            # raise Exception("Directories already exists!")
            os.rmdir(dir)


if __name__ == '__main__':
    dir_path1 = 'C:/Users/HP/Desktop/pathA'
    dir_path2 = 'C:/Users/HP/Desktop/pathB'
    dir_path3 = 'C:/Users/HP/Desktop/pathC'

    create_multiple_dirs(dir_path1, dir_path2, dir_path3)