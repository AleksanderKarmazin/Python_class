def my_f ():
    	print ( 'I am function')

my_f ()
def to_test():
    print ( 'Function is object', isinstance(my_f,object))

to_test ()
test = my_f 

test ()
test ()
test ()
test ()

my_list = []
my_list.append(my_f)
print(my_list)

print (callable(my_list), callable(my_f), callable(test), callable(to_test))

my_f()


def return_min_function():
    return min

test = return_min_function()
min_value = test(4, 5, -9, 12)
print('Min values is', min_value)
