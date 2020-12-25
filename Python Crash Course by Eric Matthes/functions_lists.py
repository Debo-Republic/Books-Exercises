# Working with functions to decentralise the utility across modules
# Simulating execution of print jobs
# One function One Job Rule 

def fire_print(requested_print, completed_print):
    """Function that executes print jobs for requested models """
    while requested_print:
        current_print = requested_print.pop()
        print(f"\n Currently printing {current_print}")
        completed_print.append(current_print)
    return completed_print


def show_completed_task(completed_print):
    """Function that shows all the models that have successfully printed. """
    for item in completed_print:
        print(f"\n {item} has been successfully printed.")


requested_print = ['Samsung Galaxy S9', 'Apple Iphone XS', 'Redmi challenges']
completed_print = []
completed_print = fire_print(requested_print, completed_print)
show_completed_task(completed_print)
