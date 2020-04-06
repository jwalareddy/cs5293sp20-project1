import pytest
import project1

from project1 import main

text = 'The instructor for this course is Professor Christan Grant. The TA for this course is Mary Hirsh. We have another TA for this course who is Keerthi Banweer. Jwala Katta is agraduate student in this course. She is good with academics. He is a great professor. Josh Mary lives on the edge of the sea. The instructor for this course is Professor Christan Grant. The TA for this course is Mary Hirsh. We have another TA for this course who is Keerthi Banweer. Jwala Katta is a graduate student in this ocurse. She is good with academics. He is a great professor. Josh Mary lives on the edge of the sea. I am born on January 28, 1997. March 1, 2020 is a great day in history. He is born on May 10, 1998. Josh was born on June 12, 2020.'

def test_dates():
    d, list_of_dates = main.dates(text)   
    assert len(list_of_dates) == 1

