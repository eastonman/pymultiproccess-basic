#!/usr/bin/python3

import multiprocessing


def worker():
    a = []
    while True:
        i = 1
        a.append(i)


for i in range(12):
    p = multiprocessing.Process(target=worker)
    p.start()
p.join()
print("Exit")
