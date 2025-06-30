# Pipeline: Chaining map, filter, and reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

result = reduce(
    lambda acc, x: acc + x,
    map(lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numbers))
)

print(result)
# Output: 56 (i.e., 2² + 4² + 6² = 4 + 16 + 36)
