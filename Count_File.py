"""
source_rakumo = [{'name':'eee.py'}, {'name':'aaa.py'}, {'name':'bbb.html'}, {'name':'ccc.js'}, {'name':'ccc', 'items':[{'name':'aaa.py'}, {'name':'bbb.html'}, {'name':'ccc', 'items':[{'name':'aaa.py'}, {'name':'bbb.html'}]}]},{'name':'ccc', 'items':[{'name':'aaa.py'}, {'name':'bbb.html'}, {'name':'ccc', 'items':[{'name':'aaa.py'}, {'name':'bbb.html'}]}]}, {'name':'aaa.py'}, {'name':'bbb.py'}]
file_extension = ".py"


"""
import re
import os

""" 
def directory(path, extension):
    list_dir = []
    list_dir = os.listdir(path)
    count = 0
    for file in list_dir:
        if file.endswith(extension):
            count += 1
    return count

source_rakumo = [{'name':'eee.py'}, {'name':'aaa.py'}, {'name':'bbb.html'}, {'name':'ccc.js'}, {'name':'ccc', 'items':[{'name':'aaa.py'}, {'name':'bbb.html'}, {'name':'ccc', 'items':[{'name':'aaa.py'}, {'name':'bbb.html'}]}]},{'name':'ccc', 'items':[{'name':'aaa.py'}, {'name':'bbb.html'}, {'name':'ccc', 'items':[{'name':'aaa.py'}, {'name':'bbb.html'}]}]}, {'name':'aaa.py'}, {'name':'bbb.py'}]

file_extension = ".py"
directory(source_rakumo, file_extension)

"""




