#[Challenge #178 Intermediate - Jumping through Hyperspace](http://www.reddit.com/r/dailyprogrammer/comments/2fe72z/9032014_challenge_178_intermediate_jumping/)

**Python 3.4**

#I/O

    How much fuel do we have? 5 
    Planet: D
    To: A-C-D (using 2 fuel)
    Back: D-B-A (using 3 fuel)


***

    How much fuel do we have? 8
    Planet: E
    To: A-C-E (using 3 fuel)
    Back: E-D-B-A (using 5 fuel)

***

    How much fuel do we have? 16
    Planet: J
    To: A-C-D-G-J (using 5 fuel)
    Back: J-I-F-D-B-A (using 11 fuel)



#Interesting tidbits:

**Map of the galaxy**

![](https://i.imgur.com/dVG2f4p.png)

*(I have yet to highlight the chosen road)*

**Shortest routes from A to every planet**

    From A to A : A (using 0 fuel)
    From A to B : A-B (using 1 fuel)
    From A to C : A-C (using 1 fuel)
    From A to D : A-C-D (using 2 fuel)
    From A to E : A-C-E (using 3 fuel)
    From A to F : A-C-D-F (using 4 fuel)
    From A to G : A-C-D-G (using 3 fuel)
    From A to H : A-C-E-H (using 4 fuel)
    From A to I : A-C-D-G-J-I (using 7 fuel)
    From A to J : A-C-D-G-J (using 5 fuel)
    From A to K : A-C-E-H-K (using 7 fuel)
