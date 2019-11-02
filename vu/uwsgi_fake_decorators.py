def spool(func, *args,**kwargs):
    class Spooler():
        @staticmethod
        def spool(*args, **kwargs):
            print('Called')
            return
    def wrapper():
        print(func)
        func(args, **kwargs)
        return Spooler
        # return func(args,**kwargs)
    return wrapper()

def timer(*outer_args,**outer_kwargs):
    def decorator(fn):
        def decorated(*args,**kwargs):
            print(outer_args)
            print(outer_kwargs)
            return fn(*args,**kwargs)
        return decorated
    return decorator

def cron(*outer_args,**outer_kwargs):
    def decorator(fn):
        def decorated(*args,**kwargs):
            print(outer_args)
            print(outer_kwargs)
            return fn(*args,**kwargs)
        return decorated
    return decorator