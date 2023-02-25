from ranges_list import range_lst

class Student:
        def __init__(self, id='', lname='', fname='',
                     lst_of_courses_with_grades=[]):
                self.id = id
                self.fname = fname
                self.lname = lname
                self.courses = lst_of_courses_with_grades
                
        def get_id(self): return self.id
        
        def get_names(self): return (self.lname,self.fname)
        
        def get_courses(self): 
                return self.courses
        
        def get_fname(self): return self.fname
        def get_lname(self): return self.lname
        def get_ccode(self): 
                return [i[0] for i in self.courses]
        def get_grades(self): 
                return [i[1] for i in self.courses]
        
        def compute_letter_grade(self, grade):
                letter_grade = [lst[1] for lst in range_lst 
                                if grade in lst[0] ]
                return letter_grade[0]
        
        def my_map(self, f, lst):
                if lst == []: return []
                else:return [ f(lst[0][1])] + self.my_map(f,lst[1:])
        
        def calc_letter_grade(self):
                ccode_list = [i[0] for i in self.courses]
                grade_list = self.my_map(self.compute_letter_grade, self.courses)
                return list(zip(ccode_list, grade_list))
                          
        
std = Student(lst_of_courses_with_grades=[ ('COMP1210' , 80) , ('COMP1215' , 60) ,
('COMP2210' , 50) , ('COMP1205' , 60) , ('FOUN2003' , 85) , ('COMP2220' , 80) ])

print(std.calc_letter_grade())

                
        
        
