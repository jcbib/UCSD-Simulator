"""
Test for my functions and classes.
"""
import pytest
from functions import *

def test_students():
    """
    Tests methods and attribute changes for student object
    
    Parameters
    ----------
    None
    
    Return
    ------
    None
        
    """
    
    # Initialize new Student Object
    bobert = Student(name='Bobert',major='Cognitive Science')
    
    # Test student initialization
    assert bobert.stats['HP'] == 0
    assert bobert.stats['Hunger'] == 0
    assert bobert.stats['Intellect'] == 0
    assert bobert.stats['Strength'] == 0
    assert bobert.stats['Luck'] == 0
    assert bobert.stats['Wealth'] == 0
    assert bobert.major == 'Cognitive Science'
    assert bobert.course_list['Fall'] == []
    assert bobert.course_list['Winter'] == []
    assert bobert.course_list['Spring'] == []
    assert bobert.inventory == {}
    
    # Check adding items
    bobert.add_item('Glasses')
    bobert.add_item('Pencil')
    
    assert bobert.inventory == {'Glasses' : 1, 'Pencil' : 1}
    
    # Check adding items with different casings
    bobert.add_item('gLasSes')
    bobert.add_item('PenCIL')
    
    assert bobert.inventory == {'Glasses' : 2, 'Pencil' : 2}
    
    # This should print 2 Glasses and 2 Pencils on two lines
    print('Testing check_inventory:')
    bobert.check_inventory()
    print()
    
    # Check randomizing stats
    bobert.rand_stats()
    assert bobert.stats['HP'] != 0
    assert bobert.stats['Hunger'] != 0
    assert bobert.stats['Intellect'] != 0
    assert bobert.stats['Strength'] != 0
    assert bobert.stats['Luck'] != 0
    
    # This should print the stats on different lines
    print('Testing check_stats:')
    bobert.check_stats()
    print()
    
    # This should print 'Cognitive Science'
    print('Testing check_major:')
    bobert.check_major()
    print()
    
    bobert.stat_change('Luck', 50)
    
    # This should change bobert's major
    bobert.major_change('Computer Science')
    print()
    
    assert bobert.major == 'Computer Science'
    
    # This should add courses to bobert's course list
    bobert.enroll('Fall','CSE 11')
    bobert.enroll('Fall','COGS 18')
    bobert.enroll('Fall','cs 2')
    bobert.enroll('Fall','COGS')
    
    assert bobert.course_list['Fall'] == ['CSE 11', 'COGS 18']
    
    
    # This should print out all the quarters and courses in each quarter
    print('Testing check_courses:')
    bobert.check_courses()
    print()
        