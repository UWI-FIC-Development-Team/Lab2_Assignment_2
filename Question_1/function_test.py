range_lst = [
        (range(90,100),'A+'), (range(80,89),'A'),(range(75,79),'A-'),
        (range(70,74),'B+'),(range(65,69),'B'),(range(60,64),'B-'),
        (range(55,59), 'C+'),(range(50,54),'C'),(range(40,49),'F1'),
        (range(30,39),'F2'), (range(0,29),'F3')
             ]

creditlist = {
        'COMP1210': 3, 'COMP1215': 3, 'COMP1205': 3, 
        'COMP2210': 3, 'COMP2220': 3, 'COMP2225': 3, 
        'FOUN2003': 1}

qplist = {
        'A+': 4.3, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 
        'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 
        'F1': 1.7, 'F2': 1.3, 'F3': 0.0
          }


       
def compute_letter_grade(grade):
                letter_grade = [lst[1] for lst in range_lst 
                                if grade in lst[0] ]
                return letter_grade[0]


def my_map(f, lst):
        if lst == []: return []
        else:return [ f(lst[0][1])] + my_map(f,lst[1:])
        
def calc_letter_grade(std_lst):
        ccode_list = [i[0] for i in std_lst]
        grade_list = my_map(compute_letter_grade, std_lst)
        return list(zip(ccode_list, grade_list))

def convert_to_wtqp(std_lst):
        credits = [creditlist[i[0]] for i in std_lst if i[0] in creditlist ]
        qp = [qplist[j[1]] for j in std_lst if j[1] in qplist ]
        return list(zip(credits, qp))

def calc_gpa(std_lst):
        total_grade_point = [sum(map(lambda x: (x[0] * x[1] ), 
                                     convert_to_wtqp(std_lst)))]
        total_credit_hrs = [sum(map(lambda x: x[0], 
                                    convert_to_wtqp(std_lst)))]
        gpa = total_grade_point[0]/total_credit_hrs[0]
        return f"{gpa:.2f}"

def main():
        lst = [ ('COMP1215' , 'B-') , ('FOUN2003' , 'A')]
        calc_letter_grade(lst)
        print(calc_gpa(lst))
        
main()

# courses = [ ('COMP1215' , 90) , ('FOUN2003' , 100)]

# lst = []
# for x in courses:
#     a,b = x
#     lst.append(b)
# print(lst)
