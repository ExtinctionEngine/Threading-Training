# -*- coding:utf-8 -*-
# Threading part 4 - subclassing
import time
import threading


# *Source code*

def run(self):
    """Method representing the thread's activity.
    You may override the method in a subclass.
    The stantard run() mehod
    invokes the callable object passed to
    the object's constructor as
    the target argument, if any, with sequential and
    keyword arguments taken
    from the args and kwargs arguments, respectively.
    """
    try:
        if self._target:
            self._target(*self._args, **self._kwargs)
    finally:
        # Avoid a recycle if the thread is running a function with
        # an argument that has a member that points to the thread.
        del self._target, self._args, self._kwargs


class MyThread(threading.Thread):
    # TEST ONE: OVERRIDING run
    def run(self):
        print('{} has started!'.format(self.getName()))
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a recycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs
            print('{} has finished!'.format(self.getName()))


def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for 5 seconds \n'.format(name))
    time.sleep(n)
    print('{} has woke up from sleep \n'.format(name))


for i in range(4):
    t = MyThread(target=sleeper, name='thread {}'.format(i + 1), args=(3, 'thread {}'.format(i + 1)))
    t.start()
