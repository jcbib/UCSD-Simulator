"""A collection of functions and classes for doing my project."""
import random as rd
from time import *
import sys

# Classes I created

class Catalog:
    """
    Catalog object containing all of the majors
    
    Attributes
    ----------
        major_list : list
            List containing all of the different majors
    """
    
    def __init__(self):
        """
        Initializes a Catalog object
        
        Parameters
        ----------
        None
        
        Returns
        -------
        Nothing
        
        """
        self.major_list = ['Anthropology', 'Bioengineering', 'Bioinformatics', 'Ecology',
                           'General Biology', 'Human Biology', 'Microbiology',
                           'Molecular and Cell Biology', 'Neurobiology', 'Biochemistry',
                           'Chemistry', 'Environmental Chemistry', 'Pharmacological Chemistry',
                           'Chinese Studies', 'Classical Studies', 'Cognitive Science',
                           'Communication', 'Computer Engineering', 'Computer Science',
                           'Critical Gender Studies', 'Data Science', 'Economics',
                           'Management Science', 'Electrical Engineering', 
                           'Engineering Physics',
                           'Mechanical Engineering', 'Aerospace Engineering', 'NanoEngineering',
                           'Structural Engineering', 'Ethnic Studies', 'Public Health',
                           'German Studies', 'Global Health', 'History', 
                           'Human Developmental Sciences',
                           'International Studies', 'Italian Studies', 'Japanese Studies',
                           'Jewish Studies', 'Latin American Studies', 'Linguistics', 
                           'Literature',
                           'Mathematics', 'Probability and Statistics', 'Spanish Literature',
                           'World Literature and Culture', 'Music', 'ICAM', 
                           'Chemical Engineering',
                           'Philosophy', 'Physics', 'Astrophysics', 'Political Science', 
                           'Psychology',
                           'Business Psychology', 'Religion', 'Russian and Soviet Studies',
                           'Earth Sciences', 'Marine Biology', 
                           'Oceanic and Atmospheric Sciences',
                           'Sociology', 'Dance', 'Theatre', 'Third World Studies',
                           'Urban Studies and Planning', 
                           'Real Estate and Development',
                           'Art History', 'Visual Arts']

