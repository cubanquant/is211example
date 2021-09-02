class BaseballPlayer:
    def __init__(self, name, team):
        """
        Constructor of a BaseballPlayer class

        :param name: The name of the player
        :param team: The team of the player
        """
        self.name = name
        self.team = team

    def display(self):
        """Display the Baseball player's name and team"""
        print(f"I'm {self.name} and I play for {self.team}")


if __name__ == "__main__":
    p1 = BaseballPlayer("Aaron Judge", "The New York Yankees")
    p2 = BaseballPlayer("Shohei Otani", "The LA Angels")

    p1.display()
    p2.display()
