

import random
import timeit
import matplotlib.pyplot as plt


def fn(prices):
    if len(prices) < 2:
        return 'Please supply a list with at least 2 prices.'

    min_val = prices[0]
    max_profit = prices[1] - prices[0]

    for curr_t in range(1, len(prices)):
        curr_val = prices[curr_t]
        curr_profit = curr_val - min_val
        max_profit = max(max_profit, curr_profit)
        min_val = min(min_val, curr_val)
    return max_profit


x1 = 1
x2 = 1200
x3 = 4000
x4 = 7000
x5 = 10000

list1 = [i for i in range(x1)]
list2 = [i for i in range(x2)]
list3 = [i for i in range(x3)]
list4 = [i for i in range(x4)]
list5 = [i for i in range(x5)]

random.shuffle(list1)
random.shuffle(list2)
random.shuffle(list3)
random.shuffle(list4)
random.shuffle(list5)

c1 = [x1, timeit.timeit(stmt='fn(list1)',
                        number=2, globals=globals())]

c2 = [x2, timeit.timeit(stmt='fn(list2)',
                        number=2, globals=globals())]

c3 = [x3, timeit.timeit(stmt='fn(list3)',
                        number=2, globals=globals())]

c4 = [x4, timeit.timeit(stmt="fn(list4)",
                        number=2, globals=globals())]

c5 = [x5, timeit.timeit(stmt="fn(list5)",
                        number=2, globals=globals())]


coords = [c1, c2, c3, c4, c5]
x_vals = [n[0] for n in coords]
y_vals = [n[1] for n in coords]

plt.scatter(x_vals, y_vals, color="red", marker="*", s=30)
plt.title('Run Time(s) vs. Input Size(n)')
plt.xlabel('input size (n)')
plt.ylabel('time (s)')
plt.show()
