

# A simple function

def simple_function():

    print("Inside the simple function")
    return 0



def function_with_parameter(name) :

    print ("Name is %s" % name)
    return


def function_with_default_parameter(id, algorithm="gini"):

    print ("ID and name is %s and %s" % (id, algorithm))
    return

def function_with_var_args(*arguments):

    first_param, second_param = arguments
    #print(arguments)

    for each in arguments:
        print each

    return


print(simple_function())
function_with_parameter("Gini Impurity")
function_with_default_parameter(101)
function_with_default_parameter(102,"logarithmic")
function_with_var_args("arg1","arg2","arg3")