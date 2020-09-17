import os
#
# test data for test_app.py
#
# jwts
jwt_ep = os.getenv('jwt_ep')
jwt_cd = os.getenv('jwt_cd')
jwt_ca = os.getenv('jwt_ca')
jwt_no = os.getenv('jwt_no')

######################################################################
# UNIT/LOCAL TESTING VARIABLES
######################################################################
#
# good add record
movie1 = {"title": "Rainy Days", "release_date": "7/4/2011", "cast": [1, 3]}
# cast list empty
movie2 = {"title": "Racing Rain", "release_date": "6/3/2017", "cast": []}
# missing one or more required fields
movie3 = {"title": "Racing Rain", "cast": [1, 2]}
# good add record
actor1 = {"name": "Marion Johnson", "dob": "8/13/1959", "gender": "F"}
# missing one or more required fields
actor2 = {"name": "Jordan Phelps", "dob": "12/13/1970"}
# good update record
umovie1 = {"title": "Flight Plan"}
# no recognizable fields
umovie2 = {"uselessfield": "whatever"}
# cast list empty
umovie3 = {"title": "Flight Plan 2", "cast": []}
# good update record
uactor1 = {"name": "Joel Blankenship", "dob": "4/3/1981"}
# no recognizable fields
uactor2 = {"uselessfield": "whatever"}

######################################################################
# HOSTED TESTING VARIABLES
######################################################################
#
# account list for use in hosted testing
ACCTS = [
    {'type': 'Executive Producer', 'jwt': jwt_ep},
    {'type': 'Casting Director', 'jwt': jwt_cd},
    {'type': 'Casting Assistant', 'jwt': jwt_ca},
    {'type': 'General Public', 'jwt': jwt_no},
]
#
# data
#
ACTORS = [
    ["Marion Johnson", "8/13/1959", "F"],
    ["Ashton Phelps", "4/3/1973", "M"],
    ["Fredrik Popolo", "3/21/1985", "M"],
    ["Georgette Milton", "12/4/1991", "F"],
    ["Francis Beckham", "5/6/1964", "F"],
    ["Floyd Bergman", "1/3/1959", "M"]
]

MOVIES = [
    ["Racing the Rain", "7/4/2011"],
    ["Field of Illusions", "3/5/1995"],
    ["Flight Train", "11/30/2020"]
]
