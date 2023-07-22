from math import prod
from ast import literal_eval
from bisect import insort_left
from bisect import bisect_left
from functools import cmp_to_key

def compare(left, right):
    match left, right:
        case int(), int():
            return left - right
        case list(), list():
            for l, r in zip(left, right):
                if diff := compare(l, r):
                    return diff
            return len(left) - len(right)
        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])  
        case _, _:
            raise Exception("Invalid Type")

def solution(file_path: str) -> int:
    with open(file_path, "r") as file:
        packets = []
        while True:
            left = literal_eval(file.readline())
            insort_left(packets, left, key=cmp_to_key(compare))
            
            right = literal_eval(file.readline())
            insort_left(packets, right, key=cmp_to_key(compare))
            
            if not file.readline():
                break
        insort_left(packets, [[2]], key=cmp_to_key(compare))
        insort_left(packets, [[6]], key=cmp_to_key(compare))
        
        return prod([i+1 for i in range(len(packets)) if packets[i] == [[2]] or packets[i] == [[6]]])

if __name__ == "__main__":
    output: int = 140
    res: int = solution("./test")
    
    if res != output:
        print(f"\nDid not pass test:\n\tExpected {output}, returned {res}")
    else:
        print("\nPassed test!")

    res = solution("./input")
    print(f"\nSolution for input: {res}")
