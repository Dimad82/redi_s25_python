import json
from mysql.connector import connect, Error

# Load the JSON file
with open('movies.json', 'r') as file:
    movies = json.load(file)

try:
    with connect(
            host="localhost",
            user="root",
            password="admin",
            database="online_movie_rating",) as connection:
        with connection.cursor() as cursor:
            insert_movies_query = """
            INSERT INTO movies (title, release_year, genre, collection_in_mil)
            VALUES (%s, %s, %s, %s);
            """
            for movie in movies:
                print()
                cursor.execute(insert_movies_query, (movie['title'], movie['release_year'], movie['genre'], movie['collection_in_mil']))
            connection.commit()
        print(connection)
except Error as e:
    print(e)