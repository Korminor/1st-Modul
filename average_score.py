grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
re_students = sorted(students)

average_1 = (sum(grades[0])/5)
average_2 = (sum(grades[1])/4)
average_3 = (sum(grades[2])/4)
average_4 = (sum(grades[3])/3)
average_5 = (sum(grades[4])/5)
#print(average_1,average_2,average_3,average_4,average_5)

average_score = dict()
#print(re_students)
average_score.update({re_students[0]:average_1,
                      re_students[1]:average_2,
                      re_students[2]:average_3,
                      re_students[3]:average_4,
                      re_students[4]:average_5})
print(average_score)