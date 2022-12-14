from ast import literal_eval

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
        res: int = 0
        index: int = 0
        while True:
            index += 1

            left = literal_eval(file.readline())
            right = literal_eval(file.readline())
            
            if compare(left, right) < 0:
                res += index
            
            if not file.readline():
                return res

if __name__ == "__main__":
    output: int = 13
    res: int = solution("./test")
    
    if res != output:
        print(f"\nDid not pass test:\n\tExpected {output}, returned {res}")
    else:
        print("\nPassed test!")

    res = solution("./input")
    print(f"\nSolution for input: {res}")
