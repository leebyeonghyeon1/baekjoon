def validation_test(value, min_val, max_val):
    if not min_val <= value <= max_val:
        raise ValueError("Value not in range")


sum = 0
for _ in range(5):
    num = int(input())
    validation_test(num, 0, 100)
    sum += num

print(sum)