class Student:
    """ 
    Student object
    
    Attributes
    ----------
        name : string
            Name of the student
        PID : string
            PID of the student
        stats : dictionary
            This holds the stats of the player
        course_list : list
            This holds all the courses the student has ever taken
        inventory : list
            This holds what the student currently has on them
        major : string
            This holds the major the student is in
        week : integer
            This holds the current week 
    """
    
    def __init__(self, name, major):
        """
        Initializes a Student object
        
        Parameters
        ----------
        name : string 
            Name of the student
        major : string
            String containing the student major
            
        Returns
        -------
        Nothing
        
        """
        
        self.name = name
        self.week = 0
        
        # Get a random PID for the real UCSD experience!
        PID = 'A'
        for i in range(8):
            PID = PID + str(rd.randint(0,9))
        self.PID = PID
     
        self.stats = {'HP' : 0, 'Hunger' : 0, 
                      'Intellect' : 0, 'Strength' : 0, 
                      'Luck' : 0, 'Wealth' : 0}
        self.course_list = {'Fall': [], 'Winter': [], 'Spring' : []}
        self.inventory = {}
        
        # Checks that major is a valid one
        major_catalog = Catalog()
        if (major not in major_catalog.major_list) :
            print('Invalid Major! You are Undeclared.')
            self.major = 'Undeclared'
        else:
            self.major = major
    
    def check_stats(self):
        """
        Prints the stats of a student
        
        Parameters
        ----------
        None
            
        Returns
        -------
        Nothing
        
        """
        print(self.name)
        for stat in self.stats:
            print(stat + ': ' + str(self.stats[stat]))
    
    def check_inventory(self):
        """
        Prints the inventory of a student
        
        Parameters
        ----------
        None
            
        Returns
        -------
        Nothing
        
        """
        
        
        for item in self.inventory:
            # If there's more than one item, make it plural
            if ( self.inventory[item] > 1 ):
                if ( item[-1] == 's'):
                    # If there's already an s at the end, print regular item
                    print(str(self.inventory[item]) + ' ' + item)
                else:
                    # If there's no s at the end, print pluralized string
                    print(str(self.inventory[item]) + ' ' + item + 's')
            else:
                # IF there's only one item, print regular string
                print(str(self.inventory[item]) + ' ' + item)
    
    def check_major(self):
        """
        Prints the major of a student
        
        Parameters
        ----------
        None
            
        Returns
        -------
        Nothing
        
        """
        print(self.major)
        
    def check_courses(self):
        """
        Prints the course list of a student
        
        Parameters
        ----------
        None
            
        Returns
        -------
        Nothing
        
        """
        for quarter in self.course_list:
            print(quarter + ':', end = ' ')
            for course in self.course_list[quarter]:
                print(course, end = ' ')
            print()

    
    def add_item(self, item):
        """
        Adds an item to the student's inventory
        
        Parameters
        ----------
        item: string
            The item to be added
            
        Returns
        -------
        Nothing
        
        """
        
        # Lowercasing makes it possible to ignore case
        lower_item = item.lower()
        key_list = []
        
        # Get the keys to determine whether an item is in the inventory already 
        # (not case sensitive)
        for key in self.inventory.keys():
            key_list.append(key.lower()) 
        
        if ( lower_item in key_list ):
            # If input is in the inventory, add one to its value count
            self.inventory[lower_item.capitalize()] += 1
        else:
            # If input it not in the inventory, initialize value to 1
            self.inventory[lower_item.capitalize()] = 1
        
    def stat_change(self, stat, change):
        """
        Changes stats of the student
        
        Parameters
        ----------
        stat: string
            Stat to be changed
        change: snteger
            How much the stat changes
            
        Returns
        -------
        Nothing
        
        """
        
        curr_stat = self.stats[stat]
        if ((curr_stat + change) <= 0):
            # If the stat reaches below 0, set stat to 0
            self.stats[stat] = 0
        elif ((curr_stat + change) >= 50):
            # If stat reaches above 50, set stat to 50
            self.stats[stat] = 50
        else:
            # If stat change is within bounds, then add stat change
            self.stats[stat] = self.stats[stat] + change

    def roll_luck(self, modifier=0):
        """
        Checks if the student is lucky or not
        
        Parameters
        ----------
        modifier : integer
            Any modifier that may affect the likelihood of doing something; defaults 0
            
        Returns
        -------
        Boolean
            True or False depending on whether luck roll was successful
        
        """
        
        luck_range = range(self.stats['Luck'] + modifier)
        rand_int = rd.randint(0, 50)
        if ( rand_int in luck_range ):
             # If random integer is in the range of luck stat, return true
            return True
        else:
            return False
    
    def rand_stats(self):
        """
        Randomizes stats of the student for game initialization and testing
        
        Parameters
        ----------
        None
            
        Returns
        -------
        None
        
        """
        for stat in self.stats:
            self.stats[stat] = rd.randint(1,10)
    
    def enroll(self, quarter, course):
        """
        Adds a course to a student's course list if lucky enough and smart enough
        to get into the class
        
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        
        """
        
        try: 
            int(course[-2:])
        except ValueError:
            print('Invalid Course!')
            return
        
        # Checks if course provided has at least two Capitalized letters in front
        if (not (course[:2].isupper())) :
            print('Invalid Course!')
            return
        
        if ( self.roll_luck(self.stats['Intellect']) ):
            self.course_list[quarter].append(course)
        else:
            print('Failed to enroll!')
        
        
    def major_change(self, new_major):
        """
        For when you feel as if your major just isn't right for you; changes major
        if lucky enough
        
        Parameters
        ----------
        new_major : string
            The major you want to change into
        Returns
        -------
        None
        
        """
    
        
        # Makes sure major entered is valid
        major_catalog = Catalog()
        if ( new_major not in major_catalog.major_list ):
            print('Invalid Major!')
        
        if ( self.roll_luck() ) :
            self.major = new_major
        else:
            print('Failed to change major!')

# Start of Functions

def delay_print(string):
    """
    Alternate string printing that creates nice scrolling effect
    
    Parameters
    ----------
        string : string
            String being printed
    Return
    ------
    None
        
    """
    
    for char in string:
        sys.stdout.write( '%s' % char )
        sys.stdout.flush()
        sleep(0.03375)
        
def int_check(string):
    """
    Checks if input is a valid integer input
    
    Parameters
    ----------
        string : string
            String being checked
    Return
    ------
        Boolean
            True if string is a valid int, False if string isn't valid int
      
    """
    
    try: 
        int(string)
        return True
    except ValueError:
        return False

def loading(string):
    """
    Creates pseudo-loading screen 
    
    Parameters
    ----------
        string : string
            Loading string being printed
    Return
    ------
        None
    """
    sleep(1.0)
    delay_print('\n' + string)
    sleep(0.5)
    delay_print('.')
    sleep(0.5)
    delay_print('.')
    sleep(0.5)
    delay_print('.\n')
    sleep(0.5)
    
