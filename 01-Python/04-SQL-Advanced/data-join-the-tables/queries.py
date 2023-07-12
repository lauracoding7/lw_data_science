# pylint:disable=C0111,C0103

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    # YOUR CODE HERE
    query = """
        SELECT
            Orders.OrderID,
            Customers.ContactName,
            Employees.FirstName
        FROM Orders
        JOIN Employees ON Employees.EmployeeID = Orders.EmployeeID
        JOIN Customers ON Customers.CustomerID = Orders.CustomerID
        ORDER BY Orders.OrderID
    """
    db.execute(query)
    return db.fetchall()

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Example :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    # YOUR CODE HERE
    query = """
        SELECT
            Customers.ContactName,
            SUM(OrderDetails.UnitPrice * OrderDetails.Quantity) AS cumulative_amount
        FROM Orders
        JOIN OrderDetails On OrderDetails.OrderID = Orders.OrderID
        JOIN Customers ON Customers.CustomerID = Orders.CustomerID
        GROUP BY Customers.CustomerID
        ORDER BY cumulative_amount
    """
    db.execute(query)
    return db.fetchall()

def best_employee(db):
    '''Implement the best_employee method to determine who’s the best employee! By “best employee”,
    we mean the one who sells the most.
    We expect the function to return a tuple like:
    ('FirstName', 'LastName', 6000 (the sum of all purchase)).
    The order of the information is irrelevant'''
    # YOUR CODE HERE
    query = """
        SELECT
            Employees.FirstName,
            Employees.LastName,
            SUM(UnitPrice * Quantity) AS cumulative_amount
        FROM Employees
        JOIN Orders On Orders.EmployeeID = Employees.EmployeeID
        JOIN OrderDetails On OrderDetails.OrderID = Orders.OrderID
        GROUP BY Employees.EmployeeID
        ORDER BY cumulative_amount DESC
        LIMIT 1
    """
    db.execute(query)
    return db.fetchall()[0]

def orders_per_customer(db):
    '''Return a list of tuples where each tuple contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    # YOUR CODE HERE
    query = """
        SELECT
            Customers.ContactName,
            COUNT(Orders.OrderID) AS order_amount
        FROM Customers
        LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
        GROUP BY Customers.CustomerID
        ORDER BY order_amount ASC
    """
    db.execute(query)
    return db.fetchall()
