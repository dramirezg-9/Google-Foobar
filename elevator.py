

def solution(l):
    new_list = [[int(j) for j in i.split('.')] for i in l]
    new_list.sort()
    return ['.'.join([str(j) for j in i]) for i in new_list]

print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))