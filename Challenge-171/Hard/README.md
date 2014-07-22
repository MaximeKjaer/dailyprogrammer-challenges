#[Challenge #171 Hard](http://www.reddit.com/r/dailyprogrammer/comments/2b21mp/7182014_challenge_171_hard_intergalatic_bitstream/)

This challenge is all about compression: compress the 3 following sentences into as few bits as even possible:

     REMEMBER TO DRINK YOUR OVALTINE
    
    
     GIANTS BEAT DODGERS 10 TO 9 AND PLAY TOMORROW AT 1300 
    
    
     SPACE THE FINAL FRONTIER THESE ARE THE VOYAGES OF THE BIT STREAM DAILY PROGRAMMER TO SEEK OUT NEW COMPRESSION
    
    
I have created my own algorithm for this challenge. It's based on these 3 rules

- 00 is used to separate characters.
- A character's binary code can therefore end on as many 0s as it may, but it can't start on a 0, and it can't have 2 or more consecutive zeros in the middle.
- The number of bits per character is variable - the characters with the highest frequency will be assigned to the lowest number of bits.

The dictionary in the solution may provide a better idea of how I assign bit values to each letter.

This method enabled me to get the following output:


    Read message of 31 Bytes
    Compressing  248  Bits into  159  Bits ( 35.8870967742 % compression)
    Sending Message.
    Decompressing Message into 31 Bytes.
    Message Matches!
    
    Read message of 53 Bytes
    Compressing  424  Bits into  273  Bits ( 35.6132075472 % compression)
    Sending Message.
    Decompressing Message into 53 Bytes.
    Message Matches!
    
    Read message of 109 Bytes
    Compressing  872  Bits into  545  Bits ( 37.5 % compression)
    Sending Message.
    Decompressing Message into 109 Bytes.
    Message Matches!
