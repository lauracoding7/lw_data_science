# pylint:disable=C0111,C0103

def order_rank_per_customer(db):
    # YOUR CODE HERE
    query = """
    SELECT
	    Orders.OrderID,
	    Customers.CustomerID,
	    OrderDate,
	    RANK() OVER (
		    PARTITION BY Orders.CustomerID
		    ORDER BY OrderDate
	    ) AS OrderRank
    FROM Customers
    JOIN Orders ON Orders.CustomerID = Customers.CustomerID

    """
    db.execute(query)
    return db.fetchall()

def order_cumulative_amount_per_customer(db):
    # YOUR CODE HERE
    query = """
        SELECT
            Orders.OrderID,
            Orders.CustomerID,
            Orders.OrderDate,
            SUM(SUM(OrderDetails.UnitPrice * OrderDetails.Quantity)) OVER (
                PARTITION BY Orders.CustomerID
                ORDER BY Orders.OrderDate
            ) AS OrderCumulativeAmount
        FROM Orders
        JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
        GROUP BY Orders.OrderID
        ORDER BY Orders.CustomerID
    """
    # the total amount for a given order -> aggregation function (inner SUM & Groupby)
    # the cumulative amount of orders -> window function (outer SUM & Partition)
    db.execute(query)
    return db.fetchall()
