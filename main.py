queue = []

def enqueue(item):   #объявляем функцию
    queue.append(item)    #добавление элемента
    print(f"enqueue({item}): {queue}")    

def dequeue():
    if not queue:    #проверка на пустоту
        print("dequeue: очередь пустая")
        return None
    item = queue.pop(0)    #встроенный метод списка
    print(f"dequeue() == {item}: {queue}")
    return item

enqueue(10)
enqueue(20)
enqueue(30)
dequeue()
enqueue(40)
dequeue()
dequeue()
dequeue()
dequeue()