'''
如果在函数名后面放了小括号，这个函数就会被执行，然而如果不放括号在它后面，那么他就可以被到处传递，并且可以赋值给别的变量而不去执行他
'''
#! /usr/bin/env python3
from functools import wraps

class logit(object):
    def __init__(self,logfile = 'out.log'):
        self.logfile = logfile

    def __call__(self.func):
        @wraps(func)
        def my_function(*arg,**kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            #open log file and wirte
            with open(self.logfile, 'a') as opened_file:
                #open log file at special location
                opened_file.write(log_string + '\n')
                #send a message
                self.notify()
                return func(*args, **kwargs)
            return wrapped_function

    def notify(self):
        pass


class emial_logit(logit):
    '''
    send emial to administrator when call the function
    '''
    def __init__(self, email = 'dianyuh@sina.com',*args, **kwargs):
        self.email = email
        super(email_logit,self).__init__(*args,**kwargs)

    def notify(self):
         pass


