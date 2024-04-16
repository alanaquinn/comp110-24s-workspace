"""Class writing and Instantiating."""

# Definition
class Profile:  # name class

    username: str  # attributes
    private: bool

    def __init__(self, username_input: str):  # constructor
        """Constructor to create new Profile object."""
        username_input == Profile.username
        Profile.private == True
        # constructor will be returning Profile object 
        # but dont have to write that return

    def tweet(self, msg: str) -> None:  # prints something but doesnt return anything
        """If profile public, print msg."""
        if not self.private:  # access private attribute within Profile (self bc in Profile)
            print(msg)

# Instantiation --> class_name(arguments)
user1: Profile = Profile("110_rulez")  
    # calls __init__(), dont need to put self --> only need username as argument
user1.private = False
    # user1 is automatically set as True, access attribute with variable_name.attribute_name
user1.tweet("OOP is cool!")
    # function call would be tweet(user1, " ")
    # but method call puts first argument(self) before