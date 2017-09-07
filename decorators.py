# def make_html_p(function, *args, **kwargs):
#     def inner(args):
#         return '<p> {} </p>'.format(function(args))
#     return inner
#
# @make_html_p
# def print_body(body):
#     return body
#
## @make_html_p
# def print_other(stuff):
#     return stuff
#
# print(print_body('this is a message'))
# print(print_other('this is another message'))


# def make_multiplier_of(n):
#     def multiplier(x):
#         return x * n
#
#     return multiplier
#
# times3 = make_multiplier_of(3)
# times5 = make_multiplier_of(5)
#
# print(times3(9))


# # Lab: Decorators
#
# ##### Goal
#
# Write a Python Decorator that will tell us how long a function took to execute.
#
# ##### Instructions
#
# Use pythons time module to calculate the time it took a function to execute.

# write parent function
# write child function
# use decorator to call child function outside of parent function
# get (print) time before and after function runs
# subtract start time from end time to get duration


import time

# start counting time before function runs
timer_zero = time.clock()
# print(timer_zero)

# function must take longer than zero nothingths of a second to process >:[
def make_html_p(function, *args, **kwargs):
    def inner(args):
        return '<p> {} </p>'.format(function(args))
    return inner

@make_html_p
def print_body(body):
    return body

@make_html_p
def print_other(stuff):
    return stuff

print(print_body('this is a message'))
print(print_other('this is another message'))

# print(time.clock())
print(time.clock() - timer_zero, "seconds process time")




