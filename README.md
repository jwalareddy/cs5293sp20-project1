# cs5293sp20-project1
# Project1 - Redactor
The Redactor is a program for hiding sensitive information such as Names, and places from the public. Whenever sensitive information is shared with the public, the data must go through a redaction process. That is, all sensitive names, places, and other sensitive information must be hidden. Documents such as police reports, court transcripts, and hospital records all containing sensitive information. Redacting this information is often expensive and time consuming.
In this project, we will use our knowledge of Python and Text Analytics to design a system that accept plain text documents then detect and redact “sensitive” items. 

## Setting up the Initial installations 
We run the following installations in the project's virtual environment. Even if the installations are done in the Python environment, in the project's virtual environment, there might be an error popping up "no module named nltk"
~~~
pipenv install nltk
pipenv install re
pipenv install CommonRegex
pipenv install numpy
~~~

## List of files
cs5293p20-project1/
~~~

├── COLLABORATORS
├── LICENSE
├── Pipfile.lock
├── README.md
├── Pipfile
├── project1
│ ├── redactor.py
│ └── main.py
├── files
│ ├── Donald.redacted
│ ├── Trump.redacted
  ├── Obama.redacted
  └── otherfiles
    ├──Ivanka.redacted
    ├──Melania.redacted
    └──Michelle.redacted
├── otherfiles
│ ├── Ivanka.txt
│ ├── Melania.txt
  └── Michelle.txt
├── stats
  └── stats.txt
├── setup.cfg
├── setup.py
├── .gitignore
├── Donald.txt
├── Obama.txt
├── Trump.txt
├── tests
  ├── test_names.py
  ├── test_genders.py
  └── test_dates
~~~  


