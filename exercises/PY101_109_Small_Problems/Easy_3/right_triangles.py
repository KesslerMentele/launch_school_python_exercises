# Right Triangles

def triangle(n):
    i = 1
    while i <= n:
        print( ' ' * (n-i) + '*' * i)
        i += 1

triangle(5)

triangle(9)