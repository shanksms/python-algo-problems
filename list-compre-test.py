
import itertools
a = ["ss", "s"]

b = [(len(s), s) for s in itertools.islice(a, 3)]

print(b)
