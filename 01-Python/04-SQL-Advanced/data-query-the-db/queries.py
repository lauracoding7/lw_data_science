# pylint:disable=C0111,C0103

def query_orders(db):
    # return a list of orders displaying each column
    # YOUR CODE HERE
    query = """
        SELECT *
        FROM Orders
        ORDER BY OrderID
    """
    db.execute(query)
    return db.fetchall()

def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)
    # YOUR CODE HERE
    query = """
        SELECT *
        FROM Orders
        WHERE OrderDate > ? AND OrderDate <= ?
    """
    db.execute(query, (date_from, date_to))
    return db.fetchall()

def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    # YOUR CODE HERE
    query = """
        SELECT *, (JULIANDAY(ShippedDate) - JULIANDAY(OrderDate)) AS WaitingTime
        FROM Orders
        ORDER BY WaitingTime
    """
    db.execute(query)
    return db.fetchall()

# import sqlite3
# conn = sqlite3.connect('data/ecommerce.sqlite')
# db = conn.cursor()
# print(query_orders(db))
