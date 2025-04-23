# def greet(a: int, name: str) -> str:
#     return a, name
# a = 5
# x = "world"
# print(greet(a))
# print(a, "относится к типу", type(a))
# print(greet(x))
# print(x, "относится к типу", type(x))

# def task_1(a: int, b: float, c: str, d: list, e: bool) -> int:
#    return type(a), type(b), type(c), type(d), type(e)
# a = 5
# b = 7.008
# c = 'str'
# d = [1, 8, 7, 5]
# e = True
# print(task_1(5, 4.08, 'bg', [2, 9], True))
# print(a, "относится к типу ", type(a))
# print(b, "относится к типу ", type(b))
# print(c, "относится к типу ", type(c))
# print(d, "относится к типу ", type(d))
# print(e, "относится к типу ", type(e))

def task_1() -> int:
    a: int = 5
    b: float = 7.008
    c: string = 'str'
    d: list = [1, 8, 7, 5]
    e: bool = True
    return type(a), type(b), type(c), type(d), type(e), len(d), a
print(task_1())

# print(type(a), type(b), type(c), type(d), type(e))

# print(a, "относится к типу ", type(a))
# print(b, "относится к типу ", type(b))
# print(c, "относится к типу ", type(c))
# print(d, "относится к типу ", type(d))
# print(e, "относится к типу ", type(e))