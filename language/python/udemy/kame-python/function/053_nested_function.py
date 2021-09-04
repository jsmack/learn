msg = "I am global"

def outer(outer_param):
    msg = "I am outer"

    def inner():
        msg = "I am inner"
        print("This is inner function.")

        # outer param access is allowed
        print(outer_param)
        # outer arg

        inner_variable = "inner var"

        print(msg)
        # I am inner


    print("This is outer function.")
    # inner_variable is no accessed
    # print(inner_variable)
    inner()
    print(msg)
    # I am outer



outer("outer arg")
# inner()
print(msg)
# I am global
