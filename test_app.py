#########################################################################
#
# @file name: test_app.py
# @purpose: test file of backend app
# @author: Tony Burge
# @date: 2020-09-09
#
#########################################################################
#
# global imports
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
#
# local imports
from app import create_app
from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth
#
# jwt tokens for testing
# TODO: Update these immediately prior to submitting for review
jwt_ep = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZIWG9XTGFJZk1od0tERjh2TEtTWiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZmluYWxwcm9qZWN0LWJ1cmdlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjU3YjBkOGY3YmUyZjAwNmU3YTg2ZDAiLCJhdWQiOiJtYW5hZ2VtZW50IiwiaWF0IjoxNTk5Nzc2MzQ4LCJleHAiOjE1OTk4NjI3NDgsImF6cCI6ImFDQTdFakF1VFcxaDhjWUJTOEJuUHo5bEtYdktxbGJNIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.IRR2yBlG_MT2AapeD1PTnUNdy8hri5CCQVJj7p_WqTDa-rpsvBhRwKAYZpAP9xaaOLo5qxRaVlzXWXI_rWXz5nlCqWM0hzzJRjPsbabYUSejccJZ4H8_FV7hRU93Jse0yw6gL1rQFBawivsi9y6NPsVk0Ppz126j4tBn3FuhB71T50-m0EVeK_siqdYSyuJndULbjX5nABH1V5JZ49wJsllVQHRxgwaqk74HkLOLXyySCP_ylZWG-OxCjPSlZlqx4n9UA0jA5fCQUG6A5G3TvAwxYT3iIMI2vG6vPu6y2xtUXeKeCccHs6BZ5LaLWqyoDIq9sqU0Sio-4F6uytGzzQ"
jwt_cd = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZIWG9XTGFJZk1od0tERjh2TEtTWiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZmluYWxwcm9qZWN0LWJ1cmdlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjU3YjBmNjA4MjRmOTAwNmVjOWQxZGMiLCJhdWQiOiJtYW5hZ2VtZW50IiwiaWF0IjoxNTk5Nzc2NDA3LCJleHAiOjE1OTk4NjI4MDcsImF6cCI6ImFDQTdFakF1VFcxaDhjWUJTOEJuUHo5bEtYdktxbGJNIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.QJcAHEYp8Rpu1ZUEa-6vsenanT_5YCKPp343JJ6H4GUuMgchgrDfaY9yP7GMAypym9uw1eE_UbgzCQ5vy1o_HMV1rGpfvXmFIr0qYV1-KcqgM_djsplsa3xsuqeJqqhQal1zWts2LaqxvMDnmKDafkcnK3HeypPX4r78eDeQ0j60V2ZGNXEM0uY0jD-YwTixYQ7giMYoy0WfBgf3LQzHIY-eNsDeA1gwqpCxcpidvKplRaPzH24up9o7h87YNuk_hmX-KWmp-HDo0jEyEekRBvR_b4f_sMg0w5P2JId8ZPzfrF2K_inY_00dOg7wRdY_kBWMz0lXOy8MJ2FhTAxUhw"
jwt_ca = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZIWG9XTGFJZk1od0tERjh2TEtTWiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZmluYWxwcm9qZWN0LWJ1cmdlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjU3YjExNGRmZmYwNjAwNjgyZDEyMmMiLCJhdWQiOiJtYW5hZ2VtZW50IiwiaWF0IjoxNTk5Nzc2NDY4LCJleHAiOjE1OTk4NjI4NjgsImF6cCI6ImFDQTdFakF1VFcxaDhjWUJTOEJuUHo5bEtYdktxbGJNIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.QaBiU12OTJP3XyRCDlcKGDJfoQHISOtl84ayhjJjLj3a28FqW-Pv1uUrIWsw2My1PQXaCp53WkNNZX-MepecnzZMy9hxGsm3sp2pcBnsy3koeN7cXhoW_jCnhsIlrZpVhOSaMYoq8AnTku8chMlYOBEcd3O0iLnQKca-ANX-P52FzBOGKQpwFvHXd7jTQfUEU8kONuB8AN4z_qBdVg0IAYAZ5CR8Fm3PJnGTdzqcjlV-oD__UduxlGNlGvUbJxzfnti8syoDEHwW1B2TZ2Mvvzn1c_wlKWmCev6KhwzqGL_RtfZYtQu0D3tcI2g-Z9zYMIjYdHRJYp4J24ebB8F57A"
jwt_no = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZIWG9XTGFJZk1od0tERjh2TEtTWiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZmluYWxwcm9qZWN0LWJ1cmdlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjU5MmIyYWMwZTU5ZTAwNzZmMTJhNGIiLCJhdWQiOiJtYW5hZ2VtZW50IiwiaWF0IjoxNTk5Nzc2NTE2LCJleHAiOjE1OTk4NjI5MTYsImF6cCI6ImFDQTdFakF1VFcxaDhjWUJTOEJuUHo5bEtYdktxbGJNIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6W119.AzenDBjIkkjJFzSdoHqEZFFmp_4q5mm-35tpimBY28rbowYSP7muFLK55jhtDSP05-8uBK9ctbJTkWSkUokatqA3KEqSirPCv3GIu-IDKT0DvQSw5NeEReRURhgu5-r0ghtKZCw41n_2J1q6GhSLAkQYl3P8ejq4mA1Kyrp_M-be5Gno-SXWNZLUFVyfOmoai_WeOic6lqSfOS8ypyKUC_QHtaNrYXpCOuH7F4Hn4vqJiyaheT7Yt5gjs1Wgxy28QyO_-LUVPRLFeuRFx2Wrw-o_6jFoDdqSXHV7Q_f9I1AIE0jxbVjFxQDEFMWmod9Yyp11lGcHh1W49qg1MywGAQ"

