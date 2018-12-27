def reverseWords(s):
    ls = s.split(' ')
    ls = list(reversed(ls))
    print(" ".join(ls))
if __name__ == '__main__':
    reverseWords("Bob likes Alice")
