# def dec(f):
#     pass
#
#
# @dec  # double = dec(double)  完全等价，装饰器本质上就是输入和输出（输出不一定）都是函数的函数（因为函数可以作为参数）
# def double(x):
#     return x * 2

import time


def timeit(i):
    def inner(f):
        def wrapper(*args, **kwargs):
            start = time.time()

            for j in range(i):
                ret = f(*args, **kwargs)
            print(f'{time.time() - start:.10f}')
            return ret

        return wrapper  # 必须要有

    return inner


@timeit(10000)
def func(x, y, z):
    return x + y + z


func(1, 2, 3)

from functools import wraps


class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass


class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''

    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass