"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: 整數，需要先處理負值的狀況
	:return: 整數中最大的位數
	"""
	if n < 0:
		n = n * -1
	max_num = n % 10
	# 不return會出現None
	return find_largest_digit_helper(n, max_num)


def find_largest_digit_helper(n, max_num):
	"""
	:param n: 整數，需要先處理負值的狀況
	:param max_num: n當中最大的位數，初始值為個位數
	透過遞迴的方式，在每一次呼叫函數時，將n//10的數值再取其除以10的餘數，來跟max_num做比較
	"""
	# 如果n == 12345，最開始的max_num == 5
	if n // 10 == 0:
		if n > max_num:
			max_num = n
		return max_num
	else:
		if max_num < n % 10:
			max_num = n % 10
		return find_largest_digit_helper(n // 10, max_num)


if __name__ == '__main__':
	main()
