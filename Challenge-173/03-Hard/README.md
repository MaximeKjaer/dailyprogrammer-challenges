#[Challenge #173 Hard - Road Trip Game](http://www.reddit.com/r/dailyprogrammer/comments/2ccipl/8012014_challenge_173_hard_road_trip_game/)

The game is pretty self-descriptive. 

**Sample play-through**

    It is 2114. We have colonized the Galaxy.
    To communicate we send 140 character max messages using [A-Z0-9].
    The technology to do this requires faster than light pulses to beam the messages to relay stations.
    
    Your job is to travel to another planet in your system and implement the Intergalactic Bitstreaming machine.
    
    That planet is 1% of a lightyear away.
    
    All you have is a broken spaceship, 300 food and 400 oxygen.
    
    Your mission is to get to the other planet as quickly as possible. To do so, you'll have to pick up people along the way. These people will have different skills - it's up to you to decide who you want aboard your ship!
    
    #############################################################
    Day 1, Year 2114.
    You found someone along the way!
    It's Jerry Yarbrough (Engineer)
    Would you like to have Jerry Yarbrough join the crew?
    
            Abilities: 
            * Will repair something in the spaceship and triple your speed every day.
            * Eats 15 food
            * Uses 10 oxygen
            
    1. Yes
    2. No
    Enter your choice: 1
    CREW: 
     Farmers: 0
     Chefs: 0
     Engineers: 1
    
    RESOURCES: 
     Food: 275.0
     Oxygen:380
     Progress: 4.8e-06%
     Speed: 4560 km per day
    #############################################################
    Day 2, Year 2114.
    You found someone along the way!
    It's Melaine Saucedo (Chef)
    Would you like to have Melaine Saucedo join the crew?
    
            Abilities: 
            * Will prevent food waste: -20% food consumption
            * Eats 20 food
            * Uses 15 oxygen
            
    1. Yes
    2. No
    Enter your choice: 2
    CREW: 
     Farmers: 0
     Chefs: 0
     Engineers: 1
    
    RESOURCES: 
     Food: 250.0
     Oxygen:360
     Progress: 1.44e-05%
     Speed: 9120 km per day
    #############################################################
    Day 3, Year 2114.
    You didn't find anyone today.
    
    
    CREW: 
     Farmers: 0
     Chefs: 0
     Engineers: 1
    
    RESOURCES: 
     Food: 225.0
     Oxygen:340
     Progress: 3.36e-05%
     Speed: 18240 km per day
    #############################################################
    Day 4, Year 2114.
    You found someone along the way!
    It's Melaine Cleveland (Farmer)
    Would you like to have Melaine Cleveland join the crew?
    
            Abilities: 
            * Will produce 25 food and 15 oxygen every day.
            * Eats 10 food
            * Uses 10 oxygen
            
    1. Yes
    2. No
    Enter your choice: 1
    CREW: 
     Farmers: 1
     Chefs: 0
     Engineers: 1
    
    RESOURCES: 
     Food: 215.0
     Oxygen:325
     Progress: 7.2e-05%
     Speed: 36480 km per day
    #############################################################
    Day 5, Year 2114.
    You didn't find anyone today.
    
    
    CREW: 
     Farmers: 1
     Chefs: 0
     Engineers: 1
    
    RESOURCES: 
     Food: 205.0
     Oxygen:310
     Progress: 0.00014879999999999998%
     Speed: 72960 km per day
    #############################################################
    Day 6, Year 2114.
    You found someone along the way!
    It's Dessie Saucedo (Chef)
    Would you like to have Dessie Saucedo join the crew?
    
            Abilities: 
            * Will prevent food waste: -20% food consumption
            * Eats 20 food
            * Uses 15 oxygen
            
    1. Yes
    2. No
    Enter your choice: 2
    CREW: 
     Farmers: 1
     Chefs: 0
     Engineers: 1
    
    RESOURCES: 
     Food: 195.0
     Oxygen:295
     Progress: 0.00030240000000000003%
     Speed: 145920 km per day
    #############################################################
    Day 7, Year 2114.
    You found someone along the way!
    It's Tu Staley (Farmer)
    Would you like to have Tu Staley join the crew?
    
            Abilities: 
            * Will produce 25 food and 15 oxygen every day.
            * Eats 10 food
            * Uses 10 oxygen
            
    1. Yes
    2. No
    Enter your choice: 1
    CREW: 
     Farmers: 2
     Chefs: 0
     Engineers: 1
    
    RESOURCES: 
     Food: 200.0
     Oxygen:285
     Progress: 0.0006096%
     Speed: 291840 km per day
    #############################################################
    Day 8, Year 2114.
    You found someone along the way!
    It's Vannessa Staley (Farmer)
    Would you like to have Vannessa Staley join the crew?
    
            Abilities: 
            * Will produce 25 food and 15 oxygen every day.
            * Eats 10 food
            * Uses 10 oxygen
            
    1. Yes
    2. No
    Enter your choice: 1
    CREW: 
     Farmers: 3
     Chefs: 0
     Engineers: 1
    
    RESOURCES: 
     Food: 220.0
     Oxygen:280
     Progress: 0.001224%
     Speed: 583680 km per day
    #############################################################
    Day 9, Year 2114.
    You found someone along the way!
    It's Natacha Adcock (Farmer)
    Would you like to have Natacha Adcock join the crew?
    
            Abilities: 
            * Will produce 25 food and 15 oxygen every day.
            * Eats 10 food
            * Uses 10 oxygen
            
    1. Yes
    2. No
    Enter your choice: 1
    CREW: 
     Farmers: 4
     Chefs: 0
     Engineers: 1
    
    RESOURCES: 
     Food: 255.0
     Oxygen:280
     Progress: 0.0024527999999999998%
     Speed: 1167360 km per day
    #############################################################
    Day 10, Year 2114.
    You found someone along the way!
    It's Boyce Cleveland (Engineer)
    Would you like to have Boyce Cleveland join the crew?
    
            Abilities: 
            * Will repair something in the spaceship and triple your speed every day.
            * Eats 15 food
            * Uses 10 oxygen
            
    1. Yes
    2. No
    Enter your choice: 1
    CREW: 
     Farmers: 4
     Chefs: 0
     Engineers: 2
    
    RESOURCES: 
     Food: 275.0
     Oxygen:270
     Progress: 0.0073679999999999995%
     Speed: 4669440 km per day
    #############################################################
    Day 11, Year 2114.
    You found someone along the way!
    It's Melaine Adcock (Farmer)
    Would you like to have Melaine Adcock join the crew?
    
            Abilities: 
            * Will produce 25 food and 15 oxygen every day.
            * Eats 10 food
            * Uses 10 oxygen
            
    1. Yes
    2. No
    Enter your choice: 1
    CREW: 
     Farmers: 5
     Chefs: 0
     Engineers: 2
    
    RESOURCES: 
     Food: 310.0
     Oxygen:265
     Progress: 0.0270288%
     Speed: 18677760 km per day
    #############################################################
    Day 12, Year 2114.
    You found someone along the way!
    It's Xuan Oswald (Farmer)
    Would you like to have Xuan Oswald join the crew?
    
            Abilities: 
            * Will produce 25 food and 15 oxygen every day.
            * Eats 10 food
            * Uses 10 oxygen
            
    1. Yes
    2. No
    Enter your choice: 1
    CREW: 
     Farmers: 6
     Chefs: 0
     Engineers: 2
    
    RESOURCES: 
     Food: 360.0
     Oxygen:265
     Progress: 0.10567199999999999%
     Speed: 74711040 km per day
    #############################################################
    Day 13, Year 2114.
    You found someone along the way!
    It's Natacha Yarbrough (Engineer)
    Would you like to have Natacha Yarbrough join the crew?
    
            Abilities: 
            * Will repair something in the spaceship and triple your speed every day.
            * Eats 15 food
            * Uses 10 oxygen
            
    1. Yes
    2. No
    Enter your choice: 1
    CREW: 
     Farmers: 6
     Chefs: 0
     Engineers: 3
    
    RESOURCES: 
     Food: 395.0
     Oxygen:255
     Progress: 0.7348176%
     Speed: 597688320 km per day
    #############################################################
    Day 14, Year 2114.
    You didn't find anyone today.
    
    
    CREW: 
     Farmers: 6
     Chefs: 0
     Engineers: 3
    
    RESOURCES: 
     Food: 430.0
     Oxygen:245
     Progress: 5.7679824%
     Speed: 4781506560 km per day
    #############################################################
    Day 15, Year 2114.
    You found someone along the way!
    It's Vannessa Staley (Chef)
    Would you like to have Vannessa Staley join the crew?
    
            Abilities: 
            * Will prevent food waste: -20% food consumption
            * Eats 20 food
            * Uses 15 oxygen
            
    1. Yes
    2. No
    Enter your choice: 2
    CREW: 
     Farmers: 6
     Chefs: 0
     Engineers: 3
    
    RESOURCES: 
     Food: 465.0
     Oxygen:235
     Progress: 46.0333008%
     Speed: 38252052480 km per day
    #############################################################
    Day 16, Year 2114.
    You found someone along the way!
    It's Jerry Staley (Chef)
    Would you like to have Jerry Staley join the crew?
    
            Abilities: 
            * Will prevent food waste: -20% food consumption
            * Eats 20 food
            * Uses 15 oxygen
            
    1. Yes
    2. No
    Enter your choice: 1
    CREW: 
     Farmers: 6
     Chefs: 1
     Engineers: 3
    
    RESOURCES: 
     Food: 477.5
     Oxygen:210
     Progress: 368.155848%
     Speed: 306016419840 km per day
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    YOU WIN!!
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    Score: 1037
