from tabulate import tabulate

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

    p = sorted(list(map(lambda x: x, dict.items())))
    max_word_len = max(len(word) for word, _ in p)
    for word, lines in p:
        print(f'{word:<{max_word_len}} | {", ".join(str(line) for line in lines)}')
        
        

             
        
file1 = open('random_text.txt', 'r')

print_txt(file1)
