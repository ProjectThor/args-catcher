args-catcher
============

Simple python test helper that allows for catching arguments and asserting on them::

    from args_catcher import catch_args


    def test_1():
        args_catcher = catch_args(allow(my_view).render.and_return('some text'))
        my_view.index(...)
        context = args_catcher.args[2]
        assert 'some_key' in context

Legal
-----

This software is released under the `MIT License <https://opensource.org/licenses/MIT>`_. 
Copyright (c) 2018 siroop AG, Franco Sebregondi. 
