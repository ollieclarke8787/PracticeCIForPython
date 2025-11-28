import numpy as np

def func1(n:int) -> int:
    return n*n

def func2(s:str) -> str:
    return s[:-1]

def func3(list:list) -> list:
    return list[::-1]

if __name__ == "__main__":
    print(func1(5))
    print(func2("Hello There"))
