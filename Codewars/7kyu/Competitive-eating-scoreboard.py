"""
You are the judge at a competitive eating competition and you need to choose a winner!

There are three foods at the competition and each type of food is worth a different amount of points.
Points are as follows:

Chickenwings: 5 points

Hamburgers: 3 points

Hotdogs: 2 points

Write a function that helps you create a scoreboard.
It takes as a parameter a list of objects representing the participants, for example:

[
  {name: "Habanero Hillary", chickenwings: 5 , hamburgers: 17, hotdogs: 11},
  {name: "Big Bob" , chickenwings: 20, hamburgers: 4, hotdogs: 11}
]
It should return "name" and "score" properties sorted by score; if scores are equals, sort alphabetically by name.

[
  {name: "Big Bob", score: 134},
  {name: "Habanero Hillary", score: 98}
]
Happy judging!

"""

class Person:
    points = {
        "chickenwings": 5,
        "hamburgers": 3,
        "hotdogs": 2
    }
    
    def __init__(self, person: dict):
        self.name = person.get('name')
        self.chickenwings = person.get("chickenwings", 0)
        self.hamburgers = person.get("hamburgers", 0)
        self.hotdogs = person.get("hotdogs", 0)
    
    def get_score(self):
        return ( self.chickenwings *  Person.points.get("chickenwings") + \
                self.hamburgers *  Person.points.get("hamburgers") + \
                self.hotdogs *  Person.points.get("hotdogs") 
        )

def scoreboard(who_ate_what):
    result = []
    for obj in who_ate_what:
        p = Person(obj)
        result.append({"name": p.name, "score": p.get_score()})
        result.sort(key=lambda p: (-p["score"], p["name"]))
    return result