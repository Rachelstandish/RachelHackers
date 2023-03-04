score_list = []
just_scores_list = []
names = []
for _ in range(int(3)):
    name = input("name ")
    score = float(input("score "))
    mini_list = [name, score]
    score_list.append(mini_list)
for i in score_list:
    score = (i[1])
    just_scores_list.append(score)
lowest = min(just_scores_list)
just_scores_list.remove(lowest)
new_lowest = min(just_scores_list)
while new_lowest == lowest:
    just_scores_list.remove(new_lowest)
    new_lowest = min(just_scores_list)
else:
    second_lowest = min(just_scores_list)
    for i in score_list:
        if i[1] == second_lowest:
            names.append(i[0])
    for n in sorted(names):
        print(n)






















