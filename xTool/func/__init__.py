#coding: utf-8

import inspect


def catch(func):
    """确保函数执行不会抛出异常
    Wrap the function to make sure that it doesn't raise any exception. Return wrapper function.
    Wrapper function accepts arguments and passes it to the wrapped function by calling it.
    If wrapped function raises an exception, exception will be returned by the wrapper.
    If wrapped function reuturns a value, wrapper will return an object of catch. ReturnValue
    type. Such object contains `value` member which provides value returned by the wrapped function.
    """
    class ReturnValue:
        def __init__(self, value):
            self.value = value
    catch.ReturnValue = ReturnValue

    def wrapper(*args, **kwargs):
        try:
            ret = func(*args, **kwargs)
            return ReturnValue(ret)
        except Exception as ex:
            return ex
    return wrapper