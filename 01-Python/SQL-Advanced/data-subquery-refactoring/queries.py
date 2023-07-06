# pylint:disable=C0111,C0103

def get_average_purchase(db):
    # return the average amount spent per order for each customer ordered by customer ID
    # YOUR CODE HERE
    query = """
        WITH AmountPerOrder AS (SELECT
            Orders.OrderID,
            Orders.CustomerID,
            SUM(OrderDetails.UnitPrice * OrderDetails.Quantity) AS Amount
        FROM Orders
        JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
        GROUP BY Orders.OrderID
        )

        SELECT
            CustomerID,
            ROUND(AVG(Amount), 2) AS AverageOrderedAmount
        FROM AmountPerOrder
        GROUP BY CustomerID
        ORDER BY CustomerID
    """
    db.execute(query)
    return db.fetchall()

def get_general_avg_order(db):
    # return the average amount spent per order
    # YOUR CODE HERE
    query = """
        WITH AmountPerOrder AS (SELECT
		    SUM(OrderDetails.UnitPrice * OrderDetails.Quantity) AS Amount
        FROM OrderDetails
        GROUP BY OrderDetails.OrderID
        )

        SELECT
	        AVG(Amount) AS GeneralAvg
        FROM AmountPerOrder
    """
    db.execute(query)
    return db.fetchone()[0]

def best_customers(db):
    # return the customers who have an average purchase greater than the general average purchase
    # YOUR CODE HERE
    query = """
        WITH AmountPerOrder AS (
            SELECT
                Orders.OrderID,
                Orders.CustomerID,
                SUM(OrderDetails.UnitPrice * OrderDetails.Quantity) AS Amount
            FROM Orders
            JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
            GROUP BY Orders.OrderID
        ),
        GeneralOrderAvg AS (
            SELECT ROUND(AVG(Amount), 2) AS GeneralAvg
            FROM AmountPerOrder
        )
        SELECT
	        AmountPerOrder.CustomerID,
	        ROUND(AVG(AmountPerOrder.Amount), 2) AS AverageOrderedAmount
        FROM AmountPerOrder
        GROUP BY AmountPerOrder.CustomerID
        HAVING AverageOrderedAmount > (SELECT GeneralAvg FROM GeneralOrderAvg)
        ORDER BY AverageOrderedAmount DESC
    """
    db.execute(query)
    return db.fetchall()

def top_ordered_product_per_customer(db):
    # return the list of the top ordered product by each customer
    # based on the total ordered amount in USD
    # YOUR CODE HERE
    query = """
    WITH OrderedProducts AS (
        SELECT
            CustomerID,
            ProductID,
            SUM(OrderDetails.Quantity * OrderDetails.UnitPrice) AS ProductValue
        FROM OrderDetails
        JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
        GROUP BY Orders.CustomerID, OrderDetails.ProductID
        ORDER BY ProductValue DESC
        ),

        Ranks AS (
            SELECT
                OrderedProducts.CustomerID,
                OrderedProducts.ProductID,
                OrderedProducts.ProductValue,
                RANK() OVER(
                    PARTITION BY OrderedProducts.CustomerID
                    ORDER BY OrderedProducts.ProductValue DESC)
                AS OrderRank
            FROM OrderedProducts
    )
    SELECT
        Ranks.CustomerID,
        Ranks.ProductID,
        Ranks.ProductValue
    FROM Ranks
    WHERE Ranks.OrderRank = 1
    ORDER BY Ranks.ProductValue DESC
    """
    db.execute(query)
    return db.fetchall()

def average_number_of_days_between_orders(db):
    # return the average number of days between two consecutive orders of the same customer
    pass  # YOUR CODE HERE
