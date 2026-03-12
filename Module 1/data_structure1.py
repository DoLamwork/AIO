#Given that the teacher cannot remember students' names, please develop a program to help her find a student's name based on his/her seat location in the class
#The class has 3 rows and 2 columns of seats
# %% 1D list
students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
row_class = 3
col_class = 2
def find_student(row, col):
    index = (row - 1) * col_class + (col - 1)
    if index < len(students):
        return students[index]
    else:
        return "No student at this seat"
#find student at row 2, column 1
print(find_student(2, 1))
#find student at row 3, column 2   
print(find_student(3, 2))

# %% 2D list 
students_2d = [["Alice", "Bob"], ["Charlie", "David"], ["Eve", "Frank"]]
def find_student_2d(row, col):
    if row <= len(students_2d) and col<= len(students_2d[0]):
        return students_2d[row - 1][col - 1]
    else:
        return "No student at this seat"

#find student at row 2, column 1
print(find_student_2d(2, 1))
#find student at row 3, column 2   
print(find_student_2d(3, 2))
# %%
