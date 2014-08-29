#[Challenge #175 Easy - Inefficient sorting algorithms - Bogo!](http://www.reddit.com/r/dailyprogrammer/comments/2d8yk5/8112014_challenge_175_easy_bogo/)

**Python 3.4**

Turns out that [Bogosort](http://en.wikipedia.org/wiki/Bogo-sort) actually is pretty efficient once you implement Bogobogosort!! Here's a script comparing the two.

#**Output**

    BOGO SORT
    ==============================
    Finished: 29 iterations with word 'hello'
    Finished: 20 iterations with word 'hello'
    Finished: 1 iterations with word 'hello'
    Finished: 18 iterations with word 'hello'
    Finished: 22 iterations with word 'hello'
    Finished: 43 iterations with word 'hello'
    Finished: 80 iterations with word 'hello'
    Finished: 36 iterations with word 'hello'
    Finished: 9 iterations with word 'hello'
    Finished: 56 iterations with word 'hello'
    
    (WRONG) BOGOBOGO SORT
    ==============================
    Finished: 13444 iterations with word 'hello'
    Finished: 5774 iterations with word 'hello'
    Finished: 17247 iterations with word 'hello'
    Finished: 10959 iterations with word 'hello'
    Finished: 1329 iterations with word 'hello'
    Finished: 1256 iterations with word 'hello'
    Finished: 6839 iterations with word 'hello'
    Finished: 1430 iterations with word 'hello'
    Finished: 21624 iterations with word 'hello'
    Finished: 5506 iterations with word 'hello'
    
    (CORRECT) BOGOBOGO SORT
    ==============================
    Finished: 2214442 iterations with word 'hello'
    Finished: 5904668 iterations with word 'hello'
    Finished: 1952674 iterations with word 'hello'
    Finished: 39587 iterations with word 'hello'
    Finished: 345852 iterations with word 'hello'
    Finished: 5295625 iterations with word 'hello'
    Finished: 506875 iterations with word 'hello'
    Finished: 5499247 iterations with word 'hello'
    Finished: 1797950 iterations with word 'hello'
    Finished: 324256 iterations with word 'hello'


    
 - **Bogosort**: 50.44 iterations (over 50 runs)
 - **My wrong Bogobogosort**: 10252.48 iterations (over 50 runs)
 - **[/u/Nodocify](http://www.reddit.com/user/Nodocify)'s correct Bogobogosort**: 2388117.6 iterations (over 10 runs)
