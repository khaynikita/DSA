#errors and exceptions
#print(a)0  #syntax error
# x=-5
# if x<0:
#     raise Exception('x should be an integer')
# assert(x==0),"s is postive"
try:
    A=5/0
except Exception as e:
    print(e)