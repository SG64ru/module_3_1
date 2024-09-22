calls = 0
def count_calls(calls):
    calls = calls + 1


    def string_info(string):
        string = input("Введите слово - ")
        l_str = len(string)
        up_string = string.upper()
        dow_string = string.lower()
        print(l_str, up_string, dow_string)
        count_calls(calls)
    return count_calls(calls)
    calls = count_calls(calls)
    print(calls)

    string_info(string)

       # def is_contains(string, list_to_search):
        #    global calls
         #   string = input("Введите строку - ")
          #  list_to_search = input("Введите список - ")
           # print(string in list_to_search)
            #count_calls(calls)
        #is_contains(string, list_to_search)

#print(calls)


