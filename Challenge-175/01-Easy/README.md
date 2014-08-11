#[Challenge #175 Easy - Inefficient sorting algorithms - Bogo!](http://www.reddit.com/r/dailyprogrammer/comments/2d8yk5/8112014_challenge_175_easy_bogo/)

**Python 3.4**

Turns out that [Bogosort](http://en.wikipedia.org/wiki/Bogo-sort) actually is pretty efficient once you implement Bogobogosort!! Here's a script comparing the two.

#**Output**

    BOGO SORT
    ==============================
    29 iterations
    20 iterations
    1 iterations
    18 iterations
    22 iterations
    43 iterations
    80 iterations
    36 iterations
    9 iterations
    56 iterations
    
    BOGOBOGO SORT
    ==============================
    13444 iterations
    5774 iterations
    17247 iterations
    10959 iterations
    1329 iterations
    1256 iterations
    6839 iterations
    1430 iterations
    21624 iterations
    5506 iterations
    
Averages over 50 runs are:

 - **Bogosort**: 50.44 iterations
 - **Bogobogosort**: 10252.48 iterations
