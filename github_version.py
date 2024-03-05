print('hello world')
def isEvenNumber(n: int):
    pass

def isSquareNumber(n: int):
    pass

if __name__ == "__main__":
    n = int(input())
    cnt = 0

    for i in range(1, n + 1):
        if (isEvenNumber(i) and isSquareNumber(i)):
            cnt += 1
    
    print(cnt)