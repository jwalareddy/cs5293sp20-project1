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
~~~
cs5293p20-project1/
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
## Platform used :
I used Google Cloud Platform to create a VM instance in the cloud. I used it for cloning the Git repository, and made changes using the following github actions.

## Git Repository commands :
Initially we create a private repository in ouy github accounts using the name cs5293p20-project1. We clone the repository link into our Linux environment by using the following command :
~~~
https://github.com/jwalareddy/cs5293sp20-project1.git
~~~
Further changes made to the directory structure are committed to github using the following commands :
~~~
git add -A
git commit -m " appropriate message to be displayed if it is the initial commit or the final commit"
git push origin master 
git pull origin master
~~~
If any errors occur while pushing the data from the linux environment to the github repository, we can use 
~~~
git push origin master --force
~~~
to pull the changes, if any, made from the github repository to our local environment, we use the following command :
~~~
git pull origin master
~~~

## Functions used :
I have created a project1 directory, in which I have 2 files, redactor.py and main.py. 
I have written the init main function in redactor.py 
In the file redactor.py, I have called the main function and the function calling. In the file main.py, I have the individual functions, each for the redaction of names, genders and dates. I have created a directory project1 and the files redactor.py and main.py are stored in those files.
## To run the program:
Go to the directory project1 and run the following python command:
~~~
pipenv run python redactor.py --input '*.txt' \
                    --input 'otherfiles/*.txt' \
                    --names --dates --genders \
                    --concept 'kids' \
                    --output 'files/' \
                    --stats stderr
~~~
## Description of the functions used : 
def names() :
Here, I give the input data as a text file. I used the nltk function to tokenize the text and the individual person names in the text file are stored in a list and redacted with the full unicode block character('\u2588'). I used the concept of tagging to extract the words tagged as PERSON. 

def dates() :
I used the CommonRegex funnction to parse the list of dates in the input file. In the input file that I gave in my program, I gave the date format in the Wikipedia format, which, for example is 18 January, 1996.

def genders() :
I assumed the following gender list, with the given values in the list to be redacted in the input file.
~~~
list_of_genders=['he', 'she', 'himself', 'herself', 'male', 'female', 'him', 'her', 'his',
 'man', 'woman', 'men', 'women', 'husband', 'wife']
 ~~~

These values, if found in the input text file are redacted with the full unicode block character('\u2588'). 

def concepts() :
I used the wordnet package to find the synonyms of the word, the wordnet.synsets() function is used to find the synonyms for any given word, using the following command.
~~~
synon = wordnet.synsets(word)
~~~

def stats() :
Stats takes either the name of a file, or special files (stderr, stdout), and writes a summary of the redaction process. Some statistics to include are the types and counts of redacted terms and the statistics of each redacted file. 

# Sample Outputs : 
# Redacting names :
~~~
Donald John Trump is the 45th and current President of the United States.
██████ ██████████ is the 45th and current President of the United States
~~~

# Redacting dates :
~~~
Check to see if the dates are redacted :
March 30, 2019
January 26, 1948
Check to see if the dates are redacted :
██████████████
██████████████
~~~

# Redacting genders : 
~~~
He is a great leader.
█ is a a great leader.
~~~

## Pytest framework for the project :
I used the Pytest framework in Python to check for the individual test cases for the redaction process. To run the pytest framework, we need to first ensure if we have the pytest installed in our current project directory. I used the following command to install the pytest in my project's execution virtual environment.
~~~
pipenv install pytest
~~~
I have written the test cases for all the three redaction functions. 
def test_names.py  :
Pytest to check if the function names() extracts the names using the appropriate packages and functions from the given input text file. I gave a sample test string, and check whether the number of names returned in the text file are the same as given in the sample string. Checked if the redaction is done. If so, the test case is passed. Else, it is failed.

def test_genders.py :
Pytest to check if the genders function takes the given gender list and redacts them with the required unicode full block character('\u2588'). If so, the test case is passed. Else, it is failed.

def test_dates.py :
Pytest to check if the dates function extracts the dates using the CommonRegex functionality from the given input text file. I gave a sample test string, and checked whether the number of dates that are returned are the same as in the given sample string. Checked if the redaction is done. If so, the test case is passed, else it is failed.

## To run the Pytest : 
I used the following command to run my python tests for the given function.
~~~
 pipenv run python -m pytest
 ~~~
 
Screenshots of successful execution of the main program, without any errors.
https://github.com/jwalareddy/cs5293sp20-project1/issues/1#issue-595426861

