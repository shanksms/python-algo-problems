def find_sum_of_two_method1(A, val):
  s = set()
  for i in A:
    if val - i in s:
      return True
    s.add(i)
  return False;

def find_sum_of_two_method2(A, val):
    i = 0
    j = len(A) - 1
    while i < j:
        sum = A[i] + A[j]
        if sum == val:
            return True
        elif sum > val:
            j = j - 1
        else:
            i = i + 1
    return False

def test(v, val, expected):
  output = find_sum_of_two_method1(v, val)
  print("exist(A, " + str(val) + ") = " + str(output) + "\n")
  assert expected == output


def main():
  v = [2, 1, 8, 4, 7, 3]
  test(v, 3, True)
  test(v, 20, False)
  test(v, 1, False)
  test(v, 2, False)
  test(v, 7, True)

main()
