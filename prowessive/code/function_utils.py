def create_function(function_name, function_arguments, function_code):
    function_string = f"def {function_name}({function_arguments}): {function_code}"
    exec(function_string)
    return_value = eval(function_name)
    return return_value

