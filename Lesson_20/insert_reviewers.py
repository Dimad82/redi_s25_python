import json
from mysql.connector import connect, Error

# Load the JSON file
with open('reviewers.json', 'r') as file:
    reviewers = json.load(file)

try:
    with connect(
            host="localhost",
            user="root",
            password="admin",
            database="online_movie_rating",) as connection:
        with connection.cursor() as cursor:
            insert_reviewers_query = """
            INSERT INTO reviewers
                (first_name, last_name)
                VALUES ( %s, %s )
            """
            for reviewer in reviewers:
                cursor.execute(insert_reviewers_query, (reviewer['first_name'], reviewer['last_name']))
            connection.commit()
        print(connection)
except Error as e:
    print(e)