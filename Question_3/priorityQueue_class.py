class Queue:
    def __init__(self):
        pass

    def enqueue_p(self, pos, item, lst):
        lst.insert(pos, item)
        print(lst)
        
    def get_pos(self, el, lst):

        if lst == []:return 0
        elif el[0] < lst[0][0]:return 0 + self.get_pos(el,[])
        else:return 1 + self.get_pos(el,lst[1:])
        
        

queue = Queue()
lst = [(1,"g"),(2,"r"),(5,"t"),(6,"e")]
item = (4,"f")
pos = queue.get_pos(item,lst)
queue.enqueue_p(pos,item, lst)





