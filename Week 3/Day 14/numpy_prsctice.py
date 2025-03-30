import numpy as np
from numpy.ma.extras import average

columns = ['Student ID', 'Name', 'Grade Level', 'Math Score', 'Science Score', 'English Score']

students_data = np.array([
[101, 'Aarav', 10, 88.0, 92.0, 85.0],
[102, 'Diya', 11, 76.0, 85.5, 78.0],
[103, 'Vihaan', 12, 90.0, 88.0, 93.5],
[104, 'Ananya', 10, 72.0, 80.0, 70.0],
[105, 'Ishaan', 11, 95.0, 90.5, 92.0],
[106, 'Kiara', 12, 60.0, 75.0, 65.0],
[107, 'Aditya', 11, 89.0, 91.0, 84.0],
[108, 'Riya', 10, 78.0, 88.5, 77.0],
[109, 'Aryan', 12, 92.0, 95.5, 94.0],
[110, 'Sneha', 10, 85.0, 89.0, 82.0],
[111, 'Manav', 11, 82.0, 87.0, 88.0],
[112, 'Tanya', 12, 75.0, 78.0, 80.5],
[113, 'Aditi', 11, 88.5, 92.0, 90.0],
[114, 'Raj', 10, 82.0, 86.0, 79.0],
[115, 'Siddharth', 12, 91.0, 89.5, 93.0],
[116, 'Nisha', 10, 79.0, 85.0, 81.0],
[117, 'Kabir', 11, 85.5, 88.0, 87.0],
[118, 'Meera', 12, 92.0, 94.0, 91.0],
[119, 'Harsh', 10, 74.0, 77.0, 72.0],
[120, 'Pooja', 11, 90.0, 91.5, 89.0]
])



grade_level=np.array([])
math_score=np.array([])
science_score=np.array([])
english_score=np.array([])

#Question 1: Basic Analysis
# 1. Extract the scores for each subject.
for i in range(0,len(students_data)):
    grade_level=np.append(grade_level,students_data[i,2])
    for j in range(0,6):
        if j==3:
            math_score=np.append(math_score,students_data[i,j]).astype(float)
        if j==4:
            science_score=np.append(science_score,students_data[i,j]).astype(float)
        if j==5:
            english_score=np.append(english_score,students_data[i,j]).astype(float)

print(math_score)
print(science_score)
print(english_score)

# 2. Calculate the average, maximum, and minimum scores for Math, Science, and
# English.

print(f"Mean of the maths score is {np.mean(math_score)}")
print(f"Mean of the Science score is {np.mean(science_score)}")
print(f"Mean of the English score is {np.mean(english_score)}")


# 3. Identify the student with the highest average score across all subjects.

avg_all=np.array([])
student_names=np.array([])

for i in range(0,len(students_data)):
    avg_all=np.append(avg_all,np.mean(students_data[i,3:].astype(float)))
    student_names=np.append(student_names,students_data[i,1])

maximum=np.max(avg_all)
index=np.where(avg_all==maximum)
print(student_names[index])

#Question 2: Grade-Level Analysis
# 1. Calculate the average scores for each subject by grade level.
grade_unique=np.unique(grade_level)
avg_gray_10=np.array([])
avg_math_score_10=np.array([])
avg_math_score_11=np.array([])
avg_math_score_12=np.array([])
avg_gray_11=np.array([])
avg_gray_12=np.array([])


for grad in grade_unique:
    if grad=="10":
        gray_index=np.where(grad==grade_level)
        maths_avg_gray=np.mean(math_score[gray_index])
        avg_math_score_10=np.append(avg_math_score_10,maths_avg_gray)
        sci_avg_gray=np.mean(science_score[gray_index])
        eng_avg_gray=np.mean(english_score[gray_index])
        average_gray=(maths_avg_gray+sci_avg_gray+eng_avg_gray)/3
        avg_gray_10=np.append(avg_gray_10,average_gray)
    if grad=="11":
        gray_index = np.where(grad == grade_level)
        maths_avg_gray = np.mean(math_score[gray_index])
        avg_math_score_11 = np.append(avg_math_score_11, maths_avg_gray)
        sci_avg_gray = np.mean(science_score[gray_index])
        eng_avg_gray = np.mean(english_score[gray_index])
        average_gray=(maths_avg_gray + sci_avg_gray + eng_avg_gray)/3
        avg_gray_11=np.append(avg_gray_12,average_gray)
    if grad=="12":
        gray_index = np.where(grad == grade_level)
        maths_avg_gray = np.mean(math_score[gray_index])
        avg_math_score_12 = np.append(avg_math_score_12, maths_avg_gray)
        sci_avg_gray = np.mean(science_score[gray_index])
        eng_avg_gray = np.mean(english_score[gray_index])
        average_gray=(maths_avg_gray + sci_avg_gray + eng_avg_gray) / 3
        avg_gray_12=np.append(avg_gray_12,average_gray)

print(f"Grad 10 :{np.mean(avg_gray_10)}")
print(f"Grad 11 :{np.mean(avg_gray_11)}")
print(f"Grad 12 :{np.mean(avg_gray_12)}")



# 2. Determine which grade level has the highest average Math score.
print("Grad 10 : ",np.max(avg_math_score_10))
print("Grad 11 : ",np.max(avg_math_score_11))
print("Grad 12 : ",np.max(avg_math_score_12))


#Question 3: Filtering and Conditional Operations
# 1. Select all students with an average score greater than 85.
print(student_names[np.where(avg_all>85)])

# 2. Find students who scored below 70 in any subject.
print(student_names[np.where(((math_score<70) | (science_score<70) | (english_score<70) ))])


# 3. Identify students in grade 12 with a Science score above 85.

print(student_names[np.where((science_score>85) & (grade_unique==12))])
# print(grade_level[np.where(science_score<85)])
