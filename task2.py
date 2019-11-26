"""
Write a function square_number that
takes in a number and squares it.
"""
def square_number(test):
    return test**2
    
#DO NOT remove lines below here, this is designed to test your code.
def test_square_number():
    assert square_number(2) == 4
    assert square_number(8) == 64
    assert square_number(10) == 100
    assert square_number(4) == 16
    print("YOUR CODE IS CORRECT