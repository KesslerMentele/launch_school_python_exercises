"""
The returns were swapped, if the date is in events then that date is not available.
"""

events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

def is_date_available(date):
    if date in events:
        return False

    return True

print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True