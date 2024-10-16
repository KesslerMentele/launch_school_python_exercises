

# Practice Problem 1
def problem_one():
    lst = [10, 9, -6, 11, 7, -16, 50, 8]

    lst_asc = sorted(lst)
    lst_desc = sorted(lst, reverse=True)
    # print(lst_asc)
    # print(lst_desc)


# Practice Problem 2
def problem_two():
    lst = [10, 9, -6, 11, 7, -16, 50, 8]
    lst.sort()
    print(lst)
    lst.sort(reverse=True)
    print(lst)


# Practice Problem 3
def problem_three():
    lst = [10, 9, -6, 11, 7, -16, 50, 8]
    lst.sort(key=str)
    print(lst)
    lst.sort(reverse=True, key=str)
    print(lst)


# Practice Problem 4
def problem_four():
    books = [
        {
            'title': 'One Hundred Years of Solitude',
            'author': 'Gabriel Garcia Marquez',
            'published': '1967',
        },
        {
            'title': 'The Book of Kells',
            'author': 'Multiple Authors',
            'published': '800',
        },
        {
            'title': 'War and Peace',
            'author': 'Leo Tolstoy',
            'published': '1869',
        },
    ]

    def year_published(book):
        return int(book['published'])

    sorted_books = sorted(books, key=year_published)
    print(sorted_books)

