import sqlite3 as sql

connection = sql.connect('Task List Data Base.db')
class To_Do_List():
    def __init__(self, TaskID, Description, Completed, Subject, DueDate, DateCreated, DateCompleted, TaskName):
        self.TaskID = TaskID
        self.Description = Description
        self.Completed = Completed
        self.Subject = Subject
        self.DueDate = DueDate
        self.DateCreated = DateCreated
        self.DateCompleted = DateCompleted
        self.TaskName = TaskName

    

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