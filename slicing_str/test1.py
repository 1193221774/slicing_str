import os


def get_filelist(dir):
    for home, dirs, files in os.walk(dir):
        for dir in dirs:
            print(home, "*", dir, "*", files)


if __name__ == "__main__":
    get_filelist('G:\\python')
