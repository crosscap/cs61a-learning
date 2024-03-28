def identity_demos():
    a = [10]
    b = a
    a == b
    a is b
    a.extend([20, 30])
    a == b
    a is b
    
    a = [10]
    b = [10]
    a == b
    a is not b
    a.append(20)
    a != b
 
