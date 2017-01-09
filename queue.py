queue = ["wake up", "Have a coffee", "Have a shower", "Get dresses", "Have a nice day"]

def view():
    for x in range (len(queue)):
        print (queue[x])
def push():
    item = raw_input("please enter the item wich to add to the queue: ")
    queue.append(item)

def pop():
    item = queue.pop()
    return item

print queue.pop(0)
print pop()


push()
view()
print pop()
