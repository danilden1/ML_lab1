# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def polindrome(inp_str):
    if type(inp_str) != str:
        return None
    inp_str = inp_str.replace(' ', '')
    if len(inp_str) < 2:
        return None
    inp_str = inp_str.lower()
    rev_str = inp_str[::-1]
    if rev_str == inp_str:
        return True
    else:
        return False

# Press the green button in the gutter to run the script.
test_list = [
    'rar',
    'tar',
    'Tar',
    'Rar',
    'R a R',
    'T a R',
    'T',
    ' T ',
    3
]
for test_string in test_list:
    print(polindrome(test_string))
#polindrome(test_list)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
