#PARAMS

Primary = ["Ön", "Arka", "Kol","Sağ Kol","Sol Kol","Sağ Ön","Sol Ön","Kapüşon"] # Parts that can be easily started by operators
NonPrimary = ["Yaka","Biye","Bant"] # Parts that cannot be started easily by operators

Threshold = 8*60 # If a machine starts producing an alternative part, it and any machine prodcuing that part should continue operating for at least this duration.
# This threshold avoids changing fibers if machine will work shortly and after that changing fiber may needed.


N = 3  # How many alternative do you want to see


"""
Helper Functions
"""




def isPrimary(di):
    """
    Checks if the 'Part' component of the dictionary is considered primary.

    Args:
    di (dict): A dictionary representing an element in an order_list or machine_list.
               It must contain a 'Part' key.

    Returns:
    bool: True if the 'Part' value in the dictionary is in the Primary list, False otherwise.
    """
    if di["Part"] in Primary:
        return True
    return False


def orderListSeperator(order_list):
    """
    Separates an order list into primary and non-primary parts and removes completed orders.

    Args:
    order_list (list): A list of dictionaries where each dictionary represents an order.
                       Each dictionary must contain 'Part' and 'finished' keys.

    Returns:
    tuple: A tuple containing two lists:
           - The first list contains orders with primary parts that are still active (not finished).
           - The second list contains orders with non-primary parts that are still active.
    """
    active_product_primary_list = []
    active_product_nonprimary_list = []

    for i in order_list:
        if i["finished"] == False:
            if isPrimary(i):
                active_product_primary_list.append(i)
            else:
                active_product_nonprimary_list.append(i)

    return (active_product_primary_list, active_product_nonprimary_list)


def isOrderSame(dict1,dict2):
    """
    Checks if two dictionaries have the same 'Order' value.

    Args:
    dict1 (dict): A dictionary representing an element in an order_list or machine_list.
                  It must contain an 'Order' key.
    dict2 (dict): Another dictionary representing an element in an order_list or machine_list.
                  It must also contain an 'Order' key.

    Returns:
    bool: True if both dictionaries have the same 'Order' value, False otherwise.
    """
    if dict1["Order"] == dict2["Order"]:
        return True
    return False

def isArticleSame(dict1,dict2):
    """
    dict1 (dictionary): one of the element (dictionary) in order_list or machine_list
    dict2 (dictionary): one of the element (dictionary) in order_list or machine_list 

    if dict1's and dict2's article components are the same than it returns True
    False otherwise
    """
    if dict1["Article"] == dict2["Article"]:
        return True
    return False


def isColorSame(dict1,dict2):
    """
    dict1 (dictionary): one of the element (dictionary) in order_list or machine_list
    dict2 (dictionary): one of the element (dictionary) in order_list or machine_list 

    if dict1's and dict2's color components are the same than it returns True
    False otherwise
    """
    if dict1["Color"] == dict2["Color"]:
        return True
    return False

def isSizeSame(dict1,dict2):
    """
    dict1 (dictionary): one of the element (dictionary) in order_list or machine_list
    dict2 (dictionary): one of the element (dictionary) in order_list or machine_list 

    if dict1's and dict2's size components are the same than it returns True
    False otherwise
    """
    if dict1["Size"] == dict2["Size"]:
        return True
    return False

def isPartSame(dict1,dict2):
    """
    dict1 (dictionary): one of the element (dictionary) in order_list or machine_list
    dict2 (dictionary): one of the element (dictionary) in order_list or machine_list 

    if dict1's and dict2's part components are the same than it returns True
    False otherwise
    """
    if dict1["Part"] == dict2["Part"]:
        return True
    return False


def orderAndArticleSame(dict1,dict2):
    """
    dict1 (dictionary): one of the element (dictionary) in order_list or machine_list
    dict2 (dictionary): one of the element (dictionary) in order_list or machine_list 

    if dict1's and dict2's order and article components are the same than it returns True
    False otherwise
    """
    if isOrderSame(dict1,dict2) and isArticleSame(dict1,dict2):
        return True
    return False
   


