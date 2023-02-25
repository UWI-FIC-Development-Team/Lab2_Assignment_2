range_lst = [
        (range(90,100),'A+'), (range(80,89),'A'),(range(75,79),'A-'),
        (range(70,74),'B+'),(range(65,69),'B'),(range(60,64),'B-'),
        (range(55,59), 'C+'),(range(50,54),'C'),(range(40,49),'F1'),
        (range(30,39),'F2'), (range(0,29),'F3')
             ]

       
def compute_letter_grade( grade):
                letter_grade = [lst[1] for lst in range_lst 
                                if grade in lst[0] ]
                return letter_grade[0]


def my_map(f, lst):
        if lst == []: return []
        else:return [ f(lst[0][1])] + my_map(f,lst[1:])
        
def calc_letter_grade(std):
        ccode_list = [i[0] for i in std]
        grade_list = my_map(compute_letter_grade, std)
        return list(zip(ccode_list, grade_list))
        

def main():
        lst = [ ('COMP1210' , 80) , ('COMP1215' , 60)]
        print(calc_letter_grade(lst))
main()
