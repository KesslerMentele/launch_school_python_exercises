# Grade Book

def get_grade(num_1, num_2, num_3):
    average = (num_1 + num_2 + num_3) / 3
    match average:
        case _ if 90 <= average <= 100:
            return 'A'
        case _ if 80 <= average < 90:
            return 'B'
        case _ if 70 <= average < 80:
            return 'C'
        case _ if 60 <= average < 70:
            return 'D'
        case _ if 0 <= average < 60:
            return 'F'


print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True