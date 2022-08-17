def sum_divisors(n):
  sum = 0
  # Return the sum of all divisors of n, not including n
  empty_list = []
  for num in range(1,n-1):
    if n % num == 0:
      empty_list.append(num)
  for num in empty_list:
      sum = num + sum

  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
