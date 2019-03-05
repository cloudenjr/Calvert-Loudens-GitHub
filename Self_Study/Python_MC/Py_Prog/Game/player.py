# *********************************************************************************************************************
# Challenge:
# Modify the Player class so that the players' scores are increased by one thousand every time their level increases
# by one. So if they jump two levels, they'll get a bonus of two thousand added to their score.
#
# If the player drops back a level, they'll lose one thousand for each level they drop back. They can't go below
# Level One, so your solution should prevent that from happening.
#
# """ the aim of ghis challenge is to practice properties, so although it may make more sense to add methods to increase
# and decrease the level, please dont do it that way - use a property."""
# *********************************************************************************************************************


class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level can't be less than 1")

    lives = property(_get_lives, _set_lives)  # if you dont specify a method (whats in parens in the code
                                              # preceding this statement) to use for the setter the property
                                              # is going to be read only;
                                              # - if you specify a setter, but no getter, you can change the value
                                              # of the property but you cant display it

    level = property(_get_level, _set_level)  # make sure NOT to use parens when setting up your properties

    @property   # another way to write property syntax; this method takes care of the 'score = property(_,_)' line
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score


    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
        # return "Name: {0}, Lives: {1}, Level: {2}, Score: {3}".format(self.name, self.lives, self.level, self.score)

