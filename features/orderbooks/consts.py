# Consts for Orderbooks

# Maximum timeout allowed before launching exception
MAX_WAIT_TIME = 5

# Flag messages to determinate the final situation of a routine
FINISHED_WITH_SUCCESS = True
FINISHED_WITH_ERROR = False

# Time (in hours) that a record will be stored before deletion
# Used in features/orderbooks/tasks/delete_order_books()
DELETE_TIME = 48

# Time (in hours) that a record will be recovered to then be used on a graph
# Used in features/orderbooks/view/RequestOrderBookGraphView
RECOVER_TIME = 24
