print('hello world')
def isEvenNumber(n: int):
    return n % 2 == 0

def isSquareNumber(n: int):
    return int(n ** 0.5) ** 2 == n

def test_isEvenNumber():
    assert isEvenNumber(2) == True
    assert isEvenNumber(3) == False
    assert isEvenNumber(4) == True
    assert isEvenNumber(5) == False
    assert isEvenNumber(6) == True
    assert isEvenNumber(7) == False
    assert isEvenNumber(8) == True
    assert isEvenNumber(9) == False
    assert isEvenNumber(10) == True

def test_isSquareNumber():
    assert isSquareNumber(1) == True
    assert isSquareNumber(2) == False
    assert isSquareNumber(3) == False
    assert isSquareNumber(4) == True
    assert isSquareNumber(5) == False
    assert isSquareNumber(6) == False
    assert isSquareNumber(7) == False
    assert isSquareNumber(8) == False
    assert isSquareNumber(9) == True
    assert isSquareNumber(10) == False

if __name__ == "__main__":
    n = int(input())
    cnt = 0

    for i in range(1, n + 1):
        if (isEvenNumber(i) and isSquareNumber(i)):
            cnt += 1
    
    print(cnt)
print('sửa code')
