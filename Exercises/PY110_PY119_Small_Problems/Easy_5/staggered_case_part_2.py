

def staggered_case(string_in:str)->str:
    count = 0
    out = ''
    for char in string_in:
        if char.isalpha():
            out += char.capitalize() if count % 2 == 0 else char.lower()
            count += 1
        else:
            out += char
    return out

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True