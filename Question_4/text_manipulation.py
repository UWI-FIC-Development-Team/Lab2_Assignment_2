import pprint
def print_txt(file):
    lines = 1
    dict = {}
    for i in (file):
        u = i.split()
        for j in u:
            if j.rstrip('.') in dict:
                dict[j.rstrip('.')] += [lines]
            else:
                dict[j.rstrip('.')] = [lines]
        lines += 1

    print(sorted(list(map(lambda x: x, dict.items()))))
        
        

             
        
file1 = open('random_text.txt', 'r')

print_txt(file1)
