# 함수에서 재귀호출 : 함수 안에서 자기자신을 호출하는 방식(recursive call)
def hello():
    print('Hello~ ')
    hello()
    
hello()

