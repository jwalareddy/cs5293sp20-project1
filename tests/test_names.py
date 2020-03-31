import pytest
import project1

from project1 import main

data = 'The instructor for this course is Professor Christan Grant. The TA for this course is Mary Hirsh. We have another TA for this course who is Keerthi Banweer. Jwala Katta is a graduate student in this ocurse. She is good with academics. He is a great professor. Josh Mary lives on the edge of the sea'

def test_names():
    d, names_list = main.names(data)
    
    assert len(names_list) == 4
    assert len(names_list) == d.count('\u2588')
