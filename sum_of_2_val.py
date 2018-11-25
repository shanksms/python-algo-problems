def find_sum_of_two(A, val):
 #TODO: Write - Your - Code
  s = set()
  for i in A:
    if val - i in s:
      return True
    s.add(i)
  return False;

print(find_sum_of_two([2, 1, 8, 4, 7, 3], 5))
