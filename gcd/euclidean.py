#
#  20-03-2025
#  c @ CNT Lab


def gcd_euclidean(a, b):

    if a < b:
        a, b = b, a
    
    r = 0
    while (r>=0):
        q = a // b
        r = a % b

        if r == 0 :
            break

        a, b = b, r

    return b


print(gcd_euclidean(28, 12))