def intro_init():
    """
    Creates pseudo-loading screen 
    
    Parameters
    ----------
        None
    Return
    ------
        student : Student
            New student object based on name and major provided
    """
    
    # Initial statements that start the story
    name = str(input('Congratulations on being admitted to UCSD! What is your name?\n'))
    major = str(input('What major did you sign up for?\n'))
    student = Student(name=name, major=major)
    delay_print('\nWelcome to UCSD ' + student.name + ', ' + student.major + ' major!\n')
    delay_print('\nJust a few guidelines:\n')
    delay_print('\n1. Do not let any of your stats get to zero!\n')
    delay_print('\n2. Your choices matter and you should make valid choices!')
    delay_print(' (Numerical Inputs)\n')
    delay_print('\n3. Start early, start often, and have fun!\n')
    delay_print('\nNow get ready for another year in your life!\n')
    
    # Create 'loading screen'
    for i in range(3):
        loading('Getting ready for the first year of college')
    
    # Randomize stats
    student.rand_stats()
    
    return student
    
def two_choices(student, string_list, option_one, option_two):
    """
    Function for events with two choices
    
    Parameters
    ----------
        student : Student
            Student object making the choice
        string_list: list
            List of strings that prompt the player to  make a choice
        option_one: function
            First option function that continues a path
        option_two: function
            Second option function that continues a path
    Return
    ------
        None
    """
    delay_print('\n' + string_list[0] +'\n')
    sleep(0.5)
    delay_print(string_list[1] +'\n')
    delay_print(string_list[2] +'\n')
    
    choice = (input("Input: "))
    
    # Check choice is valid
    if (int_check(choice) and in_range(1, 2, int(choice))) :
        choice = int(choice)
    else:
        print('Provide a valid choice.')
        sleep(0.5)
        student.stats['Intellect'] -= 1
        print('You lost 1 Intellect point!')
        check_stats_gt_zero(student)
    
    # Execute option based on choice
    if (choice == 1):
        option_one(student)
    else:
        option_two(student)
    
    
def three_choices(student, string_list, option_one, option_two, option_three):
    """
    Function for events with two choices
    
    Parameters
    ----------
        student : Student
            Student object making the choice
        string_list: list
            List of strings that prompt the player to  make a choice
        option_one: function
            First option function that continues a path
        option_two: function
            Second option function that continues a path
        option_three: function
            Third option function that continues a path
    Return
    ------
        None
    """
    delay_print('\n' + string_list[0] +'\n')
    sleep(0.5)
    delay_print(string_list[1] +'\n')
    delay_print(string_list[2] +'\n')
    delay_print(string_list[3] +'\n')
    
    choice = (input("Input: "))
    
    # Check choice is valid
    if (int_check(choice) and in_range(1, 3, int(choice))) :
        choice = int(choice)
    else:
        print('Provide a valid choice.')
        sleep(0.5)
        student.stats['Intellect'] -= 1
        print('You lost 1 Intellect point!')
        check_stats_gt_zero(student)
    
    # Execute option basedon choice
    if (choice == 1):
        option_one(student)
    elif (choice == 2):
        option_two(student)
    else:
        option_three(student)

def rand_beg_week_event(student):
    """
    Creates random event at beginning of the week
    
    Parameters
    ----------
        student : Student
            Student object getting altered
    Return
    ------
        None
    """
    # Add hunger every new event
    student.stats['Hunger'] += 1
    check_stats_gt_zero(student)
    
    # String list for each random event
    event_str_list = ['Khosla has announced no more parking!', 
                      'A nice, new boba shop just opened up near campus', 
                      'Tuition has been raised!', 
                      'Raccoons attack you when walking back from your 8PM discussion.', 
                      'You failed something!',
                      'You got sick!']
    
    # Choose a random event
    rand_int = rd.randint(0,5)
    
    # Save random event string
    random_event = event_str_list[rand_int]
    
    delay_print('\n' + random_event + '\n')
    
    # Execute statements based on random event chosen
    if (rand_int == 0):
        delay_print('\nYou now have to walk very long distances to get places.\n')
        print('Hunger has increased by 2!')
        print('Strength has increased by 1!')
        student.stats['HP'] += 2
        student.stats['Strength'] += 1
        check_stats_gt_zero(student)
    elif (rand_int == 1):
        delay_print('\nOf course, you go there and spend money on three different drinks\n')
        print('Hunger has decreased by 4!')
        print('Wealth has decreased by 3!')
        student.stats['HP'] -= 4
        student.stats['Wealth'] -= 3
        check_stats_gt_zero(student)
    elif (rand_int == 2):
        delay_print('\nYou just get more broke.\n')
        print('Wealth has decreased by 2!')
        student.stats['Wealth'] -= 2
    elif (rand_int == 3):
        delay_print('\nYou limp back to your apartment and watch as the raccoons glare menacingly')
        delay_print(' at your door\n')
        print('Health has decreased by 3!')
        print('Luck has decreased by 1!')
        student.stats['HP'] -= 3
        student.stats['Luck'] -= 1
    elif (rand_int == 4):
        delay_print('\nYou feel dumb, but lucky because you weren\'t the lowest score\n')
        print('Health has decreased by 1!')
        print('Intellect has decreased by 1!')
        print('Luck has increased by 2!')
        student.stats['HP'] -= 1
        student.stats['Intellect'] -= 1
        student.stats['Luck'] += 2
    elif (rand_int == 5):
        delay_print('\nYou feel sick.\n')
        print('Health has decreased by 2!')
        student.stats['HP'] -= 2
    
    # Loading effect
    loading(rand_loading_strings()) 
    
    # Go to middle of week
    midweek_prompt(student)
    
