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
def clean_database(acct):
    #
    header = {
        "Authorization": f"Bearer {acct['jwt']}",
        "Content-Type": "application/json"
    }
    for resource in ["movies", "actors"]:
        resource_list = get_resource(acct, resource)
        if len(resource_list) == 0:
            print(f"Error deleting {resource}. Either no {resource} exist, " +
                  "or the user does not have permission/JWTs expired")
        for item in resource_list:
            if resource == "actors":
                print(f"...attempting to delete actor: {item['name']}...", end='')
            else:
                print(f"...attempting to delete movie: {item['title']}...", end='')
            res = requests.delete(URL + f"{resource}/" + str(item['id']), headers=header)               
            if res.json()['success']:
                print("Success")
            else:
                print("Failed")

# function to get actor or movie list based on "resource" argument passed
def get_resource(acct, resource):
    #
    url = URL + resource
    header = {
      "Authorization": f"Bearer {acct['jwt']}",
      "Content-Type": "application/json"
    }
    print("\n\n\nIn get_resource:", url)




    # TODO: some project here where id is not returned
    res = requests.get(url, headers=header)
    if res.json()['success']:
        resource_list = res.json()[f'{resource}']
        # TODO:
        # this does not return movie id for some reason?
        print("----> resource_list from get_resource")
        print("----> URL: ", url)
        print("----> header: ", header)
        print("----> list: ", resource_list)
    else:
        resource_list = []
    return resource_list





# function to add new actor or movie based on "resource" agrument passed
def add_resource(acct, resource, payload):
    #
    url = URL + resource
    header = {
      "Authorization": f"Bearer {acct['jwt']}",
      "Content-Type": "application/json"
    }
    res = requests.post(url, data=payload, headers=header)
    print("...attempting to add: " + payload + "...", end ='')
    print("with results:", res.json()['success'])


# main app
#
print_greeting()
#
# traverse each account type and perform hosted tests
for acct in ACCTS:
    print("\n" * 2)
    print("--------------------------------------------------------------")
    print("* Clean up database for next account test *")
    print("--------------------------------------------------------------")
    print(f">>> Testing: {acct['type']}")
     #
    # clean datase for each run - should work unless user does not have
    # permissions or if JWTs have expired
    clean_database(acct)
    #
    # -----------------------------------------------------------------------
    # add actors - properly formatted, should work unless user does not have
    # permission or if JWTs have expried
    print("\n* Adding actors *")   
    # for actor in ACTORS:
    #     add_actor(acct, actor)
    payload = ""
    for actor in ACTORS:
        payload = ('{"name": ' + '"' + actor[0] + '"' + ', "dob": ' + '"' +
                   actor[1] + '"' + ', "gender": ' + '"' + actor[2] + '"}')
        add_resource(acct, "actors", payload)
    # TODO add actor with missing data

    #
    # -----------------------------------------------------------------------
    # add movies - properly formatted, should work unless user does not have
    # permission or if JWTs have expried
    # first must find ID of actors
    print("\n* Adding movies *")       
    #actor_list = get_actors(acct)
    actor_list = get_resource(acct, "actors")
    if len(actor_list) == 0:
        print("No actors available to add movies. Check permissions when adding actors.")
    else:
        for movie in MOVIES:
            payload = ('{"title": ' + '"' + movie[0] + '"' + ', "release_date": ' +
                       '"' + movie[1] + '"' + ', "cast": ' + '[')
            # choose random number to determine how many actors to add to movie
            # to match actor_list indeces, had to modify with -1 on len
            # then add one to represent a number from 1 to actors
            cast_num = randint(0, len(actor_list) - 1) + 1
            for x in range (0, cast_num):
                payload += str(actor_list[x]['id'])
                if x != cast_num - 1:
                    payload += ", "
            payload += "]}"
            add_resource(acct, "movies", payload)
    # TODO add movie with missing fields, no cast, and wrong actor IDs

    #
    # -----------------------------------------------------------------------
    # update actor

    #
    # -----------------------------------------------------------------------
    # update movie

    #
    # -----------------------------------------------------------------------
    # delete actor

    #
    # -----------------------------------------------------------------------
    # delete movie


