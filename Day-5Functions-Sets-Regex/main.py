# Problem Statement:
# A function find_unique_words(paragraph) that takes a string paragraph as input. 
# The function should return a set of unique words from the paragraph.
import re

def remove_punctuation(doc):
    return re.sub(r'[^\w\s]','',doc)

def find_unique_words(paragraph):
    updated_paragraph = remove_punctuation(paragraph).lower().split()
    word_set = set()
    for word in updated_paragraph:
        word_set.add(word)
    print(word_set)

text = input("Enter the text to remove duplicate words : ")
find_unique_words(text)


# Problem Statement - 2:
# Validate if an email address is correctly formatted.
# Requirements:
# The email should contain exactly one @ symbol.
# There should be a domain name after the @ symbol.
# The domain should contain at least one dot (.) after the domain name.

def validate_email(email):
    email_pattern = r'^[A-Za-z0-9.%/+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$'
    return bool(re.match(email_pattern,email))

email = input("Enter the email-id to check if it is valid : ")
print(validate_email(email))

# Problem Statement - 3:
# Extract valid phone numbers from a given text.
# Requirements:
# Phone numbers can be in the following formats:
# (123) 456-7890
# 123-456-7890
# 1234567890

def validate_phone(phone_numbers):
    mobile_pattern = r'\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}'
    return re.findall(mobile_pattern,phone_numbers)

mobile = input("Enter the mobile to check if it is valid : ")
print("If valid you will get entered mobile number.")
print(validate_phone(mobile))