# Locale Part 1

def extract_language(locale):
    language_code = locale[:2]
    return language_code



print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko