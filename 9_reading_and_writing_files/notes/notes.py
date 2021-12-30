import os
from pathlib import Path

###################################################################
# use the path function to join path members into a single path
# Accounts for various OS's
# my_path = Path('spam', 'bacon', 'eggs') # /spam/bacon/eggs
# print(my_path)

###################################################################
# my_files = ['accounts.txt', 'details.csv', 'invite.docx']

# for filename in my_files:
#     print(Path('/User/michael', filename))

###################################################################
# home_folder = Path('/User/michael')
# sub_folder = Path('spam')

# full_path = home_folder / sub_folder

# print(full_path)

###################################################################
# Current Working Directory
# print(Path.cwd())

# os.chdir('/Users/michael')

# print(Path.cwd())

###################################################################

# Get home dir
# print(Path.home())

# Make dir
# os.makedirs('test')

# Make nested dirs
# Creates ./test1/test2/test3
# os.makedirs(Path('test1', 'test2', 'test3'))

# Convert relative path to absolute path
# print(os.path.abspath('.')) # takes in a relative path as argument
# print(os.path.abspath('..'))

# Get a relative path from one location to another
# print(os.path.relpath('/System', '/Library'))
# returns '../System'

# Parts of a path
# p = Path.cwd()

# print('p.anchor:', p.anchor)
# print('p.parent:', p.parent)
# print('p.name:', p.name)
# print('p.stem:', p.stem)
# print('p.suffix:', p.suffix) # .txt
# print('p.drive:', p.dive) # doesn't exist on linux / MacOS

####################################################
# os.path.dirname() will give full path up to parent dir
# print(os.path.dirname(Path.cwd()))

####################################################
# Basename will print the final section of the path
# print(os.path.basename(Path.cwd()))

# get current dir and convert to a string
# current_dir = str(Path.cwd())
# print(current_dir)

# # convert path string into list separating by os separator
# print(current_dir.split(os.sep))


############################################################
# GET FILE SIZE

# test_file_path = Path(Path.cwd(), 'test_file.txt')
# test_file_path2 = Path(Path.cwd(), 'test_file2.txt')

# # print(test_file_path)

# # returns the file size in bytes of the given file
# file_size = os.path.getsize(test_file_path)
# print(file_size)

# file_size2 = os.path.getsize(test_file_path2)
# print(file_size2)

# Print file size of random server.js file
# print(os.path.getsize(Path(Path.home(), 'Code', 'Express', 'stuff-exchange', 'server.js')))

############################################################
# GET CONTENTS OF DIRECTORY
# returns a list of directory contents
# print(os.listdir(Path.cwd()))

# lists contents of the home dir
# print(os.listdir(Path.home()))

############################################################

# Print out size of all current files
# current_files = os.listdir(Path.cwd())

# print(current_files)

# for file in current_files:
#     file_size = os.path.getsize(Path(Path.cwd(), file))
#     print('file size:', file_size)

############################################################
# Print out sum of current directory contents' size

# total_size = 0

# for file in current_files:
#     total_size += os.path.getsize(Path(Path.cwd(), file))

# print('total size:', total_size)

############################################################
# Print filenames that match a 'glob' pattern
# current_path = Path(Path.cwd())

# get current path's glob and conver to a list
# current_files = list(current_path.glob('*'))
# print(current_files)

# returns all files with .txt extension
# current_files = list(current_path.glob('*.txt'))
# print(current_files)

# ? matches any single character
# current_files = list(current_path.glob('test_file?.txt'))
# print(current_files)

####################################################################
# Check if path exists
# p = Path.cwd()
# print(p.exists())
# print(Path(p, 'another_dir').exists()) # checks if ./another_dir exists

# Check if file exists
# file_to_check = Path(Path.cwd(), 'test_file.txt')
# file_to_check2 = Path(Path.cwd(), 'test_fileeee.txt')

# print(file_to_check.is_file())
# print(file_to_check2.is_file())

# Check if directory exists
# dir_to_check.is_dir() # => True / False


####################################################################
# Write to file
# p = Path('spam.txt')

# creates new file and writes to it
# p.write_text('hello world!')

# ####################################################################
# # read file
# print(p.read_text())


# ####################################################################
# hello_file_path = Path.cwd() / 'test_file.txt'

# opened file in read mode
# opened_file = open(hello_file_path)
# read file
# print(opened_file.read())
# return list of lines of file
# print(opened_file.readlines())
# opened_file.close()

# ####################################################################
# surfboards_file = open('surfboards.txt', 'w')

# surfboards_file.write('long board\nfish\nfunboard\n')
# surfboards_file.close()

# ####################################################################
# Shelving / storing data to a file as a key value pair
# Saving to hard drive for later use
# Doesn't have to be openned in write mode
# import shelve

# shelf_file = shelve.open('mydata')

# cats = ['Zoe', 'Pooka', 'Simon']

# shelf_file['cats'] = cats

# shelf_file.close()

# ####################################################################
# Read shelved binary data from file from the key / value pair
# shelf_file = shelve.open('mydata')

# # # print(type(shelf_file))

# print(shelf_file['cats'])
# print(len(shelf_file)) # can get the num of properties
# print(len(shelf_file['cats'])) # can interact with cats list just like any python list
# shelf_file.close()

# ####################################################################
# import shelve

# shelf_file = shelve.open('mydata')

# print(list(shelf_file.keys()))
# print(list(shelf_file.values()))

# ####################################################################
# Can use pprint.pformat to format python code to write to another python file
# import pprint

# cats = [
#     { 'name': 'Zoe', 'desc': 'chubby' },
#     { 'name': 'Tim', 'desc': 'friendly' },
#     { 'name': 'Layla', 'desc': 'scaredy-cat' }
# ]

# cats_file = open('cats.py', 'w')
# cats_file.write(f'cats = {pprint.pformat(cats)}\n')
# cats_file.write(f'cats = {cats}\n')
# cats_file.close()
