import sqlite3 as sql
""" connection = sql.connect('chinook.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM customers")
for row in cursor:
    print(row)

connection.commit()
connection.close()"""




# connection = sql.connect('chinook.db')
# name = input("Enter a name: ")
# query = """ 
# Select Title From albums
# Where albums.Title LIKE ?"""
# params =  ('%'+name+'%',)
# print(query, params)
# print('\nResults found: \n----------')
# cursor = connection.cursor()
# cursor.execute(query, params)
# for row in cursor:
#     print(f'{row[0]}:')

connection = sql.connect('chinook.db')
artists = input("Enter an artist: ")
query = """ 
select artists.Name as 'Artists Name' , albums.Title as 'Album Title'
FROM artists
join albums on artists.ArtistId = albums.ArtistId
where artists.Name LIKE ?
group by artists.Name"""
params =  ('%'+artists+'%',)
print(query, params)
print('\nResults found: \n----------')
cursor = connection.cursor()
cursor.execute(query, params)
for row in cursor:
    print(f'{row[0]}:, {row[1]}')
