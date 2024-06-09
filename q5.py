def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_special_number(num):
    sum_factorials = 0
    original_num = num
    while num > 0:
        digit = num % 10
        sum_factorials += factorial(digit)
        num //= 10
    return sum_factorials == original_num

num = int(input("Enter a number: "))
if is_special_number(num):
    print(num, "is a special number.")
else:
    print(num, "is not a special number.")