def isSame(dict1,dict2):
    """
    dict1 (dictionary): one of the element (dictionary) in order_list or machine_list
    dict2 (dictionary): one of the element (dictionary) in order_list or machine_list 

    if dict1's and dict2's all components (Same order, article, color, size and part) are the same than it returns True
    False otherwise
    """
    if isOrderSame(dict1,dict2) and isArticleSame(dict1,dict2) and isColorSame(dict1,dict2) and isSizeSame(dict1,dict2) and isPartSame(dict1,dict2):
        return True
    return False



def exceptPart(dict1,dict2):
    """
    dict1 (dictionary): one of the element (dictionary) in order_list or machine_list
    dict2 (dictionary): one of the element (dictionary) in order_list or machine_list 

    if dict1's and dict2's all components except part (Same order, article, color, size ) are the same than it returns True
    False otherwise
    """
    if isOrderSame(dict1,dict2) and isArticleSame(dict1,dict2) and isColorSame(dict1,dict2) and isSizeSame(dict1,dict2) and not isPartSame(dict1,dict2):
        return True
    return False


def exceptSize(dict1,dict2):
    """
    dict1 (dictionary): one of the element (dictionary) in order_list or machine_list
    dict2 (dictionary): one of the element (dictionary) in order_list or machine_list 

    if dict1's and dict2's order, article, and color componenets are the same and ensures size is different from each other than it returns True
    False otherwise
    """
    if isOrderSame(dict1,dict2) and isArticleSame(dict1,dict2) and isColorSame(dict1,dict2) and not isSizeSame(dict1,dict2) :
        return True
    return False


def exceptColor(dict1,dict2):
    """
    dict1 (dictionary): one of the element (dictionary) in order_list or machine_list
    dict2 (dictionary): one of the element (dictionary) in order_list or machine_list 

    if dict1's and dict2's order and article components are the same and exures that color is different from each other than it returns True
    False otherwise
    """
    if isOrderSame(dict1,dict2) and isArticleSame(dict1,dict2) and not isColorSame(dict1,dict2):
        return True
    return False

def numberOfMachine(di,machines):
    """
    di (dictionary): one of the element (dictionary) in order_list or machine_list
    machines (list): machine_list (includes dictionaries representing the machines)

    Counts How many machines are currently working on product Di
    """
    result = 0
    for i in machines:
        if isSame(i,di):
            result +=1
    return result





def totalTime(order):
    """
    order (dictionary): one of the element (dictionary) in order_list

    """
    return order["Total_Time_Needed"]


def duplicateChecker(order):
    k = 0
    for i in range(len(order)):
        for j in range(len(order)):
            if i == j:
                continue
            if isSame(order[i],order[j]):
                k += 1

    if k > 0:
        print("Warning: There is Duplicate in your orders! ")
        return False
    else:
        print("Approved: No Duplcate Found! ")

    return True




"""
Threshold-Based Machine Activation Condition:

If code includes following:
(numberOfMachine(i,machines) == 0 or i["Total_Time_Needed"]/(numberOfMachine(i,machines)+1) >= Threshold) 

It means that if no machines are currently working, a machine can be started. However, 
if at least one machine is already working, a new one can be started only if both machines will be active for more than the Threshold.


"""
def findPartDiff(di,orders, machines):
    """
    di (dictionary): one of the element (dictionary) in order_list or machine_list
    order_list (list): List of orders (orders are dictionary)
    machines (list): machine_list (includes dictionaries representing the machines)

    returns a list of orders that are the same with di except for "Part" component if these orders obey Threshold-Based Machine Activation Condition
    """
    result = []
    for i in orders:
        if exceptPart(di,i) and (numberOfMachine(i,machines) == 0 or i["Total_Time_Needed"]/(numberOfMachine(i,machines)+1) >= Threshold):
            result.append(i)
    
    return result


def findSizeDiff(di,orders, machines):
    """
    di (dictionary): one of the element (dictionary) in order_list or machine_list
    order_list (list): List of orders (orders are dictionary)
    machines (list): machine_list (includes dictionaries representing the machines)

    returns a list of orders that have same Order (componenet), Article, Color and different Size component if these orders obey Threshold-Based Machine Activation Condition
    """
    result = []
    for i in orders:
        if exceptSize(di,i) and (numberOfMachine(i,machines) == 0 or i["Total_Time_Needed"]/(numberOfMachine(i,machines)+1) >= Threshold):
            result.append(i)

    return result



