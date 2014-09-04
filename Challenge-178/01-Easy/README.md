#[Challenge #178 Easy - Geometric transformations](http://www.reddit.com/r/dailyprogrammer/comments/2f6a7b/9012014_challenge_178_easy_transformers_matrices/)

**Python 3.4**

A very succinct Python solution. It uses eval(), so there's the added benefit of having certain extra functionality, namely:

 - ```exit()``` for a clean exit.
 - The whole ```math``` suite (```math.pi, math.sin(), math.cos()```...)
 - Any builtin function that returns a number (```.count(), abs(), len()...```)


**I/O**

    >> (0, 5)
    0 5
    >> translate(3, 2)
    3 7
    >> scale(1,3,0.5)
    2.0 5.0
    >> rotate(3,2,1.57079632679)
    6.0 3.0
    >> reflect(X) 
    6.0 -3.0
    >> translate(2,-1)
    8.0 -4.0
    >> scale(0,0,-0.25)
    -2.0 1.0
    >> rotate(1,-3,3.14159265359)
    4.0 -7.0
    >> reflect(Y)
    -4.0 -7.0
