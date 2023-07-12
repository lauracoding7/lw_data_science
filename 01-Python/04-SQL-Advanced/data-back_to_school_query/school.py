# pylint:disable=C0111,C0103

def students_from_city(db, city):
    """return a list of students from a specific city"""
    # YOUR CODE HERE
    query = """
        SELECT *
        FROM students
        WHERE birth_city = ?
    """
    db.execute(query, (city,)) # argument needs to be passed as a tuple
    students = db.fetchall()
    return students


# To test your code, you can **run it** before running `make`
#   => Uncomment the following lines + run:
# python school.py

# import sqlite3
# conn = sqlite3.connect('data/school.sqlite')
# db = conn.cursor()
# print(students_from_city(db, 'Paris'))
