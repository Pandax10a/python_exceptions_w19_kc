
from math import nan, pi


try:
    string_to_number = 'hi this is string' + 22
except TypeError:
    print("can only concatenate str to str not to int")
except:
    print('this will always happen')
finally:
    string_to_number = "hi this is a string " + '22'
    print(string_to_number)


def get_user_input():
    user_num = input('enter a number: ')
    try:
        float(user_num)
    except ValueError:
        user_num = input('try again this time a number: ')
    except:
        print('just enter a simple number')
    finally:
        if(user_num == nan):
            user_num = pi
            print('i have chosen for you, the number is pi')
    result_outside_saved.append(user_num)
    return user_num

result_outside_saved = []

get_user_input()
get_user_input()
   
sum_result = float(result_outside_saved[0]) + float(result_outside_saved[1])

print(sum_result)