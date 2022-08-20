
def 데코레이터_이름(함수):
  print("데코레이터 동작")
  def 내용():
    #사전동작 내용
    print('사전 동작 내용')
    함수()
    #사후동작 내용
    print('사후 동작 내용')
  return 내용
  
@데코레이터_이름
def f():
  print("함수 내부 내용")
f()

# def a_func(b_func):
#     print("a_func")
#     def c_func():
#         print("b_func")
#         b_func()
#     return c_func

# @a_func
# def d_func():
#     print("d_func")

# print("##########")

# d_func()