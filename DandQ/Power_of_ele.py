def power_of_ele(base, power):
    if power == 0:
        return 0
    elif power == 1:
        return base
    else:
        sub = power//2
        val = power_of_ele(base, sub)
        c =  val * val

        if power % 2 == 0:
            return c
        else:
            return c * base

ans = power_of_ele(2, 7)
print(ans)