"""File to define River class."""

__author__ = "730411985"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River ecosystem of bears and fish."""
    day: int
    fish: list[Fish]
    bears: list[Bear]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:  # 2/1.1
        """Remove old animals from river."""
        check_fish: list[Fish] = []  # empty lists to add to instead of removing from list
        check_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                check_fish.append(fish)
        for bears in self.bears:
            if bears.age <= 5:
                check_bears.append(bears)
        self.fish = check_fish
        self.bears = check_bears
        return None
    
    def remove_fish(self, amount: int) -> None:  # 2/1.2
        """Remove given amount of fish."""
        for fishies in range(0, amount):
            self.fish.pop(fishies)
        return None

    def bears_eating(self) -> None:  # 2/2.3
        """Bears eat 3 fish a day if possible, increasing hunger score and decreasing fish."""
        for bears in self.bears:
            if len(self.fish) >= 5:  # check for 5+ fish for this bear
                self.remove_fish(3)  # remove 3 fish
                bears.eat(3)  # bear eats 3 fish
        return None
    
    def check_hunger(self) -> None:  # 2/2.4
        """Remove bears in cases of starvation."""
        not_starving: list[Bear] = []
        for teddy in self.bears:
            if teddy.hunger_score >= 0:  # not starving
                not_starving.append(teddy)  # use append on lists
        self.bears = not_starving
        return None
        
    def repopulate_fish(self) -> None:  # 2/3.2
        """Each pair of fish mates for four offspring."""
        fish_pairs = len(self.fish) // 2  # floor division rounds down to whole num
        for fish in range(0, fish_pairs):  # iterate through each fish pairs
            for fish in range(0, 4):  # add fish four times for each adult pair
                self.fish.append(Fish())
        return None    
    
    def repopulate_bears(self) -> None:  # 2/3.1
        """Each pair of bears mates for a single offspring."""
        babies: list[Bear] = len(self.bears) // 2  # floor division rounds down to whole num
        self.bears.append(babies)
        return None
    
    def view_river(self) -> None:  # 1/3.3 working
        """Print river status."""
        print(f"~~~ Day {str(self.day)}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self) -> None:  # 1/4.3
        """Simulate one week of life in river."""
        day: int = 0
        while day <= 7:  # iterate over 7 days 
            self.one_river_day()
            day += 1
            
