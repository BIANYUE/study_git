# -*- coding: utf-8 -*-
import os


def main():
    os.remove("../data.txt")
    for pyname in os.listdir("../process"):
        os.system(f"python ./process/{pyname}")


if __name__ == '__main__':
    main()
