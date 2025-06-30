import os
from flask import Flask, jsonify, abort, request
from models import setup_db, Movie, Actor
from flask_cors import CORS
from auth.auth import requires_auth
import markdown

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():

        file_object = open('README.md')
        data = file_object.read()
        file_object.close()

        data_html = markdown.markdown(data)

        return data_html        

    # @app.route('/coolkids')
    # def be_cool():
    #     return "Be cool, man, be coooool! You're almost a FSND grad!"
    
    # First of all, Endpoint "get actors" shall be implemented
    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(jws):

        actors = Actor.query.order_by(Actor.id).all()

        if len(actors) == 0:
            abort(422)

        actors_formatted = [actor.format() for actor in actors]

        return jsonify(
            {
                "success": True,
                "actors": actors_formatted
            })
    
    # Implement the endpoint for getting all movies
    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(jws):

        movies = Movie.query.order_by(Movie.id).all()

        if len(movies) == 0:
            abort(422)

        movies_formatted = [movie.format() for movie in movies]

        return jsonify(
            {
                "success": True,
                "movies": movies_formatted
            })
    
    # Implement the endpoint for deletion of actors
    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    @requires_auth('delete:actors')
    def delete_actor(jws, actor_id):
        
        try:
            actor = Actor.query\
                .filter(Actor.id == actor_id)\
                .one_or_none()
            
            if actor is None:
                abort(404)

            actor_format = actor.format()

            actor.delete()

            return jsonify(
                {
                    "success": True,
                    "deleted": actor_format
                }
            )

        except:
            abort(422)


    # Implement the endpoint for deletion of movies
    @app.route("/movies/<int:movie_id>", methods=["DELETE"])
    @requires_auth('delete:movies')
    def delete_movie(jws, movie_id):

        try:
            movie = Movie.query\
                .filter(Movie.id == movie_id)\
                .one_or_none()
            
            if movie is None:
                abort(404)
            
            movie_format = movie.format()

            movie.delete()

            return jsonify(
                {
                    "success": True,
                    "deleted": movie_format
                }
            )

        except:
            abort(422)

        return 'No deletion of movies implemented, yet!'
    
    # Implement the endpoint for movie posting
    @app.route("/movies", methods=["POST"])
    @requires_auth('post:movies')
    def post_movie(jws):

        body = request.get_json()

        try:
            new_title = body.get('title', None)
            new_release_date = body.get('release_date', None)
            actor_ids = body.get('cast', None)

            if new_title is None or new_release_date is None:
                abort(422)

            movie = Movie(title=new_title,
                          release_date=new_release_date)

            if actor_ids is not None:
                add_actors_to_cast(actor_ids=actor_ids, movie=movie)

            movie.insert()

            movies = Movie.query.order_by(Movie.id).all()

            movies_formatted = [movie.format() for movie in movies]

            return  jsonify(
                {
                    "movies": movies_formatted,
                    "success": True
                }
            )

        except:
            abort(422)

        return

    # Implement the endpoint for actor posting
    @app.route("/actors", methods=["POST"])
    @requires_auth('post:actors')
    def post_actor(jws):

        body = request.get_json()

        try:
            new_name = body.get('name', None)
            new_age = body.get('age', None)
            new_gender = body.get('gender', None)
            movie_ids = body.get('movies', None)

            if new_name is None or \
                new_age is None or \
                new_gender is None:
                abort(422)

            actor = Actor(name=new_name,
                          age=new_age,
                          gender=new_gender)
            
            if movie_ids is not None:
                add_movies_of_actor(movie_ids=movie_ids, actor=actor)

            actor.insert()

            actors = Actor.query.order_by(Actor.id).all()

            actors_formatted = [actor.format() for actor in actors]

            return jsonify(
                {
                    "actors": actors_formatted,
                    "success": True
                }
            )

        except:
            abort(422)


        return 'no posting implemented!'
    
    # Implement the endpoint for the actor patching
    @app.route('/actors/<int:actor_id>',methods = ["PATCH"])
    @requires_auth('patch:actors')
    def patch_actor(jws, actor_id):

        body = request.get_json()

        try:
            actor = Actor.query\
                .filter(Actor.id == actor_id)\
                .one_or_none()
            
            if actor is None:
                abort(404)
            
            if 'name' in body:
                actor.name = body["name"]
            if "age" in body:
                actor.age = body["age"]
            if "gender" in body:
                actor.gender = body["gender"]
            if "movies" in body:
                # erase everything in the first place
                actor.movies = []
                actor.update()

                # then append all newly configured references
                movie_ids = body["movies"]
                add_movies_of_actor(movie_ids=movie_ids, actor=actor)
            
            actor.update()

            actors = Actor.query.order_by(Actor.id).all()

            actors_formatted = [actor.format() for actor in actors]

            return jsonify(
                {
                    "actors": actors_formatted,
                    "success": True
                }
            )

        except:
            abort(400)
    
    @app.route('/movies/<movie_id>', methods=["PATCH"])
    @requires_auth('patch:movies')
    def patch_movie(jws, movie_id):

        body = request.get_json()

        try:
            
            movie = Movie.query\
                .filter(Movie.id == movie_id)\
                .one_or_none()
            
            if movie is None:
                abort(404)
            
            if "title" in body:
                movie.title = body["title"]

            if "release_date" in body:    
                movie.release_date = body["release_date"]

            if "actors" in body:
                # erase everything in the first place
                movie.actors = []
                movie.update()

                 # then append all newly configured references
                actor_ids = body["actors"]
                add_actors_to_cast(actor_ids=actor_ids, movie=movie)

            movie.update()

            movies = Movie.query.order_by(Actor.id).all()

            if len(movies) == 0:
                abort(422)

            movies_formatted = [movie.format for movie in movies]

            return jsonify(
                {
                    "success": True,
                    "movies": movies_formatted
                }
            )

        except:
            abort(400)

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, 
                        "message": "bad request"}), 400

    @app.errorhandler(401)
    def authorizationMissing(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Authorization Header not present"
        }), 401
    
    @app.errorhandler(403)
    def permissionNotFound(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "Permission not found."
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return(
            jsonify({"success": False, "error": 404, 
                     "message": "Resource either empty or not found"}),
            404
        )
    
    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success":False, "error": 422, 
                     "message":"Unprocessable Request"}),
            422,
        )


    # define function for adding actors to the cast
    # by providing the actor names 
    def add_actors_to_cast(actor_ids, movie):
        for actor_id in actor_ids:
            actor = Actor.query.\
                filter(Actor.id == actor_id).\
                one_or_none()
            if actor is not None\
                and actor not in movie.actors:
                movie.actors.append(actor)  


    # define function for adding mvoies to the actor
    # by providing the title 
    def add_movies_of_actor(movie_ids, actor):
        print(movie_ids)
        for movie_id in movie_ids:
            movie = Movie.query.\
                filter(Movie.id == movie_id).\
                one_or_none()
            if movie is not None\
                and movie not in actor.movies:
                    actor.movies.append(movie)  

    @app.route('/headers')
    @requires_auth
    def headers(payload):
        print(payload)

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
