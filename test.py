""""
Author: Nguyen Van Dat
Date: 17/03/2020
"""
"""
INPUT: 
source_rakumo = [{'name':'eee.py'}, {'name':'aaa.py'}, {'name':'bbb.html'}, {'name':'ccc.js'}, {'name':'ccc', 'items':[{'name':'aaa.py'}, {'name':'bbb.html'}, {'name':'ccc', 'items':[{'name':'aaa.py'}, {'name':'bbb.html'}]}]},{'name':'ccc', 'items':[{'name':'aaa.py'}, {'name':'bbb.html'}, {'name':'ccc', 'items':[{'name':'aaa.py'}, {'name':'bbb.html'}]}]}, {'name':'aaa.py'}, {'name':'bbb.py'}]
file_extension = ".py"

OUTPUT: 8 

"""

source_rakumo = [{'name': 'eee.py'}, {'name': 'aaa.py'}, {'name': 'bbb.html'}, {'name': 'ccc.js'}, {'name': 'ccc',
                                                                                                    'items': [{
                                                                                                        'name': 'aaa.py'},
                                                                                                        {
                                                                                                            'name': 'bbb.html'},
                                                                                                        {
                                                                                                            'name': 'ccc',
                                                                                                            'items': [
                                                                                                                {
                                                                                                                    'name': 'aaa.py'},
                                                                                                                {
                                                                                                                    'name': 'bbb.html'}]}]},
                 {'name': 'ccc', 'items': [{'name': 'aaa.py'}, {'name': 'bbb.html'},
                                           {'name': 'ccc', 'items': [{'name': 'aaa.py'}, {'name': 'bbb.html'}]}]},
                 {'name': 'aaa.py'}, {'name': 'bbb.py'}]
file_extension = ".py"
count = 0


def checkFile(y, count):
    for key in y:
        if ".py" in key['name']:
            count += 1
            return count


k = 0
for x in source_rakumo:
    if ".py" in x['name']:
        k += 1
    for y in x.values():
        if type(y) == list:
            k += checkFile(y, count)
            for index in y:
                if "items" in index:
                    k += checkFile(index['items'], count)
print(k)
