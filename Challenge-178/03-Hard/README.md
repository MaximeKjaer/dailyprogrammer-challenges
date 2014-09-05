#[Challenge #178 Hard - Regular Expression Fractals](http://www.reddit.com/r/dailyprogrammer/comments/2fkh8u/9052014_challenge_178_hard_regular_expression/)

**Python 3.4**

The approach is described [here](https://imgur.com/a/QWMGi). I'm actually amazed by the results of this one. It was good fun :)

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