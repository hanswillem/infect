"""Replaces bytes in one file with bytes in another file."""

# how to use:
#
# REPLACE RANDOM CHUNK OF BYTES
# python infect.py kick.wav epilepticfit.csv -m 1 -c 45 -i 10 -f 5
# -m = mode 1
# -c = maximum lenght of the chunk of bytes (the actual chunk will be random each itteration)
# -i = amount of itterations
# -f = amount of files that will be exported
# 
# REPLACE RANDOM BYTES
# python infect.py kick.wav epilepticfit.csv -m 2 -r 1000 -f 5
# -m = mode 2
# -r = amount of random bytes to replace
# -f = amount of files that will be exported
#
# REPLACE EVERY N BYTES (works good for PNG's and MP4)
# python infect.py kick.wav epilepticfit.csv -m 3 -n 512
# -m = mode 3
# -n = replace every n bytes

import argparse
import random
import os

# ----------------------------- glitch functions -----------------------------

def main():
    def replaceRandomChunksOfBytes(c, n):
        c = min(100, c)
        for t in range(n):
            # get bytes
            chunk = random.randint(1, c) / 100
            l = int(chunk * len(fileBioList))
            pos = random.randint(0, len(fileBioList) - l)
            bioBytes = [fileBioList[pos + i] for i in range(l)]
            # replace bytes
            pos = random.randint(header_length, len(fileBaseList))
            maxLength = len(fileBaseList) - pos
            l = min(l, maxLength)
            fileResultList[pos:pos + l] = bioBytes

    def replaceRandomBytes(n):
        for i in range(n):
            pos = random.randint(header_length, len(fileBaseList) - header_length)
            fileResultList[pos] = random.choice(fileBioList)

    def replaceEveryNBytes(n):
        for i in range(len(fileBaseList)):
            if i > header_length and i % n == 0:
                fileResultList[i] = random.choice(fileBioList)

    def saveResult(n):
        f3_fileName, f3_extension = os.path.splitext(args.fileBase)
        if args.numFiles > 1:
            resultFilename = f3_fileName + "_glitched_" + str(n) + f3_extension
        else:
            resultFilename = f3_fileName + "_glitched" + f3_extension
        open(os.path.join("results", resultFilename), "wb").write(bytes(fileResultList))

# ----------------------------- arguments -----------------------------

    parser = argparse.ArgumentParser()
    parser.add_argument("fileBase", help = "The file you want to infect.", type = str)
    parser.add_argument("fileBio", help = "The file with biodata.", type = str)
    parser.add_argument("-r", "--randomBytes", default = 1, help = "Number of bytes to replace.", type = int)
    parser.add_argument("-n", "--everyNBytes", default = 512, help = "Modulo number of bytes to replace.", type = int)
    parser.add_argument("-c", "--chunk", default = 25, help = "An int between 0 and 100 that describes the size of the chunk of bytes in percentage", type = int)
    parser.add_argument("-f", "--numFiles", default = 1, help = "The amount of files that will be created.", type = int)
    parser.add_argument("-i", "--itteration", default = 1, help = "The amount of times the function will be repeated.", type = int)
    parser.add_argument("-m", "--mode", default = 1, help = "1 = Replace chunk of bytes. | 2 = Replace random bytes. | 3 = Replace every n byte.", type = int)
    args = parser.parse_args()

# ----------------------------- setup -----------------------------

    header_length = 1000

    if not os.path.exists("./results"):
        os.mkdir("./results")

    fileBaseList = list(open(args.fileBase, "rb").read())
    fileBioList = list(open(args.fileBio, "rb").read())
    fileResultList = list(open(args.fileBase, "rb").read())

# ----------------------------- GLITCH -----------------------------

    if args.mode == 1:
        print("Mode 1: replace chunks of bytes")
        for i in range(args.numFiles):
            replaceRandomChunksOfBytes(args.chunk, args.itteration)
            saveResult(i)
        print("finshed!")
    elif args.mode == 2:
        print("Mode 2: replace random bytes")
        for i in range(args.numFiles):
            replaceRandomBytes(args.randomBytes)
            saveResult(i)
        print("finshed!")
    elif args.mode == 3:
        print("Mode 3: replace every n byte")
        for i in range(args.numFiles):
            replaceEveryNBytes(args.everyNBytes)
            saveResult(i)
        print("finshed!")
    else:
        print("Mode can only be 1, 2 or 3!")
    
# ----------------------------- main -----------------------------

if __name__ == '__main__':
    main()