def findColorDiffActive(di,orders, machines):
    """
    di (dictionary): one of the element (dictionary) in order_list or machine_list
    order_list (list): List of orders (orders are dictionary)
    machines (list): machine_list (includes dictionaries representing the machines)

    returns a list of orders that have same Order (componenet), Article and different Color component  AND Number of Machine working on these order is bigger than 0 if this orders obey Threshold-Based Machine Activation Condition
    """
    result = []
    for i in orders:
        if exceptColor(di,i) and  i["Total_Time_Needed"]/(numberOfMachine(i,machines)+1) >= Threshold and numberOfMachine(i,machines) > 0:
            result.append(i)

    return result


def findColorDiffNotActive(di,orders, machines):
    """
    di (dictionary): one of the element (dictionary) in order_list or machine_list
    order_list (list): List of orders (orders are dictionary)
    machines (list): machine_list (includes dictionaries representing the machines)

    returns a list of orders that have same Order (componenet), Article and different Color component  AND Number of Machine working on these order is 0
    """
    result = []
    for i in orders:
        if exceptColor(di,i)  and numberOfMachine(i,machines) == 0:
            result.append(i)

    return result


def findSameOrderActive(di,orders, machines):
    """
    di (dictionary): one of the element (dictionary) in order_list or machine_list
    order_list (list): List of orders (orders are dictionary)
    machines (list): machine_list (includes dictionaries representing the machines)

    returns a list of orders that have same Order (componenet), different Article AND Number of Machine working on this order is bigger than 0 if these orders obey Threshold-Based Machine Activation Condition
    """
    result = []
    for i in orders:
        if isOrderSame(di,i) and not isArticleSame(di,i) and i["Total_Time_Needed"]/(numberOfMachine(i,machines)+1) >= Threshold and numberOfMachine(i,machines) > 0:
            result.append(i)

    return result


def findSameOrderNotActive(di,orders, machines):
    """
    di (dictionary): one of the element (dictionary) in order_list or machine_list
    order_list (list): List of orders (orders are dictionary)
    machines (list): machine_list (includes dictionaries representing the machines)

    returns a list of orders that have same Order (componenet), different Article AND Number of Machine working on these order is 0
    """
    result = []
    for i in orders:
        if isOrderSame(di,i) and not isArticleSame(di,i) and numberOfMachine(i,machines) == 0:
            result.append(i)

    return result


def findDiffOrderActive(di,orders,machines):
    """
    di (dictionary): one of the element (dictionary) in order_list or machine_list
    order_list (list): List of orders (orders are dictionary)
    machines (list): machine_list (includes dictionaries representing the machines)

    returns a list of orders that have different Order (componenet), different Article AND Number of Machine working on this order is bigger than 0 if these orders obey Threshold-Based Machine Activation Condition
    """
    result = []
    for i in orders:
        if not isOrderSame(di,i) and not isArticleSame(di,i) and i["Total_Time_Needed"]/(numberOfMachine(i,machines)+1) >= Threshold and numberOfMachine(i,machines) > 0:
            result.append(i)

    return result



def findDiffOrderNotActive(di,orders,machines):
    """
    di (dictionary): one of the element (dictionary) in order_list or machine_list
    order_list (list): List of orders (orders are dictionary)
    machines (list): machine_list (includes dictionaries representing the machines)

    returns a list of orders that have different Order (componenet), different Article AND of Machine working on these order is 0
    """
    result = []
    for i in orders:
        if not isOrderSame(di,i) and not isArticleSame(di,i) and numberOfMachine(i,machines) == 0:
            result.append(i)

    return result



