def new_func(func):
    def wrapped(*args, ** kwargs):
        if args[0] == 'root' and args[1] == '123':
            print('welcome!')
            return func()
        else:
            print('username or password is wrong')

    return wrapped


@new_func
def run():
    print('begin')


run('root', '123')
