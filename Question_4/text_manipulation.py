
def print_index(file):
    lines = 1
    dict = {}
    for line in (file):
        for word in (x:= line.split()):
            if word.rstrip('.') in dict:
                dict[word.rstrip('.')] += [lines]
            else:
                dict[word.rstrip('.')] = [lines]
        lines += 1

    word_lst = sorted(list(map(lambda x: x, dict.items())))
    pretty_print_index(word_lst)
    
def pretty_print_index(word_lst):
    max_word_len = max(len(word) for word, _ in word_lst)
    
    for word, lines_number in word_lst:
        join_ = ", ".join(str(line) for line in lines_number)
        print(f'{word.lower():<{max_word_len}} : {join_}')
        

def compare_files(file1, file2):
    file1_ = {word.rstrip() for lines in file1 for word in (lines.split())}
    file2_ = {word.rstrip() for lines in file2 for word in (lines.split())}
    intersection_ = len(list((file1_).intersection(file2_)))
    
    print(file1_)
    union_ = len((list((file1_).union(file2_))))
    # headers = ['Number of words common', 'Total number of words']
    
    print(f'Number of words common: {intersection_}\
          \nTotal number of words: {union_}')
        


file1 = open('random_text.txt', 'r')
file2 = open('random_text2.txt', 'r')

print_index(file1)
# compare_files(file1, file2)

