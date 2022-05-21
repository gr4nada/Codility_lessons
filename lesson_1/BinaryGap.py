import re

def solution(N):
    pattern = re.compile('0+1')
    binary = bin(N)
    zeros = pattern.findall(binary)
    max = 0
    for zero in zeros:
        size = len(zero) -1
        if size>max:
            max = size
    return max