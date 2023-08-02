"""
Your friend has been out shopping for puppies (what a time to be alive!)... 
He arrives back with multiple dogs, and you simply do not know how to respond!

By repairing the function provided, you will find out exactly how you should respond, depending on the number of dogs he has.

The number of dogs will always be a number and there will always be at least 1 dog.

Good luck!"""

# first-solution
def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
    respond = dogs[0] if n <= 10 else dogs[1] if n <= 50 else dogs[3] if n == 101  else dogs[2]
    return respond

#second-solution to explain 
def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];

    if n <= 10 : return dogs[0]
    elif n <= 50 : return dogs[1]
    elif n == 101 : return dogs[3]
    else :  
        return dogs[2]
        