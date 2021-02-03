import json
school_subject = {}
with open('For_6_Task.txt.txt', 'r') as i:
    for line in i:
        subject, lecture, practice, lab = line.split()
        school_subject[subject] = int(lecture) + int(practice) + int(lab)
print(f'Количество часов по предметам - \n {school_subject}')

#Ерунда какая-то получилась - не разобрался