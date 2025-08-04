import sqlite3
connection = sqlite3.connect('python_releases.db') # create database



releaselist = [
    # (version, date, status, features) 
    ('Python 2.7', '2010-07-03', 'EOL (2020)', 'Legacy projects only'),
    ('Python 3.0', '2008-12-03', 'Deprecated', 'Unicode strings, print function'),
    ('Python 3.6', '2016-12-23', 'Deprecated', 'f-strings, async generators'),
    ('Python 3.7', '2018-06-27', 'Deprecated', 'dataclasses, breakpoint()'),
    ('Python 3.8', '2019-10-14', 'Deprecated', 'walrus operator :='),
    ('Python 3.9', '2020-10-05', 'Deprecated', 'type hinting, dict merge'),
    ('Python 3.10', '2021-10-04', 'Deprecated', 'structural pattern matching'),
    ('Python 3.11', '2022-10-24', 'Stable', '10-60% faster performance'),
    ('Python 3.12', '2023-10-02', 'Stable', 'better debugging, flexible f-string'),
    ('Python 3.13', 'Coming Oct 2024', 'Pre-release', 'removing deprecated features')
]

 

connection.close() # close database