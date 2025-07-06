"""This module defines the GenerationIdentifier class, which is used to 
identify the generation of an individual based on their birth year.
"""
__version__ = "4.4.2025"
__author__ = "Cedrick S"

class GenerationIdentifier:
    """A class to identify the generation which an individual belongs to
    based on their birth year.
    """

    def __init__(self, birth_year: int):
        """Initialises an instance of the GenerationIdentifier class.

        Args:
            birth_year (int): Represents the birth year of a person.
        """

        self.birth_year = birth_year

    def identifier(self) -> str:
        """Identifies the generation based on the birth_year.

        Args:
            birth_year (int): The birth year of a person.

        Returns:
            str: What type of generation the person belong too.
        """

        birth_year = self.birth_year

        if birth_year >= 1000 and birth_year <= 1150:
            print("You are part of the middle ages generation.")
            print("Were you a peasant in the medieval era?")
        elif birth_year >= 1150 and birth_year <= 1250:
            print("You are part of the crusader generation.")
            print("What was your rank in the crusader army.")
        elif birth_year >= 1250 and birth_year <= 1350:
            print("You are part of the late medieval generation.")
            print("What was your opinion on the renaissance days?")
        elif birth_year >= 1350 and birth_year <= 1450:
            print("You part of the plague generation.")
            print("How was your daily life during the black death.")
        elif birth_year >= 1450 and birth_year <= 1500:
            print("You are part of the pre-renaissance generation.")
            print("What was your contribution towards art and humanism.")
        elif birth_year >= 1500 and birth_year <= 1600:
            print("You are part of the renaissance generation.")
            print("What was the favorite thing you witnessed.")
        elif birth_year >= 1600 and birth_year <= 1700:
            print("You are scientific revolution generation.")
            print("Who was your favorite philosopher.")
        elif birth_year >= 1700 and birth_year <= 1800:
            print("You are part of the enligtment generation.")
            print("What is your idea of liberty and freedom?")
        elif birth_year >= 1800 and birth_year <= 1830:
            print("You are part of the napoleonic generation.")
            print("I'm sorry you had to live through was that reshaped Europe.")
        elif birth_year >= 1830 and birth_year <= 1860:
            print("You are part of the Victorian generation.")
            print("I know you witnessed the rise of the British Empire and the " \
            "industrial boom.")
        elif birth_year >= 1860 and birth_year <= 1882:
            print("You are part of the Second Industrial Revolution Generation.")
            print("What technology did you love the most.")
        elif birth_year >= 1883 and birth_year <= 1900:
            print("You are part of the progressive generation.")
            print("What reform movements did you admire the most?")
        elif birth_year >= 1901 and birth_year <= 1927:
            print("You are part of the greatest generation.")
            print("I'm sorry you had to live through world war two and the " \
            "great depression.")
        elif birth_year >= 1928 and birth_year <= 1945:
            print("You are part of the silent generation.")
            print("I'm sorry you had to live through different wars but I hope " \
            "you did your civic duty.")
        elif birth_year >= 1946 and birth_year <= 1964:
            print("You are part of the baby boomer generation.")
            print("How many kids did you have? 10 or 15 hehehe")
        elif birth_year >= 1965 and birth_year <= 1980:
            print("You are part of the generation X")
            print("I know you lived through independence, early tech innovation" \
            " and economic transitions.")
        elif birth_year >= 1981 and birth_year <= 1996:
            print("You are part of the millenials generation.")
            print("I know you lived through digital transformation and the " \
            "2008 recession.")
        elif birth_year >= 1997 and birth_year <= 2012:
            print("You are part of the generation Z")
            print("I know you have been raised with smartphones. What is the " \
            "new tik tok trend you're doing?")
        elif birth_year >= 2013 and birth_year <= 2025:
            print("You are part of the generation Alpha.")
            print("I know you have been raised with Artificial Intellegence," \
            " climate change awareness and the pandemic world.")
            print("What did you do during covid?")
        else:
            return "Sorry, you have entered an invalid birth year."

generation = GenerationIdentifier(birth_year=2010)
message = generation.identifier()
print(message)