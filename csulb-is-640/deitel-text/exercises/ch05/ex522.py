'''
5.22 (Simulating a Queue with a List) In this chapter, you simulated a stack using a list.
You also can simulate a queue collection with a list. Queues represent waiting lines similar
to a checkout line in a supermarket. The cashier services the person at the front of the line
first. Other customers enter the line only at the end and wait for service.

In a queue, you insert items at the back (known as the tail) and delete items from the
front (known as the head). For this reason, queues are first-in, first-out (FIFO) collections. 
The insert and remove operations are commonly known as enqueue and dequeue.

Queues have many uses in computer systems, such as sharing CPUs among a potentially large number 
of competing applications and the operating system itself. Applications not currently being 
serviced sit in a queue until a CPU becomes available. The application at the front of the queue 
is the next to receive service. Each application gradually advances to the front as the 
applications before it receive service.

Simulate a queue of integers using list methods append (to simulate enqueue) and pop
with the argument 0 (to simulate dequeue). Enqueue the values 3, 2 and 1, then dequeue
them to show that they’re removed in FIFO order.
'''

def simulate_queue(queue_list = [3, 2, 1]):
    in_list = queue_list
    queue = enqueue_list(in_list)
    queue = dequeue_list(queue)

def enqueue_list(list_to_queue):
    in_list = list_to_queue
    queue = []
    print('enqueueing the list')
    for i in in_list:
        queue.append(i)
        print(f'enqueued {i}, queue is now {queue}')
    return queue

def dequeue_list(list_to_dequeue):
    queue = list_to_dequeue
    print('dequeueing the list')
    while len(queue) > 0:
        dequeued = queue.pop(0)
        print(f'dequeued {dequeued}, queue is now {queue}')
    print('queue is empty.')
    return queue

simulate_queue(['a', 'b', 'c'])