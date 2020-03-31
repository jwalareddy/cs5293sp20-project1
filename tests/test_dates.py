import pytest
import project1

from project1 import main

data = 'The instructor for this course is Professor Christan Grant. The TA for this course is Mary Hirsh. We have another TA for this course who is Keerthi Banweer. Jwala Katta is a gradua te student in this ocurse. She is good with academics. He is a great professor. Josh Mary live s on the edge of the sea''The instructor for this course is Professor Christan Grant. The TA for this course is Mary Hirsh. We have another TA for this course who is Keerthi Banweer. Jwala Katta is a gradua te student in this ocurse. She is good with academics. He is a great professor. Josh Mary live s on the edge of the sea. I am born on January 28, 1997. March 1, 2020 is a great day in history. He is born on May 10, 1998. Josh was born on June 12, 2020.'

def test_dates():
    d, dates_list = main.dates(data)
    
    assert len(dates_list) == 1
    assert len(dates_list) == d.count('\u2588')
