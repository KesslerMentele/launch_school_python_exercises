# Filter

scores = [96, 47, 113, 89, 100, 102]

def count_high(score_list):
    if type(score_list) is not list: return None
    count = 0
    for scores in score_list:
        if scores >= 100: count +=1
    return count

print(count_high(scores))