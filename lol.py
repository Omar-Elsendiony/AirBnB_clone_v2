def reverse_number(num):
    try:
        num = int(num)
    except ValueError:
        return 'not a number'
    negative = 1 if num < 0 else -1
    num = str(num * -negative)
    reverse = num[::-1]
    reverse = int(reverse) * -negative
    return reverse

print(reverse_number(78))
