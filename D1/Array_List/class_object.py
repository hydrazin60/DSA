# class Student:
#     # Class attribute
#     school = "ABC High School"  # Shared by all instances

#     def __init__(self  , name, age):
#         # Instance attributes
#         self.names =    name
#         self.ages =    age

# # Class object
# print(Student )   # Output: <class '__main__.Student'>
# obj = Student
# print(obj)

 
# # Creating instance objects
# student1 = Student("Alice", 15 )
# student2 = Student( "Bob", 16)

# print(student1.names , student1.ages)

# # Accessing class attribute via class object
# print(Student.school)  # Output: ABC High School

# # Accessing instance attributes via instance objects
# print(student1.names)  # Output: Alice
# print(student2.names)  # Output: Bob

# # Accessing class attribute via instance objects
# print(student1.school)  # Output: ABC High School
# print(student2.school)  # Output: ABC High School



########################### 1. Instance Method
# class Student:
#     def __init__(self, name, grade):
#         self.name = name   # Instance variable
#         self.grade = grade # Instance variable

#     # Instance method
#     def display_info(self):
#         return f"Name: {self.name}, Grade: {self.grade}"

# # Creating an instance of Student
# student1 = Student("Alice", "Grade 8")
# print(student1.display_info())  # Output: Name: Alice, Grade: Grade 8

###################################### 2. Class Method
# class Student:
#     school = "ABC High School"  # Class variable

#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     # Class method
#     @classmethod
#     def change_school(cls, new_school):
#         cls.school = new_school

# # Using the class method to change the class variable
# print(Student.school)  # Output: ABC High School
# Student.change_school("XYZ High School")
# print(Student.school)  # Output: XYZ High School

###################### 3. Static Method 
class Student:
    school = "ABC High School"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    # Static method
    @staticmethod
    def is_passing_grade(grade):
        # Only a utility method, no access to self or cls
        return grade >= 50

# Using the static method
print(Student.is_passing_grade(75))  # Output: True
print(Student.is_passing_grade(45))  # Output: False
