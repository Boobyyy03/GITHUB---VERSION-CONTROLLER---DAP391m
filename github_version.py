print('hello world')
def isEvenNumber(n: int):
    return n % 2 == 0

def isSquareNumber(n: int):
    return int(n ** 0.5) ** 2 == n

if __name__ == "__main__":
    n = int(input())
    cnt = 0

    for i in range(1, n + 1):
        if (isEvenNumber(i) and isSquareNumber(i)):
            cnt += 1
    
    print(cnt)