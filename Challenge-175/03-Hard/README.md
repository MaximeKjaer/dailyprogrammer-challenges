#[Challenge #175 Hard - Simulation of a laser in a hall of mirrors](http://www.reddit.com/r/dailyprogrammer/comments/2dmdwo/8152014_challenge_175_hard_hall_of_mirror/)

**Python 3.4**

*Dependencies*

- PIL
- Shapely

This was perhaps the hardest challenge so far for me. My solution isn't exactly elegant or extremely efficient - to be fair, I didn't even solve the challenge as it is stated (with manual inputs)!! (though I'll do it later).
I've set it up to randomly place 400 mirrors on a 1000x1000 grid, shoot a laser off, and see where it ends (with a given distance, defaulted to 50 000).

#Ouput

**Distance: 50 000 (with normal vectors)**

![](http://i.imgur.com/v2OKXIY.png)

Black lines are mirrors, red line is the laser, green lines are the normal vectors to the mirrors.


***

**Distance: 50 000**

![](http://i.imgur.com/hZXP518.png)

Green dot is the starting point, red dot is the end.

***

**And a last one**
![](http://i.imgur.com/unGzPzn.png)
