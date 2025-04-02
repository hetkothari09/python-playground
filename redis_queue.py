from itertools import takewhile

import redis

r = redis.Redis(
    host="localhost",
    port="6379",
    db=0
)

def enqueue(queue_name, element):
    # pushes 1 element on the right side of the queue, simulating a queue
    r.rpush(queue_name, element)
    return f"Pushed element: {element}\n"

def dequeue(queue_name):
    # pops 1 element from the left side of the queue, simulating a queue
    popped_task = r.lpop(queue_name)
    if popped_task:
        return f"Popped element is {popped_task}\n"
    else:
        return "There is no element present in the queue\n"

if __name__ == '__main__':
    task_size = int(input("Enter the number of tasks:"))
    while True:
        print("REDIS QUEUE IMPLEMENTATION: \n")
        print("1. Queue your tasks")
        print("2. Dequeue your tasks")
        print("3. Print the queue")
        print("4. Exit")
        choice = int(input("\nEnter your choice:"))
        if choice == 1:
            i = 0
            while i < task_size:
                task_name = input("Enter task name: ")
                print(enqueue("my_task_queue", task_name))
                i += 1
        elif choice == 2:
            popped_element = dequeue("my_task_queue")
            print(popped_element)
        elif choice == 3:
            values = r.lrange("my_task_queue", 0, 100)
            for i in values:
                print(i.decode())
            print()
        elif choice == 4:
            exit()
        else:
            print("Enter a valid response!")