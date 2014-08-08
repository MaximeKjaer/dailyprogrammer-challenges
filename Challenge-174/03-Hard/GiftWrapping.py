from PIL import Image, ImageDraw, ImageOps
from random import randint

n = 26

#Create image
img = Image.new( 'RGB', (101, 101), 'white')
draw = ImageDraw.Draw(img)
points = [(randint(0, 100), randint(0, 100))  for _ in range(n)]

def left(point, line):
    """Determines if a point is to the left of a line"""
    x, y = point[0], point[1]
    #DETERMINE SLOPE
    if line[1][0] - line[0][0] != 0: #If it isn't vertical
        slope = (line[1][1] - line[0][1]) / (line[1][0] - line[0][0])
        y_intercept = line[0][1] - slope*line[0][0]
    else:
        slope = 'vertical'
    #DETERMINE IF IT IS TO THE LEFT
    if line[0][0] > line[1][0]: #If the line goes from left to right, then check if the point is above
        return y > slope*x + y_intercept
    elif line[0][0] < line[1][0]: #If it goes from right to left, then check if the point is below
        return y < slope*x + y_intercept
    elif slope == 'vertical' and line[0][1] > line[1][1]: #If it goes from up to down then check if the point is to the right
        return x > line[0][1]
    elif slope == 'vertical' and line[0][1] < line[1][1]: #If it goes from down to up, then check if the point is to the left
        return x < line[0][1]


def jarvis(S):
    pointOnHull = min(S)
    i = 0
    endpoint = ''
    P = [0]
    while endpoint != P[0]:
        if P == [0]:
            P[0] = pointOnHull
        else:
            P.append(pointOnHull)
        endpoint = S[0]
        for j in range(1, len(S)):
            line = [P[i], endpoint]
            if (endpoint == pointOnHull) or left(S[j], line):
                endpoint = S[j]
        i += 1
        pointOnHull = endpoint
    return P

P = jarvis(points)

draw.polygon(P, outline='red')
draw.point(points, fill="black")
img = img.resize((500, 500))
img = ImageOps.flip(img)
img.save('hull.png', 'PNG')
