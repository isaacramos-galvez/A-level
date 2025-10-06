matches = 10
team_score = []

points = 0
total_points = 0
def points():
    y = int(input("What was the opponents score?"))
    x = int(input("What was your score?"))
    if x > y:
         points = 3
         total_points = total_points + points
    elif x == y:
         points = 1
         total_points = total_points + points
    elif x < y:
         points = 0
    print(total_points)

while matches != 0:
              points()
              matches = matches - 1