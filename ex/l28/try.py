try:
    x = 1/0
except ZeroDivisionError as e:
    print('handling a', type(e))
    x = 0
print(x)

def invert(x):
    y = 1/x
    print('Never printed if x is 0')
    return y

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print('handled', e)
        return 0
