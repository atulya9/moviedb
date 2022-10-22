import sqlite3

with sqlite3.connect('movies.db') as conn:
    # Creating empty table
    cursor_obj = conn.cursor()
    cursor_obj.execute("DROP TABLE IF EXISTS movies")

    # Creating columns in the table
    table = """ CREATE TABLE movies (
        id INT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        poster_path VARCHAR(255) NOT NULL,
        language VARCHAR(255) NOT NULL,
        overview VARCHAR(255) NOT NULL,
        release_date VARCHAR(255) NOT NULL
    );"""

    cursor_obj.execute(table)
    print("Table Created")

    # Adding values to the table
    cursor_obj.execute('''INSERT INTO movies VALUES(1, 'The Shawshank Redemption', 'https://www.imdb.com/title/tt0111161/mediaviewer/rm10105600/', 'English', 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', '22 September 1994')''')
    cursor_obj.execute('''INSERT INTO movies VALUES(2, 'The Godfather', 'https://www.imdb.com/title/tt0111161/mediaviewer/rm746868224/', 'English', 'The aging patriarch of an organized crime dynasty in postwar New York City transfers control of his clandestine empire to his reluctant youngest son.', '14 March 1972')''')
    cursor_obj.execute('''INSERT INTO movies VALUES(3, 'The Dark Knight', 'https://www.imdb.com/title/tt0111161/mediaviewer/rm4023877632/', 'English', 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.', '14 July 2008')''')
    cursor_obj.execute('''INSERT INTO movies VALUES(4, '12 Angry Men', 'https://www.imdb.com/title/tt0111161/mediaviewer/rm2927108352/', 'English', 'The jury in a New York City murder trial is frustrated by a single member whose skeptical caution forces them to more carefully consider the evidence before jumping to a hasty verdict.', '10 April 1957')''')

    print('Data inserted in table: ')
    data = cursor_obj.execute('''SELECT * FROM movies''').fetchall()
    for row in data:
        print(row)

    conn.commit()




