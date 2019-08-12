import time
import threading

total = 4


def create_items():
    global total
    for i in range(10):
        time.sleep(2)
        print('added item')
        total += 1
    print('creation is done')


def create_items_2():
    global total
    for i in range(7):
        time.sleep(1)
        print('added item')
        total += 1
    print('creation is done')


def limits_items():

    # print('finished sleeping")

    global total
    while True:
        if total > 5:
            print('overload')
            total -= 3
            print('subtracted 3')
        else:
            time.sleep(1)
            print('waiting')


creator1 = threading.Thread(target=create_items)
creator2 = threading.Thread(target=create_items_2)
limitor = threading.Thread(target=limits_items, daemon=True)  # Once the main program terminate, daemon thread will be forced to terminate as well.

creator1.start()
creator2.start()
limitor.start()

creator1.join()  # main program will be blocked before the thread finishes its work
creator2.join()  # main program will be blocked before the thread finishes its work


print('our ending value of total is', total)
