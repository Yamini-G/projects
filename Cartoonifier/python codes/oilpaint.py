import cv2
from glob import glob
from sys import argv
from matplotlib import pyplot as plt
import numpy as np

# BLF BiLateral Filter


def main(files):
    for PATH in glob(files):
        inputimg = cv2.imread(PATH, 1)
        rgbimg = cv2.cvtColor(inputimg, cv2.COLOR_BGR2RGB)
        temp = cv2.bilateralFilter(rgbimg, 9, 7, 9)

        for i in range(8):
            temp = cv2.bilateralFilter(temp, 9, 30, 15)

        bgrimg = cv2.cvtColor(temp, cv2.COLOR_RGB2BGR)
        path, ftybe = PATH.split('.')
        newPath = path + "Oil-filter" + '.' + ftybe
        print(newPath)
        cv2.imwrite(newPath, bgrimg)


if __name__ == "__main__":
    main(argv[1])