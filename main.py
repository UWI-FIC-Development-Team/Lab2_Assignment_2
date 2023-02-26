from student_class import Student

def main():
        student1 = Student(id='50000101', fname='Jane', lname='Doe', 
                   lst_of_courses_with_grades=[('COMP1210', 80), ('COMP1215', 60), 
                                               ('COMP2210', 50), ('COMP1205', 60), 
                                               ('FOUN2003', 85), ('COMP2220', 80)
                    ])
        student1.calc_gpa()
        
if __name__ == 'main':
        main()
