#[Challenge #178 Hard - Regular Expression Fractals](http://www.reddit.com/r/dailyprogrammer/comments/2fkh8u/9052014_challenge_178_hard_regular_expression/)

**Python 3.4**

The approach is described [here](https://imgur.com/a/QWMGi). I *really* liked this one. I'm actually amazed by the results, but also by how short my code is. I was expecting something much longer. The attribution of the quadrant numbers is based on the fact that they depend on whether the pixel's coordinates are odd or even (and to a certain extent, the quadrant-code for each pixel is based on whether it's coordinates are divisible by 2, 4, 6, 8, 16... or not).

Good fun :)

#Results:

**\[13\]\[24\]\[\^1\]\[\^2\]\[\^3\]\[\^4\]**

![](https://i.imgur.com/QwyLu6G.png)

***

**(.)\1..\1**

![](https://i.imgur.com/KRPDtla.png)

**.\*1.***

(anything that contains a 1):

![](https://i.imgur.com/1yrYlrt.png)

***

**.\*(12|23|34).***

![](https://i.imgur.com/GrWXOch.png)