def midweek_prompt(student):
    """
    Provides prompts on what the student can do in the middle of the week
    
    Parameters
    ----------
        student : Student
            Student object getting altered
    Return
    ------
        None
    """
    # Add hunger every new event
    student.stats['Hunger'] += 1
    check_stats_gt_zero(student)
    
    # Show choices for what player can do
    delay_print('\nIt\'s the middle of the week and you can do some things. Here are some ')
    delay_print('things:\n')
    delay_print('1. Check inventory\n')
    delay_print('2. Check stats\n')
    delay_print('3. Check major\n')
    delay_print('4. Check courses\n')
    delay_print('5. Enroll in classes\n')
    delay_print('6. Change major\n')
    
    choice = (input("Input: "))
    
    # Check choice is valid
    if (int_check(choice) and in_range(1, 6, int(choice))) :
        choice = int(choice)
    else:
        print('Provide a valid choice.')
        sleep(0.5)
        student.stats['Intellect'] -= 1
        print('You lost 1 Intellect point!')
        check_stats_gt_zero(student)
        midweek_prompt(student)
    
    # Execute method based on choice made
    if (choice == 1):
        student.check_inventory()
        reprompt(student)
    elif (choice == 2):
        student.check_stats()
        reprompt(student)
    elif (choice == 3):
        student.check_major()
        reprompt(student)
    elif (choice == 4):
        student.check_courses()
        reprompt(student)
    elif (choice == 5):
        quarter = str(input('Which quarter?\n'))
        course = str(input('What course?\n'))
        student.enroll(quarter, course)
        reprompt(student)
    elif (choice == 6):
        major = str(input('Which major?\n'))
        student.major_change(major)
        reprompt(student)
    
def end_of_week_choice(student):
    """
    Two end of the week choices (will add more in the future)
    
    Parameters
    ----------
        student : Student
            Student object getting altered
    Return
    ------
        None
    """
    # Randomizes between the first choice or second choice event
    rand_int = rd.randint(0,1)
    
    if ( rand_int == 0 ):
    # First choice event has two choices
        string_list = ['Do you go home?','1. Yes','2. No']
        def option_one(student):
            print('Health has increased by 4!')
            print('Hunger has decreased by 4!')
            print('Luck has increased by 4!')
            student.stats['HP'] += 4
            student.stats['Hunger'] -= 4
            student.stats['Luck'] += 4
            check_stats_gt_zero(student)
            check_weeks(student)
        def option_two(student):
            print('Health has decreased by 4!')
            print('Hunger has increased by 4!')
            print('Luck has decreased by 4!')
            student.stats['HP'] -= 4
            student.stats['Hunger'] += 4
            student.stats['Luck'] -= 4
            check_stats_gt_zero(student)
            check_weeks(student)
        two_choices(student, string_list, option_one, option_two)
    else:
    # Second choice event has three choices
        string_list = ['What do you do this weekend?', '1. Party', '2. Study', '3. Drop out']
        def option_one(student):
            print('Health has decreased by 2!')
            print('Luck has increased by 1!')
            print('Intellect has decreased by 2!')
            print('Strength has increased by 2!')
            student.stats['HP'] -= 2
            student.stats['Luck'] += 1
            student.stats['Intellect'] -=2
            student.stats['Strength'] +=2
            check_stats_gt_zero(student)
            check_weeks(student)
        def option_two(student):
            print('Health has decreased by 2!')
            print('Intellect has increased by 3!')
            print('Strength has decreased by 1!')
            student.stats['HP'] -= 2
            student.stats['Intellect'] += 3
            student.stats['Strength'] -= 1 
            check_stats_gt_zero(student)
            check_weeks(student)
        def option_three(student):
            print('You have successfully dropped out of UCSD. Goodbye.')
            sys.exit(0)
        three_choices(student, string_list, option_one, option_two, option_three)
                 
