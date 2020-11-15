# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def sum_mult(list_a, list_b):
    if len(list_a) != len(list_b):
        return None
    list_summ = []
    list_mult = []
    for elem in range(len(list_a)):
        # stupid number sheck
        try:
            list_summ.append(list_a[elem] + list_b[elem])
            list_mult.append(list_a[elem] * list_b[elem])
        except:
            return None
    return [list_summ, list_mult]


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

def max_digit_sum(stop_str, max_numbers):
    numb_list = []
    while True:
        msg = input("Input number ")
        if msg == stop_str:
            print('Input end')
            break
        print(msg)
        try:
            numb_list.append(int(msg))
        except:
            print('wrong format')
        if len(numb_list) >= max_numbers:
            break
    print(numb_list)
    max_summ = 0
    max_index = 0
    for i in range(len(numb_list)):
        sum_of_digits = 0
        number = abs(numb_list[i])
        for digit in str(number):
            sum_of_digits += int(digit)
        print(sum_of_digits)
        if sum_of_digits > max_summ:
            max_summ = sum_of_digits
            max_index = i
    return numb_list[max_index] - max_summ

def goose_weight(breed, sex, age_days):
    table = {
        'H': {'m': {1: 99, 10: 267, 20: 756, 30: 1390, 40: 1800, 50: 2310, 60: 3510, 90: 5320, 120: 6000, 160: 6420},
              'f': {1: 106, 10: 254, 20: 698, 30: 1300, 40: 1730, 50: 2170, 60: 3280, 90: 4470, 120: 5210, 160: 5680}},
        'A': {'m': {1: 99, 10: 394, 20: 965, 30: 1820, 40: 2513, 50: 3440, 60: 4025, 90: 4760, 120: 5250, 160: 5625},
              'f': {1: 95, 10: 395, 20: 977, 30: 1871, 40: 2520, 50: 3230, 60: 3840, 90: 4540, 120: 4630, 160: 5006}},
        'U': {'m': {1: 100, 10: 292, 20: 791, 30: 1410, 40: 1970, 50: 2520, 60: 3420, 90: 4350, 120: 4700, 160: 5110},
              'f': {1: 98, 10: 310, 20: 715, 30: 1230, 40: 1920, 50: 2330, 60: 3190, 90: 3780, 120: 4140, 160: 4530}},
        'K': {1: 102, 10: 250, 20: 700, 30: 1360, 40: 1600, 50: 2600, 60: 3900, 90: 4700, 120: 5100, 160: 5400}}

    try:
        if breed == 'K':
            return table[breed][age_days]
        else:
            return table[breed][sex][age_days]
    except:
        print("Не верные параметры")
        return None


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

# for test_string in test_list:
#   print(polindrome(test_string))
# polindrome(test_list)
l_a = [1, 2, 3, 4, 5]
l_b = [2, 3, 4, 5, 6]

#print(sum_mult(l_a, l_b))
#print(max_digit_sum('stop', 10))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
