# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:13:11 2019
Ren Liuhao
REAR
Reversal Distance
November 15, 2019

Goal:
Calculate the reversal distance between each permutation pair.
@author: renli
# mutation from both sides
"""

# Reversal Distance
# =================
#
# A reversal of a permutation creates a new permutation by inverting some
# interval of the permutation; (5,2,3,1,4), (5,3,4,1,2), and (4,1,2,3,5) are
# all reversals of (5,3,2,1,4). The reversal distance between two permutations
# π and σ, written drev(π,σ), is the minimum number of reversals required to
# transform π into σ (this assumes that π and σ have the same length).
#
# Given: A collection of at most 5 pairs of permutations, all of which have
# length 10.
#
# Return: The reversal distance between each permutation pair.
#
# Sample Dataset
# --------------
# 1 2 3 4 5 6 7 8 9 10
# 3 1 5 2 7 4 9 6 10 8
#
# 3 10 8 2 5 4 7 1 6 9
# 5 2 3 1 7 4 10 8 6 9
#
# 8 6 7 9 4 1 3 10 2 5
# 8 2 7 6 9 1 5 3 10 4
#
# 3 9 10 4 1 8 6 7 5 2
# 2 9 8 5 1 7 3 4 6 10
#
# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10
#
# Sample Output
# -------------
# 9 4 5 7 0


def cmp(a, b):
    for i in a:
        if i in b:
            # print(i)
            return True
    else:
        return False


def rd(i):
    a = set()
    a.add(i[0])
    b = set()
    b.add(i[1])
    # print(a,b)
    c = 0
    while not cmp(a, b):
        c += 1
        if c == 9:
            return 9
        if c % 2 == 0:
            mut(a)
        else:
            mut(b)
    return c


def reversal(p):
    for i in range(len(p)):
        for j in range(i + 2, len(p) + 1):
            yield p[:i]+p[i:j][::-1]+p[j:]


def mut(x):
    tempdic = set()
    for p in x:
        for temp in reversal(p):
            tempdic.add(temp)
    x.update(tempdic)


def input_(file):
    global data3
    if file == '':
        f = open(r'C:\Users\renli\！！think jupyter\rosalind_rear (5).txt', "rt")
    else:
        f = open(file, 'rt')
    exec('')
    data = f.readlines()
    # print(data)
    f.close()
    for _ in range(int((len(data)-2)/3)):
        data.remove('\n')
    data2 = [[data[2*i].split(' '), data[2*i+1].split(' ')]
             for i in range(int(len(data)/2))]
    # print(data2)
    data3 = []
    for i in data2:
        temp = []
        for j in range(2):
            temp.append(''.join([str(int(x)-1) for x in i[j]]))
        data3.append(temp)
    print('Permutations:')
    for i in data3:
        print(i)


def main():
    import time
    ff = input('file?\n' +
               r'(Default: C:\Users\renli\！' +
               r'！think jupyter\rosalind_rear (5).txt)' +
               '\n')
    time_start = time.time()
    input_(ff)
    print('Reversal distances:')
    for i in data3:
        print(rd(i), end=' ')
    print('')
    time_end = time.time()
    print('Time taken = {}s'.format(time_end - time_start))


if __name__ == '__main__':
    main()
