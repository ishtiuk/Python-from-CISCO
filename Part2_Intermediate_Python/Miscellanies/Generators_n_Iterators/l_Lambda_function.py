
# the Lambda function takes argument and  expression seperated by ':'

#      : retuning part for 0 parametered 
lambda : 2 

#     arg : expression 
lambda x : x * x

two = lambda : 2
sqr = lambda x : x * x
pwr = lambda x, y : x ** y


for i in range(-2, 3):
    print(sqr(i), end='  ')
    print(pwr(i, two()))