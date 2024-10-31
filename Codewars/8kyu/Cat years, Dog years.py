"""
Kata Task
I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:
    humanYears >= 1
    humanYears are whole numbers only

Cat Years
    15 cat years for first year
    +9 cat years for second year
    +4 cat years for each year after that

    Dog Years
    15 dog years for first year
    +9 dog years for second year
    +5 dog years for each year after that

"""

def human_years_cat_years_dog_years(human_years):
    
    cat_year = {
        1 : 15,
        2 : 24,
    }
    
    dog_year = {
        1 : 15,
        2 : 24,
    }
    
    cat_y = cat_year[human_years] if human_years <= 2 else cat_year[2] + (human_years-2) * 4
    dog_y = dog_year[human_years] if human_years <= 2 else dog_year[2] + (human_years-2) * 5
    
    return [human_years, cat_y, dog_y]