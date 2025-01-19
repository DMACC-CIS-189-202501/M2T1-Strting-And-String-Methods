import ast
import pytest

# Function to count the usage of specific functions in the code
def count_function_usage(code, function_name):
    tree = ast.parse(code)
    return sum(isinstance(node, ast.Call) and getattr(node.func, 'attr', None) == function_name for node in ast.walk(tree))

# Test functions to check the usage of each specified function
def test_capitalize():
    with open('assignment.py', 'r') as file:
        code = file.read()
    assert count_function_usage(code, 'capitalize') == 1, "capitalize does not appear to be used."

def test_find():
    with open('assignment.py', 'r') as file:
        code = file.read()
    assert count_function_usage(code, 'find') == 1, "find does not appear to be used."

def test_index():
    with open('assignment.py', 'r') as file:
        code = file.read()
    assert count_function_usage(code, 'index') == 1, "index does not appear to be used."

def test_isalnum():
    with open('assignment.py', 'r') as file:
        code = file.read()
    assert count_function_usage(code, 'isalnum') == 1, "isalnum does not appear to be used."

def test_isalpha():
    with open('assignment.py', 'r') as file:
        code = file.read()
    assert count_function_usage(code, 'isalpha') == 1, "isalpha does not appear to be used."

def test_isdigit():
    with open('assignment.py', 'r') as file:
        code = file.read()
    assert count_function_usage(code, 'isdigit') == 1, "isdigit does not appear to be used."

def test_islower():
    with open('assignment.py', 'r') as file:
        code = file.read()
    assert count_function_usage(code, 'islower') == 1, "islower does not appear to be used."

def test_isupper():
    with open('assignment.py', 'r') as file:
        code = file.read()
    assert count_function_usage(code, 'isupper') == 1, "isupper does not appear to be used."

def test_isspace():
    with open('assignment.py', 'r') as file:
        code = file.read()
    assert count_function_usage(code, 'isspace') == 1, "isspace does not appear to be used."

def test_startswith():
    with open('assignment.py', 'r') as file:
        code = file.read()
    assert count_function_usage(code, 'startswith') == 1, "startswith does not appear to be used."

if __name__ == "__main__":
    pytest.main()