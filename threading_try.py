import threading
import time


def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for 5 seconds \n'.format(name))
    time.sleep(n)
    print('{} has woke up from sleep \n'.format(name))


# t = threading.Thread(target=sleeper, name='thread1', args=(5, 'thread1'))
# t.start()

threads_list = []

start = time.time()
for i in range(5):
    t = threading.Thread(target=sleeper, name='thread{}'.format(i), args=(5, 'thread{}'.format(i)))
    threads_list.append(t)
    t.start()
    print('{} has started'.format(t.name))


for i in threads_list:
    t.join()

end = time.time()
print('time taken: {}'.format(end-start))
print('All five threads have finished their jobs')


def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for 5 seconds \n'.format(name))
    time.sleep(n)
    print('{} has woke up from sleep \n'.format(name))


start = time.time()
for i in range(5):
    print('iteration {} has started'.format(i))
    sleeper(5, i)

end = time.time()

print('time taken: {}'.format(end-start))