import pytest
import project1

from project1 import main

text = 'The instructor for this course is Professor Christan Grant. The TA for this course is Mary Hirsh. We have another TA for this course who is Keerthi Banweer. Jwala Katta is agraduate student in this course. She is good with academics. He is a great professor. Josh Mary lives on the edge of the sea. I met her on a fine Sunday. She seems like a great girl. He is naughty but he is intelligent.'

def test_genders():
    value, list_of_genders  = main.genders(text)
    assert value is not None
