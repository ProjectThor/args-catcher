class ArgumentCatcher:
    """
    Can be used together with test doubles to assert on expected arguments in hindsight.
    This can be useful for asserting certain args on method calls with complex arguments,
    i.e. render method with complex context structure.

    Usage:
        args_catcher = ArgumentCatcher()
        allow(my_view).render.and_return_result_of(args_catcher.catch_args)
        my_view.index(...)
        context = args_catcher.args[2]
        assert 'some_key' in context
    """

    def __init__(self, return_value=lambda: None):
        self.args = None
        self.kwargs = None
        self.return_value = return_value

    def catch_args(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return self.return_value()

    def __str__(self):
        return f"<ArgumentCatcher caught args={self.args}, kwargs={self.kwargs}>"


def catch_args(allowance):
    """
    Convenience method to use ArgumentCatcher. Wrop your allow call with args_catcher(..)

    Usage:

        args_catcher = catch_args(allow(my_view).render.and_return('some text'))
        my_view.index(...)
        context = args_catcher.args[2]
        assert 'some_key' in context
    """
    args_catcher = ArgumentCatcher(allowance._return_value)
    allowance.and_return_result_of(args_catcher.catch_args)
    return args_catcher
