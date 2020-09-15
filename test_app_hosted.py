#########################################################################
#
# @file name: test_app_hosted.py
# @purpose: test file of backend app on hosted heroku instance
# @out_of_scope: no need to test every possible error. that is conducted
# in the unit tests. Mostly testing permissions here with a few error
# conditions added
# @author: Tony Burge
# @date: 2020-09-12
#
#########################################################################
#
#
# global imports
import requests
from flask import abort
from random import randint
#
# local imports
from test_config import ACCTS
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
    print("\n" * 50)
    print("#" * 80)
    print("Testing Casting Application deployed on Heroku")
    print("Submitted by Tony Burge")
    print("#" * 80)

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
        for item in resource_list:
            res = (requests.delete(URL + f"{resource}/" + str(item['id']),
                   headers=header))

# function to get actor or movie list based on "resource" argument passed
def get_resource(acct, resource):
    #
    url = URL + resource
    header = {
      "Authorization": f"Bearer {acct['jwt']}",
      "Content-Type": "application/json"
    }
    res = requests.get(url, headers=header)
    if res.json()['success']:
        resource_list = res.json()[f'{resource}']
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

# function to update actor or movie based on "resource" argument based
def update_resource(acct, resource, payload, id):
    #
    url = URL + resource + "/" + str(id)
    header = {
      "Authorization": f"Bearer {acct['jwt']}",
      "Content-Type": "application/json"
    }
    res = requests.patch(url, data=payload, headers=header)

# main app
#
print_greeting()
#
# traverse each account type and perform hosted tests
for acct in ACCTS:
    #
    print("\n" * 2)
    print("--------------------------------------------------------------")
    print(f">>> Testing: {acct['type']}")
    #
    # clean database with executive producer each time. This is to ensure
    # data is all clear before testing. Should work unless JWT for exec
    # producer has expired or if records do not exist
    print("\n* Cleaning databased using executive producer for next role test")
    clean_database(acct)
    #
    # -----------------------------------------------------------------------
    # add actors - properly formatted, should work unless user does not have
    # permission or if JWTs have expried
    print("\n* Adding actors: should pass if use has permission *")   
    # for actor in ACTORS:
    #     add_actor(acct, actor)
    payload = ""
    for actor in ACTORS:
        payload = ('{"name": ' + '"' + actor[0] + '"' + ', "dob": ' + '"' +
                   actor[1] + '"' + ', "gender": ' + '"' + actor[2] + '"}')
        add_resource(acct, "actors", payload)
    #
    # add actor with missing data. this should fail even if user
    # has permission to add actor
    print("\nMissing data. Should fail regardless of permission.")
    payload = '{"name": "Jonny Depp"}'
    add_resource(acct, "actors", payload)

    #
    # -----------------------------------------------------------------------
    # add movies - properly formatted, should work unless user does not have
    # permission or if JWTs have expried
    # first must find ID of actors
    print("\n* Adding movies: should pass if user has permission *")       
    actor_list = get_resource(acct, "actors")
    if len(actor_list) == 0:
        print("No actors available to add movies. Check permissions " +
              "when adding actors.")
    else:
        for movie in MOVIES:
            payload = ('{"title": ' + '"' + movie[0] + '"' +
                       ', "release_date": ' + '"' + movie[1] + '"' +
                       ', "cast": ' + '[')
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
    #
    # add movie with missing field(s). this should fail regardless of
    # permissions
    print("\nMissing data. Should fail regardless of permission.")
    payload = '{"title": "Raising Arizona"}'
    add_resource(acct, "actors", payload)   
    #
    # add movie with empty cast list. this should fail regardless of
    # permissions
    print("\nEmpty cast list. Should fail regardless of permission.")
    payload = ('{"title": "Raising Arizona", "release_date":' +
               ' "01/01/2000", "cast": []}')
    add_resource(acct, "actors", payload)   
    #
    # -----------------------------------------------------------------------
    # update actor
    print("\n* Updating actor record: should pass if user has permission *")       
    actor_list = get_resource(acct, "actors")
    if len(actor_list) == 0:
        print("No actors available to update. Check permissions " +
              "when adding actors.")
    # update first record available
    else:
        actor = actor_list[0]
        payload = '{"name": "UpdateTest Actor"}'
        print("...attempting to update", actor)
        print("...with " + payload)
        update_id = actor['id']
        update_resource(acct, "actors", payload, update_id)
        #
        # get new actor list to verify
        actor_list = get_resource(acct, "actors")
        for actor in actor_list:
            if actor['id'] == update_id:
                print("...updated: ", actor)
                break
    #
    # -----------------------------------------------------------------------
    # update movie
    print("\n* Updating movie record: should pass if user has permission *")       
    movie_list = get_resource(acct, "movies")
    if len(movie_list) == 0:
        print("No movies available to update. Check permissions " +
              "when adding movies.")
    # update first record available
    else:
        movie = movie_list[0]
        payload = '{"title": "The Updated Movie"}'
        print("...attempting to update", movie)
        print("...with " + payload)
        update_id = movie['id']
        update_resource(acct, "movies", payload, update_id)
        #
        # get new movie list to verify
        movie_list = get_resource(acct, "movies")
        for movie in movie_list:
            if movie['id'] == update_id:
                print("...updated: ", movie)
                break


    #
    # -----------------------------------------------------------------------
    # delete actor

    #
    # -----------------------------------------------------------------------
    # delete movie


