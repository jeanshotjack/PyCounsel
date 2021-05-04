'''
Jean (Diana) Shalenkova
Class: CS 521 - Spring 2
Date: 29 April 2021
Term Project Code
Description of Problem:
    This is PyCounsel, my term project for the course. It is a basic mental
    health counseling program. It takes a user's name and complaint, and then
    it searched through the complaint and checks to see if any of them are in
    the three files containing common symptoms of depression, anxiety, and
    substance abuse. It then asks if the user wants advice and returns the
    advice string.

    INSTRUCTIONS: Just run the project in your IDE!
'''

# Init empty lists into which the files will read their contents
d_list = []
a_list = []
s_list = []

# A list of generic advice for people suffering from mental health issues.
advice = ["it sounds like you may be struggling with depression. You are not "
          "alone. Consider reaching out to someone you trust.\n",
          "it sounds like you may be struggling with anxiety. Take a time out "
          "and try to step back from the problem. Try counting to ten.\n",
          "it sounds like you may be struggling with substance abuse. Please "
          "reach out to someone who can help you through your path to "
          "sobriety.\n"]


class User:
    '''
    Constructs an object User (the user of the program) and its methods.
    '''
    def __init__(self, name, complaint):
        '''
        Creates a new instance of User
        :param name: The name of the user from input
        :param complaint: The user's complaint from input
        '''
        self.name = name
        self.complaint = complaint

    def get_complaint(self):
        '''
        Finds the user complaint and returns it (for ease of use in program)
        :return: The user's complaint as a string
        '''
        return self.complaint

    def want_advice(self, observed):
        '''
        Handles giving the user advice should they choose to ask for it.
        :param observed: The observed issue with which the user's complaint
                            aligns
        :return: Users name, comma, with either a piece of advice based on
                    which issue they seem to be experiencing, or telling them
                    that they are okay, or thanking them for using the program.
        '''

        # The result string onto which our advice or thanks will be attached
        res = f"\n{self.name}, "

        # If the list of observed issues is not empty
        if observed:
            ask_advice = input(
                "Would you like some advice? Please type y or n: ")
            if ask_advice.lower() == "y":
                if "depression" in observed:
                    res += str(advice[0])  # Pull advice from list of generic
                if "anxiety" in observed:
                    res += str(advice[1])  # advice based on which issue the
                if "substance abuse" in observed:
                    res += str(advice[2])  # user seems to be experiencing
            else:
                res += "thank you for using PyCounsel."
        else:
            res += "thankfully, you seem to not be experiencing symptoms of " \
                   "depression, anxiety, or substance abuse."
        return res

    def __repr__(self):
        '''
        Returns a representation of object User
        '''
        return f"The user's name is {self.name} and the user's mental health" \
               f" complaint is '{self.complaint}'"


def read_files():
    '''
    Reads our 3 symptoms files and sorts them into lists for easier use.
    :return: No return
    '''
    with open("depress.txt", "r") as depression:
        for line in depression:
            line = line.strip()
            d_list.append(line)

    with open("anxiety.txt", "r") as anxiety:
        for line in anxiety:
            line = line.strip()
            a_list.append(line)

    with open("substance.txt", "r") as substance:
        for line in substance:
            line = line.strip()
            s_list.append(line)


def get_complaint_type(user_complaint):
    '''
    Checks to see if any words in the user's complaint match the symptoms lists,
    and creates a list of the issues their symptoms match
    :param user_complaint: Input from user complaint
    :return: A list of the issues the user's symptoms match
    '''

    # Init empty list to hold the issue names
    observed = []

    if any([emotion in user_complaint for emotion in a_list]):
        observed.append("anxiety")

    if any([emotion in user_complaint for emotion in d_list]):
        observed.append("depression")

    if any([emotion in user_complaint for emotion in s_list]):
        observed.append("substance abuse")

    return observed


def unit_test():
    '''
    A unit test with a hardcoded test user to check User class methods.
    :return: No return
    '''
    test_user = User("Dan", "I feel irritable, nauseous, and paranoid.")
    assert (repr(test_user) == "The user's name is Dan and the user's mental "
                               "health complaint is 'I feel irritable, "
                               "nauseous, and paranoid.'"), \
        "The User repr method is not functioning."
    assert test_user.get_complaint() == "I feel irritable, nauseous, and " \
                                        "paranoid.", "The User get complaint " \
                                                    "method is not functioning."
    test_observed = ["anxiety"]
    assert test_user.want_advice(test_observed) == \
           "\nDan, it sounds like you may be struggling with anxiety. Take a " \
           "time out and try to step back from the problem. Try counting to " \
           "ten.\n", "The User want advice method is not functioning."


def main():
    try:
        # Read text files into lists
        read_files()

        #  Ask user to input their  name and their complaint
        name = input("Welcome to PyCounsel, a Python-run counseling program."
                          " Please enter your name: ")
        complaint = input("Please state your mental health complaint: ")

        # Create instance of User with our above inputs as parameters
        user = User(name, complaint)

        # Pull the user complaint
        user_complaint = user.get_complaint()

        # Determine which category/ies the user's symptoms fall into
        observed = get_complaint_type(user_complaint)

        # Ask user if they want any advice, and print the result of this process
        suggest = user.want_advice(observed)
        print(suggest)

    except:
        print("PyCounsel is having trouble. Please try again.")

    # Disclaimer
    finally:
        print(f"\nPlease remember"
              f" that PyCounsel is not a replacement for mental health "
              f"counseling.\nIf you are struggling with mental health issues,"
              f" please refer to a licensed therapist\nor call SAMHSA's "
              f"National Helpline at 1-800-662-HELP (4357).")


if __name__ == '__main__':
    # Unit test commented out for smooth running of program.
    # Un-comment to run the unit test.
    # unit_test()
    main()



