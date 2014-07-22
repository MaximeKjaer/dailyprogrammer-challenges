#[Challenge #172 Intermediate (2)](http://www.reddit.com/r/dailyprogrammer/comments/2ba46z/7252014_challenge_172_intermediate_breach/)

This will be the easiest one so far for me... because I already had the code for this laying around! It was for a project that I've pretty much abandonned. It's in 2 files - a maker and a checker.

#**Sample input and output**

Running the following command: ```python password_maker.py test123``` will create the following output: 

```salt.txt```:

    8516df486fe34f19b52bc0812e72cfe5

```encrypted.txt```:

    4c925be95cd08257296ac684c3e32c9b739c69f0a700589ac737ac77dfc5d125ad37f7e8204b696c3584b6cf5fe2afbc600feb5ebbdfb992052cfbe9f328a682

And of course, running the ```password_checker.py``` with the correct password will return:

    ACCESS GRANTED
