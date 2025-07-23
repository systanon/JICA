def checkParity(n):
        if n % 2 == 0:
            return True
        else:
            return False


def main(n):
    dict = {}
    if isinstance(n, int):
        return checkParity(n)
    else:
        for i in n:
            dict[i] = checkParity(i)
    return dict
print(main(3))

print(main([1,2,3,4,5]))