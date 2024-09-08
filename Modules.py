import sys

print(sys.executable)
print(sys.platform)
print(sys.argv[0])
print(sys.version_info.major)

print(sys.getsizeof(1))
print(sys.getsizeof(42))
print(sys.getsizeof(1.0))

print(sys.getsizeof(""))
print(sys.getsizeof("a"))
print(sys.getsizeof("ab"))
print(sys.getsizeof("abcedfghij"))
