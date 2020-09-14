#
# all get/post/delete/patch errors are handled by deployed app except expired JWTs
# in parsing methods in this app. for the pupose of this quick hosted test app,
# I am not handling those errors
#
# global imports
import requests
from flask import abort
from random import randint
#
# local imports
from test_config import jwt_ep, jwt_cd, jwt_ca, jwt_no, ACCTS
from test_config import movie1, movie2, movie3, actor1, actor2
from test_config import umovie1, umovie2, umovie3, uactor1, uactor2
from test_config import ACTORS, MOVIES

#
# constants
URL = "https://burgefsndcapstone.herokuapp.com/"

#############################################################################
# helper functions
#############################################################################
#
# display greeting
def print_greeting():
    print("\n" * 10)
    print("#" * 50)
    print("Testing Casting Application deployed on Heroku")
    print("Submitted by Tony Burge")
    print("#" * 50)

# delete all entries. this will clear the N:M table since requests
# are ran through deployed python using SQL Alchemy ORM
def clean_database():
    #
    # delete actors
    header = {
        "Authorization": f"Bearer {jwt_ep}",
        "Content-Type": "application/json"
    }
    res = requests.get(URL + "actors", headers=header)
    for item in res:
        print(item)
    if res is None:
        print("*** ACCESS ERROR: CHECK JWTs ***")
    else:
        actor_list = res.json()['actors']
        for actor in actor_list:
            res = requests.delete(URL + "actors/" + str(actor['id']), headers=header)        
    #
    # delete movies
    res = requests.get(URL + "movies", headers=header)
    movie_list = res.json()['movies']
    for movie in movie_list:
        res = requests.delete(URL + "movies/" + str(actor['id']), headers=header)

# function to get actor list
def get_actors(acct):
    #
    url = URL + "actors"
    header = {
      "Authorization": f"Bearer {acct['jwt']}",
      "Content-Type": "application/json"
    }
    res = requests.get(URL + "actors", headers=header)
    actor_list = res.json()['actors']
    return actor_list

def get_movies(acct):
    #
    url = URL + "movies"
    header = {
      "Authorization": f"Bearer {acct['jwt']}",
      "Content-Type": "application/json"
    }
    res = requests.get(URL + "movies", headers=header)
    movie_list = res.json()['movies']
    return movie_list

# function to add new actor or movie based on "resource" agrument passed
def add_resource(acct, resource, payload):
    #
    url = URL + resource
    header = {
      "Authorization": f"Bearer {acct['jwt']}",
      "Content-Type": "application/json"
    }
    res = requests.post(url, data=payload, headers=header)
    print("adding: " + payload + "...", end ='')
    for entry in res:
        print("with results:", entry)


# main app
#
print_greeting()

for acct in ACCTS:
    print("\n" * 2)
    print("--------------------------------------------------------------")
    print("* Clean up database for next account test *")    
    print(f"Testing: {acct['type']} - if not Executive Producer or " +
          "Casting Director, this should fail")
 
    clean_database()
    #
    # add actors
    print(f"for {acct['type']}")
    # for actor in ACTORS:
    #     add_actor(acct, actor)
    payload = ""
    for actor in ACTORS:
        payload = ('{"name": ' + '"' + actor[0] + '"' + ', "dob": ' + '"' +
                   actor[1] + '"' + ', "gender": ' + '"' + actor[2] + '"}')
        add_resource(acct, "actors", payload)
    #
    # add movies
    # first must find ID of actors
    actor_list = get_actors(acct)
    for movie in MOVIES:
        payload = ('{"title": ' + '"' + movie[0] + '"' + ', "release_date": ' +
                   '"' + movie[1] + ', "cast": ' + '[')
        cast_num = randint(1, len(actor_list))
        for x in range (1, cast_num):
            print(actor_list[x -1])
            payload += str(actor_list[x-1]['id'])
            if x != cast_num - 1:
                payload += ", "
        payload += "]}"
        print(payload)
        add_resource(acct, "movies", payload)






# for each acount type/jwt, run each test
