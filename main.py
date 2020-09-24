#!/usr/bin/python3

import multiprocessing


def worker():
    while True:
        pass


for i in range(12):
    p = multiprocessing.Process(target=worker)
    p.start()

p.join()

print("Main processing exit")
