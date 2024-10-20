

def palindromes(orig:str)->list:
    def substrings(string:str):
        return [string[start:end + 1]
                for start in range(len(string))
                for end in range(len(string))
                if end >= start
                ]
    all_list = substrings(orig)
    return [item for item in all_list if item == item[::-1] and len(item) > 1]





print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True