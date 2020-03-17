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
k = 0
count = 0

ext = file_extension.split(".")[-1]  # lay dc gia tri 'py'


def countFile01(x, count):
    for data in x:
        if "py" in data['name']:  # trong thu muc co file .py nao khong
            count += 1
        if 'items' in data:  # kiem tra xem trong thu muc data co thu muc item con nao khong
            for value in data['items']:
                if "py" in value['name']:
                    count += 1
    return count


def couter(source, count):
    for key in source_rakumo:
        if "py" in key['name']:
            count += 1
        m = key.values()
        for x in m:
            if type(x) == list:
                k = countFile01(x, count)
    result = count + k
    print(result)


couter(source_rakumo, 0)
