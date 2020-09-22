import re

# passes an open text file through this function with a start and end string to return what is between those two values.


def text_gathering(opened_file, start_identifier, end_identifier):
    start = opened_file.find(start_identifier)
    end = opened_file.find(end_identifier)
    return opened_file[start:end]


# This is specifically used to return the location, to the end of the text file (used here for references)
def text_references(opened_file, start_identifier):
    start = opened_file.find(start_identifier)
    return opened_file[start:]

# Identifying the keywords:


def keywords_text(opened_file, start_identifier, end_identifier):
    start = opened_file.find(start_identifier)
    end = opened_file.find(end_identifier)
    return opened_file[start:end]


test_string = '''Key words: ambulation responses, microswitches, multiple disabilities, indices of happiness,
contingency, quality of life, social validation

Children with severe to profound develop-
mental, disabilities
sometimes present with gait and posture'''


print(keywords_text(test_string, 'Key words:', 'posture'))


# Open file With context manager
with open('txt_files/article0.txt', 'r') as f:
    f_contents = f.read()
    print(keywords_text(f_contents, 'Key words', 'METHOD'))
    print(text_gathering(f_contents, "METHOD", "RESULTS"))
    print(text_gathering(f_contents, "RESULTS", "REFERENCES"))
    print(text_references(f_contents, "REFERENCES"))
