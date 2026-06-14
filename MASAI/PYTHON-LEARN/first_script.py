# Examples of list comprehensions and lambda functions

# 1. Simple list comprehension: squares of numbers 0-9
squares = [x*x for x in range(10)]

# 2. List comprehension with condition: even numbers from 0-9
evens = [x for x in range(10) if x % 2 == 0]

# 3. Nested list comprehension: multiplication table 1-3 by 1-3
mult_table = [[i * j for j in range(1, 4)] for i in range(1, 4)]

# 4. Using lambda with map to double values
double = list(map(lambda x: x * 2, range(5)))

# 5. Using lambda with filter to keep odd numbers
odds = list(filter(lambda x: x % 2 == 1, range(10)))

# 6. Using lambda as sorting key: sort tuples by second element
pairs = [(1, 3), (2, 1), (3, 2)]
pairs_sorted_by_second = sorted(pairs, key=lambda t: t[1])

if __name__ == '__main__':
	print('squares:', squares)
	print('evens:', evens)
	print('mult_table:', mult_table)
	print('double:', double)
	print('odds:', odds)
	print('pairs_sorted_by_second:', pairs_sorted_by_second)
