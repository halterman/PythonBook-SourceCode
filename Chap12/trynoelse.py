def fun1():
    try:
        print('try code')
    except:
        print('exception handling code')
    else:
        print('no exception raised code')
        x = int('a')  # Raises an exception


def fun2():
    try:
        print('try code')
        print('no exception raised code')
        x = int('a')  # Raises an exception
    except:
        print('exception handling code')


print('Calling fun2')
fun2()
print('-------------')
print('Calling fun1')
fun1()
