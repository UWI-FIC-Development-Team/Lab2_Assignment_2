from ranges_list import range_lst, creditlist, qplist

class Student:
        '''
        Creates a student with an id, first name and last name as a
        list and the course codes and grades as a list of tuples.
        '''
        def __init__(self, id='', lname='', fname='',
                     lst_of_courses_with_grades=[]):
                self.id = id
                self.fname = fname
                self.lname = lname
                self.courses = lst_of_courses_with_grades
                
        def get_id(self):
                '''Returns the id value from the given student record.'''
                return self.id
        
        
        def get_name(self):
                ''' Returns student name as a list from the student record'''
                return [self.fname,self.lname]
        
        def get_courses(self):
                '''Returns a list of tuples where first part of the tuple is the
                course and the second part of the tuple is the corresponding
                grade that the student has received.'''
                return self.courses
        
        def get_fname(self):
                '''Returns student's first name as a string given the student name
                list.
                '''
                return self.fname
        
        def get_lname(self): 
                '''Returns student's last name as a string given the student name
                list.
                '''
                return self.lname
        
        def get_ccode(self): 
                '''Returns the course code from a tuple of course code and grade.
                '''
                return [i[0] for i in self.courses]
        
        def get_grades(self): 
                '''Returns the grade from a tuple of course code and grade.'''
                return [i[1] for i in self.courses]
        
        def compute_letter_grade(self, grade):
                '''Returns the numerical grade as a letter grade'''
                letter_grade = [lst[1] for lst in range_lst 
                                if grade in lst[0] ]
                return letter_grade[0]
        
        def my_map(self, f, lst):
                '''Returns a all letter grades from a list of tuples of, 
                course codes and numrcial grades'''
                if lst == []: return []
                else:return [ f(lst[0][1])] + self.my_map(f,lst[1:])
        
        def calc_letter_grade(self):
                '''Returns a tuple of course codes and letter grades'''
                ccode_list = [i[0] for i in self.courses]
                grade_list = self.my_map(self.compute_letter_grade, self.courses)
                return list(zip(ccode_list, grade_list))
        
        def convert_to_wtqp(self):
                '''Retunrs a tuple of credit weight and quality points'''
                credits = [creditlist[i[0]] for i in self.calc_letter_grade() if i[0] in creditlist ]
                qp = [qplist[j[1]] for j in self.calc_letter_grade() if j[1] in qplist ]
                return list(zip(credits, qp))

        def calc_gpa(self):
                '''Returns gpa to two decimal places'''
                total_grade_point = [sum(map(lambda x: (x[0] * x[1] ), 
                                        self.convert_to_wtqp()))]
                total_credit_hrs = [sum(map(lambda x: x[0], 
                                        self.convert_to_wtqp()))]
                gpa = total_grade_point[0]/total_credit_hrs[0]
                return f"{gpa:.2f}"
        
        def print_student_gpa(self):
                '''Prints Student id, along with student name as list and student gpa'''
                print("Student Id: ", self.get_id())
                print("Student Name: ", self.get_name())
                print("GPA:", self.calc_gpa())
                
        def get_full_name(self):
                return f'{self.fname}{self.lname}'
