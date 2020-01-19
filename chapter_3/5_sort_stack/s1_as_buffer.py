def sort(s1):
    s2 = []

    while s1:
        tmp = s1.pop()
        while s2 and s2[-1] > tmp:
            s1.append(s2.pop())
        s2.append(tmp)

    while s2:
        s1.append(s2.pop())


if __name__ == '__main__':
    stack = [7, 10, 5, 12, 8, 3, 1]
    print(f'Stack: {stack}')
    sort(stack)
    print(f'Sorted: {stack}')