# test data
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


# test case class for casting app
class CastingTestCase(unittest.TestCase):
    #
    # set up test environment
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)
        #
        # bind app to current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    # executed after each test
    def tearDown(self):
        pass

    # ----------------------------------------------------------------------
    # POST tests
    # ----------------------------------------------------------------------

    # ACTORS
    #
    # unauthorized: add actor (casting assistant)
    def test_401_add_actor(self):
        test = (self.client().post('/actors', json=actor1,
                headers={"Authorization": "Bearer {}".format(jwt_ca)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 401)

    # authorized: add actor (casting director)
    def test_200_add_actor(self):
        test = (self.client().post('/actors', json=actor1,
                headers={"Authorization": "Bearer {}".format(jwt_cd)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor_id'])

    # authorized: add actor but missing required fields
    def test_412_add_actor_missing_fields(self):
        test = (self.client().post('/actors', json=actor2,
                headers={"Authorization": "Bearer {}".format(jwt_cd)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 412)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],
                         'precondition failed or request data missing')

    # MOVIES
    #
    # unauthorized: add movie (casting director)
    def test_401_add_movie(self):
        test = (self.client().post('/movies', json=movie1,
                headers={"Authorization": "Bearer {}".format(jwt_cd)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 401)

    # authorized: add movie (executive producer)
    def test_200_add_movie(self):
        test = (self.client().post('/movies', json=movie1,
                headers={"Authorization": "Bearer {}".format(jwt_ep)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie_id'])

    # authorized: add movie but missing cast list
    def test_412_add_movie_no_cast(self):
        test = (self.client().post('/movies', json=movie2,
                headers={"Authorization": "Bearer {}".format(jwt_ep)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 412)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],
                         'precondition failed or request data missing')

    # authorized: add movie but missing required fields
    def test_412_add_movie_missing_fields(self):
        test = (self.client().post('/movies', json=movie3,
                headers={"Authorization": "Bearer {}".format(jwt_ep)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 412)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],
                         'precondition failed or request data missing')

    # ----------------------------------------------------------------------
    # PATCH tests
    # ----------------------------------------------------------------------

    # ACTORS
    #
    # unauthorized: update actor (casting assistant)
    def test_401_update_actor(self):
        test = (self.client().patch('/actors/2', json=uactor1,
                headers={"Authorization": "Bearer {}".format(jwt_ca)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 401)

    # authorized: update actor (casting director)
    def test_200_update_actor(self):
        test = (self.client().patch('/actors/2', json=uactor1,
                headers={"Authorization": "Bearer {}".format(jwt_cd)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 200)
        self.assertEqual(data['success'], True)

    # authorized: update actor (casting director), but wrong id
    def test_412_update_actor_unknown_id(self):
        test = (self.client().patch('/actors/-1', json=uactor1,
                headers={"Authorization": "Bearer {}".format(jwt_cd)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 412)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],
                         'precondition failed or request data missing')

    # authorized: update actor (casting director), but no recognized fields
    def test_412_update_actor_no_fields(self):
        test = (self.client().patch('/actors/2', json=uactor2,
                headers={"Authorization": "Bearer {}".format(jwt_cd)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 412)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],
                         'precondition failed or request data missing')

    # MOVIES
    #
    # unauthorized: update movie (casting assistant)
    def test_401_update_movie(self):
        test = (self.client().patch('/movies/2', json=umovie1,
                headers={"Authorization": "Bearer {}".format(jwt_ca)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 401)

    # authorized: update movie (casting director)
    def test_200_update_movie(self):
        test = (self.client().patch('/movies/2', json=umovie1,
                headers={"Authorization": "Bearer {}".format(jwt_cd)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 200)
        self.assertEqual(data['success'], True)

    # authorized: update movie (casting director), but wrong id
    def test_412_update_movie_unknown_id(self):
        test = (self.client().patch('/movies/-1', json=umovie1,
                headers={"Authorization": "Bearer {}".format(jwt_cd)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 412)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],
                         'precondition failed or request data missing')

    # authorized: update movie (casting director), but no regognized fields
    def test_412_update_movie_no_fields(self):
        test = (self.client().patch('/movies/2', json=umovie2,
                headers={"Authorization": "Bearer {}".format(jwt_cd)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 412)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],
                         'precondition failed or request data missing')

    # authorized: update movie (casting director), but empty cast list
    def test_412_update_movie_empty_castlist(self):
        test = (self.client().patch('/movies/2', json=umovie3,
                headers={"Authorization": "Bearer {}".format(jwt_cd)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 412)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],
                         'precondition failed or request data missing')

    # ----------------------------------------------------------------------
    # GET tests
    # ----------------------------------------------------------------------

    # ACTORS
    #
    # unauthorized: get actors (public)
    def test_401_get_actors(self):
        test = (self.client().get('/actors',
                headers={"Authorization": "Bearer {}".format(jwt_no)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 401)

    # authorized: get movies (casting assistant)
    def test_200_get_actors(self):
        test = (self.client().get('/actors',
                headers={"Authorization": "Bearer {}".format(jwt_ca)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    # MOVIES
    #
    # unauthorized: get movies (public)
    def test_401_get_movies(self):
        test = (self.client().get('/movies',
                headers={"Authorization": "Bearer {}".format(jwt_no)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 401)

    # authorized: get movies (casting assistant)
    def test_200_get_movies(self):
        test = (self.client().get('/movies',
                headers={"Authorization": "Bearer {}".format(jwt_ca)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    # ----------------------------------------------------------------------
    # DELETE tests
    # ----------------------------------------------------------------------

    # ACTORS
    #
    # unauthorized: delete actor (casting assistant)
    def test_401_delete_actor(self):
        test = (self.client().delete('/actors/1',
                headers={"Authorization": "Bearer {}".format(jwt_ca)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 401)

    # authorized: delete actor (casting director)
    def test_200_delete_actor(self):
        test = (self.client().delete('/actors/1',
                headers={"Authorization": "Bearer {}".format(jwt_cd)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 200)
        self.assertEqual(data['success'], True)

    # authorized: delete actor but unknown actor_id
    def test_412_delete_actor_unknown_id(self):
        test = (self.client().delete('/actors/-1',
                headers={"Authorization": "Bearer {}".format(jwt_cd)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 412)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],
                         'precondition failed or request data missing')

    # MOVIES
    #
    # unauthorized: delete movie (casting director)
    def test_401_delete_movie(self):
        test = (self.client().delete('/movies/1',
                headers={"Authorization": "Bearer {}".format(jwt_cd)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 401)

    # authorized: delete movie (executive producer)
    def test_200_delete_movie(self):
        test = (self.client().delete('/movies/1',
                headers={"Authorization": "Bearer {}".format(jwt_ep)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 200)
        self.assertEqual(data['success'], True)

    # authorized: delete movie but unknown movie_id
    def test_412_delete_movie_unknown_id(self):
        test = (self.client().delete('/movies/-1',
                headers={"Authorization": "Bearer {}".format(jwt_ep)}))
        data = json.loads(test.data)
        self.assertEqual(test.status_code, 412)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],
                         'precondition failed or request data missing')


#
# Main: run app
if __name__ == "__main__":
    unittest.main()
