from prowessive.code.function_utils import create_function


class TestFunctionUtils:

    def test_create_function(self):
        name = 'my_func'
        arguments = 'name'
        code = 'return f"Hello, {name}!"'
        myfunc = create_function(name, arguments, code)
        return_value = myfunc('John Doe')
        assert return_value == "Hello, John Doe!"
