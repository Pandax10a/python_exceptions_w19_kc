
try:
    string_to_number = 'hi this is string' + 22
except TypeError:
    print("can only concatenate str to str not to int")
except:
    print('this will always happen')
finally:
    string_to_number = "hi this is a string " + '22'
    print(string_to_number)