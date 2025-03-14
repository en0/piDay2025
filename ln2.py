"""The simplest example of a spigot algorithm i could find.

This algorithm calculates the binary digits of log(2)

Identity Function:
ln(2) = sum(1/(k*2^k)) where k = range(1, infinity)

Isolating the desired digit:
2^(n-1) * ln(2) = 2^(n-1) * sum(1/(k*2^k)) where k = range(1, infinity)

But we need to split this out into HEAD and TAIL where the HEAD holds values with orders of largness and the TAIL holds values with order of smallness.

HEAD = sum((2^(n-1-k)) / k) where k = range(1, n-1) # This isolates the positive digits
TAIL = sum(1/(k*2^(k-n-1))) where k = range(n, infinity) # this isolates the negative digits

but, we can simplify it more by taking a modulo of the positive part.
HEAD = sum((2^(n-1-k) % k) / k)

Now we can sum-up the HEAD and a few of the first values from TAIL and convert the digit to binary.
"""
import math

def ln2_spigot(n, p=10):
    sum_of_c = 0
    sum_of_d = 0
    for k in range(1, n+p):
        if k < n:
            a = math.pow(2, (n-1-k))
            b = a % k
            c = b / k
            sum_of_c += c
        else:
            d = 1 / (k*math.pow(2, k - (n - 1)))
            sum_of_d += d
    x = (sum_of_c % 1) + sum_of_d
    return 1 if x * 2 % 2 >= 1 else 0

ans = [str(ln2_spigot(n)) for n in range(1, 100)]
print("0." + "".join(ans))

