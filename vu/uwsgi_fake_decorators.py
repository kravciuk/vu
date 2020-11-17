def spool(func=None, *args,**kwargs):
    class Spooler():
        def spool(self, *args, **kwargs):
            func(*args, **kwargs)
            return
    def wrapper():
        return Spooler()
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