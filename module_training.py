def add(a,b):
    return a+b

def sub(a,b):
    return a-b

#if __name__ == "__main__": 을 쓰면 다른 파일에서 모듈을 불러서 쓸 때는 False가 되기 때문에 다음 문장이 수행되지 않는다.
if __name__ == "__main__":
    print(add(1,4))
    print(sub(4,2))

