def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True
    return False


def two_sum2(numbers, target):
    s = set()
    for num in numbers:
        if (target - num) in s:
            return True
        s.add(num)
    return False


print(two_sum([1, 3, 7], 8) == True)
print(two_sum([1, 3, 7], 6) == False)
print(two_sum([], 1) == False)
print(two_sum([1, 1], 2) == True)
print(two_sum([1, 3, 7], 8) == True)
print(two_sum([1], 1) == False)