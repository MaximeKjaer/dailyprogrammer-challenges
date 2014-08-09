from PIL import Image, ImageDraw, ImageOps
from random import randint

n = 150

#Create image
img = Image.new( 'RGB', (101, 101), 'white')
draw = ImageDraw.Draw(img)
points = [(randint(0, 100), randint(0, 100))  for _ in range(n)]

def left(point, line):
    """Determines if a point is to the left of a line
    (http://stackoverflow.com/questions/1560492/how-to-tell-whether-a-point-is-to-the-right-or-left-side-of-a-line)
    A BIG thank-you to /u/Frichjaskla !!"""
    position = (line[1][0]-line[0][0])*(point[1]-line[0][1]) -  (line[1][1]-line[0][1])*(point[0]-line[0][0])
    return position<0

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
