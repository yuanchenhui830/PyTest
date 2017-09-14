def triangles():
    yield [1,]
    t = [1,1,]
    yield t
    while True:
        t = triangle(t)
        yield t


def triangle(t):
    result = [1,]
    for i in range(len(t)-1):
        result.append(t[i] + t[i+1]) 
    result.append(1)
    return result
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break