def reprompt(student):
    """
    Asks if the student wants to do something else in the middle of the week
    
    Parameters
    ----------
        student : Student
            Student object getting altered
    Return
    ------
        None
    """
    # Asks player for choice
    delay_print('\nDo something else?\n')
    delay_print('1. Yes\n')
    delay_print('2. No\n')
        
    choice = (input("Input: "))
    
    # Checks if choice is valid
    if (int_check(choice) and in_range(1, 2, int(choice))) :
        choice = int(choice)
    else:
        print('Provide a valid choice.')
        sleep(0.5)
        student.stats['Intellect'] -= 1
        print('You lost 1 Intellect point!')
        check_stats_gt_zero(student)     
        reprompt(student)
    
    # Executes midweek again if choice is 1, moves on otherwise
    if (choice == 1):
        midweek_prompt(student)
    elif (choice == 2):
        loading(rand_loading_strings()) 
        end_of_week_choice(student)
                    
def in_range(low, high, value):
    """
    Checks if a value is in range
    
    Parameters
    ----------
        low: integer
            Lower end of interval
        high : integer
            Upper end of interval
        value : integer
            Value being checked
    Return
    ------
        True if in range, False if not in range
    """
    if ( (value >= low) and (value <= high) ):
        return True
    else:
        return False
        
def rand_loading_strings():
    """
    Generates an entertaining random loading string
    
    Parameters
    ----------
        None
    Return
    ------
        String
            Loading String for loading function
    """
    # List of loading strings
    loading_strings = ['Looking for parking', 'Sleeping', 'Trying to wake up for your 8AM',
                       'Fighting raccoons', 'Studying for weekly midterms']
    return loading_strings[rd.randint(0, len(loading_strings)-1)]

def check_stats_gt_zero(student):
    """
    Checks that player is still healthy
    
    Parameters
    ----------
        student : Student
            The student being checked
    Return
    ------
        None
    """
    
    # If students stats are too low or too high, they lose
    if (student.stats['HP'] <= 0) :
        delay_print('\nYour health has deteriorated and you\'ve ended up in the hospital ')
        delay_print('and unavailable for the rest of the year.\n')
        sys.exit(0)
    elif (student.stats['Hunger'] > 15):
        delay_print('\nYou starved.\n')
        sys.exit(0)
    elif (student.stats['Intellect'] <= 0):
        delay_print('\nYou were academically disqualified. You couldn\'t cut it for UCSD.\n')
        sys.exit(0)
    elif (student.stats['Strength'] <= 0):
        delay_print('\nYou are too tired to walk around UCSD. You can\'t take it and collapse\n')
        sys.exit(0)
    elif (student.stats['Luck'] <= 0):
        delay_print('\nYou\'re out of luck! All of your exams are just unfair and you fail\n')
        sys.exit(0)
    elif (student.stats['Wealth'] <= 0):
        delay_print('\nYou ran out of money. Those trips to Convoy and boba were too much for ')
        delay_print('your wallet. Not even financial aid can help you. (As if they ever do)\n')
        sys.exit(0)
    else:
        return

def check_weeks(student):
    """
    Checks number of weeks
    
    Parameters
    ----------
        student : Student
            The student being checked
    Return
    ------
        None
    """
    
    # Execute endgame prompts if after finals
    if (student.week == 12):
        delay_print('\nYou made it! Congratulations! Now you just have to wait for your final \
                     scores.\n')
        delay_print('\n Continue to the next quarter? \n')
        delay_print('1. Yes\n')
        delay_print('2. No\n')
        
        choice = (input("Input: "))
    
        if (int_check(choice) and in_range(1, 2, int(choice))) :
            choice = int(choice)
        else:
            print('Provide a valid choice.')
            sleep(0.5)
            student.stats['Intellect'] -= 1
            print('You lost 1 Intellect point!')
            check_stats_gt_zero(student)
            check_weeks(student)
        if (choice == 1):
            delay_print('\n It\'s the beginning of a new quarter!\n')
            loading(rand_loading_strings()) 
            rand_beg_week_event()
        elif (choice == 2):
            sys.exit(0)
    # Begin next week and add one to week 
    else:
        student.week += 1
        loading(rand_loading_strings()) 
        rand_beg_week_event(student)