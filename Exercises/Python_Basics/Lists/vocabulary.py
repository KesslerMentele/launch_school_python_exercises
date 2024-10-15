# Vocabulary

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

def extract_items(list_or_item):
    if isinstance(list_or_item, list):
        for item in list_or_item:
            extract_items(item)
    else:
        print(list_or_item)

extract_items(vocabulary)

