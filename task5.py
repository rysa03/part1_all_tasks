def string_length(test):
    return len(test)
def test_string_length():
    assert string_length('hello!') == 6
    assert string_length('banana') == 6
    assert string_length('8') == 1
    assert string_length('funnyguys') == 9
    assert string_length('101') == 3
print("YOUR CODE IS CORRECT!")
test_string_length()
#a=input()
#b=len(a)
#print(b)