def findSizeDiffSamePart(di,orders, machines):
    """
    di (dictionary): one of the element (dictionary) in order_list or machine_list
    order_list (list): List of orders (orders are dictionary)
    machines (list): machine_list (includes dictionaries representing the machines)

    returns a list of orders that its components are the same with di except for "Size" component if these orders obey Threshold-Based Machine Activation Condition
    """
    result = []
    for i in orders:
        if exceptSize(di,i) and isPartSame(di,i) and (numberOfMachine(i,machines) == 0 or i["Total_Time_Needed"]/(numberOfMachine(i,machines)+1) >= Threshold):
            result.append(i)

    return result



def findColorDiffActiveSamePart(di,orders, machines):
    """
    di (dictionary): one of the element (dictionary) in order_list or machine_list
    order_list (list): List of orders (orders are dictionary)
    machines (list): machine_list (includes dictionaries representing the machines)

    returns a list of orders that its components are the same with di except for "Color" component AND Number of Machine working on this order is bigger than 0 if these orders obey Threshold-Based Machine Activation Condition
    """
    result = []
    for i in orders:
        if exceptColor(di,i) and isPartSame(di,i) and i["Total_Time_Needed"]/(numberOfMachine(i,machines)+1) >= Threshold and numberOfMachine(i,machines) > 0:
            result.append(i)

    return result


def findColorDiffNotActiveSamePart(di,orders, machines):
    """
    di (dictionary): one of the element (dictionary) in order_list or machine_list
    orders (list): List of orders (orders are dictionary)
    machines (list): machine_list (includes dictionaries representing the machines)

    returns a list of orders that its components are the same with di except for "Color" component AND of Machine working on these order is 0
    """
    result = []
    for i in orders:
        if exceptColor(di,i)  and isPartSame(di,i) and numberOfMachine(i,machines) == 0:
            result.append(i)

    return result



def combineMachineWithOrders(orders, machine_list):

    """
    Combines a list of orders with a list of machines based on matching attributes.

    orders (list): List of orders (orders are dictionary)
    machines (list): machine_list (includes dictionaries representing the machines)

    Returns:
    list: A list of combined dictionaries. Each dictionary represents an order 
          with its corresponding machine data merged in. If an order has a corresponding machine,
          the machine data is included in the resulting dictionary.
    """
    # Convert machine list to a dictionary for faster lookup

    machine_dict = {}
    for machine in machine_list:
        key = (machine['Order'], machine['Article'], machine['Color'], machine['Size'], machine['Part'])
        machine_dict[key] = machine
    
    # Combine the machine list with corresponding orders
    combined_list = []
    for order in orders:
        key = (order['Order'], order['Article'], order['Color'], order['Size'], order['Part'])
        if key in machine_dict:
            # Merge the order data into the machine dictionary
            combined_machine = {**order ,**machine_dict[key] }
            combined_list.append(combined_machine)
    
    return combined_list



def groupByBant(combinedList):
    """
    Groups a list of combined order and machine dictionaries by the 'Bant' key.

    Args:
    combinedList (list): A list of dictionaries where each dictionary contains
                         information about an order and its corresponding machine.
                         Each dictionary must include the 'Bant' key.

    Returns:
    dict: A dictionary where the keys are unique 'Bant' values, and the values
          are lists of dictionaries (items from combinedList) that belong to that 'Bant'.
    """


    grouped_by_bant = {}
    for item in combinedList:
        bant = item['Bant']
        if bant not in grouped_by_bant:
            grouped_by_bant[bant] = []
        grouped_by_bant[bant].append(item)
    return grouped_by_bant



def averageMinByBant(groupedByBantList):
    """
    Calculates the average 'time' for each 'Bant' group.

    Args:
    groupedByBantList (dict): A dictionary where each key is a 'Bant' value and 
                              each value is a list of dictionaries that belong to that 'Bant'.
                              Each dictionary in the list must contain a 'time' key representing minutes.

    Returns:
    dict: A dictionary where each key is a 'Bant' value and each value is the average 'time' 
          (in minutes) for that 'Bant', rounded to 2 decimal places.
    """

    average_by_bant = {}
    for bant, items in groupedByBantList.items():
        total_time = sum(item['time'] for item in items)
        average_time = total_time / len(items) if items else 0
        average_by_bant[bant] = round(average_time, 2)  # Rounded to 2 decimal places
    return average_by_bant
