# PyCounsel
PyCounsel is a basic mental health counseling program. Created for CS521 at Boston University. Spring 2021.

## How It Works
1. Takes a user's name and complaint and creates an instance of the User class using the inputs as parameters
2. Reads three text files - each containing a list of common symptoms for depression, anxiety, and substance abuse - into three awaiting empty lists
3. The user's mental health complaint is checked against these lists to see if there are any matching words between the complaint string and the list
4. A match will indicate that the user is experiencing a symptom of one of the three issues PyCounsel works with
5. The name of the issue which symptoms matched the user's complaint into a separate list
6. This list is then passed into a method that will either tell the user they seem to be okay, or it will ask if the user would like some advice
  a. Should the user choose to not ask for advice, the program thanks the user and closes
  
  b. Should the user choose yes, the method will return a string of generic advice from another list on how to deal with the issue the user is dealing with. Depending on which issue/s the user is dealing with, they will receive the advice that matches it
7. The program then issues a disclaimer stating it is not a real therapist and ends. 
