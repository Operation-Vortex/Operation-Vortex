
x = 'global'

def outer_function():
    x = 'Enclosing'

    def inner_function():
        print(f"Inner function: {x}")

    inner_function()
    print(f"Outer function: {x}")

outer_function()
print(f"Global scope: {x}")