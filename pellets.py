def big_divide(s):
    new_list = []
    carry = 0
    for c in s:
        c = int(c)
        new_list.append(str(c // 2 + carry * 5))
        carry = c % 2
    for c, i in zip(new_list, range(len(new_list))):
        if c != '0':
            return ''.join(new_list[i:]), carry
    return '', carry

def number(s):
    bits = []
    while len(s):
        s, c = big_divide(s)
        bits.append(c)
    return bits

def bits_sum_one(bits):
    for i in range(len(bits)):
        if bits[i] == 1:
            bits[i] = 0
        else:
            bits[i] = 1
            return 1
    bits.append(1)
    return 1


def bits_subs_one(bits):
    bits[0] = 0
    return 1

def divide_by_2(bits):
    count = 0
    while bits[0] == 0:
        count += 1
        bits.pop(0)
    return count

def solution(n):
    bits = number(n)
    if not bits:
        return 1
    k = 0
    while len(bits) > 1:
        if bits[0] == 1:
            if bits[1] == 1:
                if len(bits) > 2:
                    k += bits_sum_one(bits)
                else:
                    k += bits_subs_one(bits)
            else:
                k += bits_subs_one(bits)
        else:
            k += divide_by_2(bits)
    return k



print(solution(str(9 * 10 ** 309)))