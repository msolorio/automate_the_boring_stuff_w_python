"""
isPhoneNumber - returns boolean indicating if string matches format

xxx-xxx-xxxx where all x's are decimal numbers
"""
# /d{3}-\d{3}-\d{4}

import re

phone_num_regex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

# Searches for the first occurence
# match_object = phone_num_regex.search('this is a string - 619-100-1000, 858-222-2222')

# Searches for all occurences
match_object = phone_num_regex.findall('this is a string - 619-100-1000, 858-222-2222')

if (match_object):
    print(match_object)
