def continous_xor(start,length):
    if start % 2 == 0:
        if length % 4 == 0:
            return 0
        elif length % 4 == 1:
            return start+length-1
        elif length % 4 == 2:
            return 1
        else:
            return (start+length-1)^1
    elif start % 2 == 1:
        if length % 4 == 1:
            return start
        elif length % 4 == 2:
            return start ^ (start + length - 1)
        elif length % 4 == 3:
            return start - 1
        else:
            return (start-1) ^ (start + length - 1)

def solution(start, length):
    x = 0
    for i in range(length):
        i = length - i
        x = x ^ continous_xor(start, i)
        start += length
    return x

for i in range (1,40):
    print(i,solution(0, i))