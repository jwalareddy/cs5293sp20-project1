import pytest
import project1

from project1 import main

text = 'The instructor for this course is Professor Christan Grant. The TA for this course is Mary Hirsh. We have another TA for this course who is Keerthi Banweer. Jwala Katta is agraduate student in this course. She is good with academics. He is a great professor. Josh Mary lives on the edge of the sea.'

def test_names():
    name_list = main.names(text)    
    assert name_list is not None

