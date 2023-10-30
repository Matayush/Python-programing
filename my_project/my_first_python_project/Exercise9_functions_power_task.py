def power(first , second):
    result = 1
    while second > 0:
        result = result * first
        second = second -1
    print(result)

POWER = power
POWER(3,3)