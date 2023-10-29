""" A simple social network for tracking connections between people. """


class Person:
    """A person in a social network.
    
    Attributes:
        name(str): the persons name
        connections(set of Person): other people int he social network who
            know this
    """