import os
from flask import Flask, jsonify, abort, request
from models import setup_db, Movie, Actor
from flask_cors import CORS

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello" 
        if excited == 'true': 
            greeting = greeting + "!!!!! You are doing great in this Udacity project."
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"
    
    # First of all, Endpoint "g"et actors" shall be implemented
    @app.route('/actors')
    def get_actors():

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
    def get_movies():

        movies = Movie.query.order_by(Movie.id).all()

        if len(movies) == 0:
            abort(422)

        movies_formatted = [movie.format() for movie in movies]

        return jsonify(
            {
                "success": True,
                "actors": movies_formatted
            })
    
    # Implement the endpoint for deletion of actors
    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    def delete_actor(actor_id):
        
        try:
            actor = Actor.query\
                .filter(Actor.id == actor_id)\
                .one_or_none()
            
            if actor is None:
                abort(404)

            actor.delete()

            return jsonify(
                {
                    "success": True,
                    "deleted": actor_id
                }
            )

        except:
            abort(422)


    # Implement the endpoint for deletion of movies
    @app.route("/movies/<int:movie_id>", methods=["DELETE"])
    def delete_movie(movie_id):

        try:
            movie = Movie.query\
                .filter(Movie.id == movie_id)\
                .one_or_none()
            
            if movie is None:
                abort(404)
            
            movie.delete()

            return jsonify(
                {
                    "success": True,
                    "deleted": movie_id
                }
            )

        except:
            abort(422)

        return 'No deletion of movies implemented, yet!'
    
    # Implement the endpoint for movie posting
    @app.route("/movies", methods=["POST"])
    def post_movie():

        body = request.get_json()

        try:
            new_title = body.get('title', None)
            new_release_date = body.get('release_date', None)

            if new_title is None and new_release_date is None:
                abort(22)

            movie = Movie(title=new_title,
                          release_date=new_release_date)
            
            movie.insert()

            return  jsonify(
                {
                    "success": True
                }
            )

        except:
            abort(22)

        return 'no posting implemented!'

    # Implement the endpoint for actor posting
    @app.route("/actors", methods=["POST"])
    def post_actor():

        body = request.get_json()

        try:
            new_name = body.get('name', None)
            new_age = body.get('age', None)
            new_gender = body.get('gender', None)

            if new_name is None or \
                new_age is None or \
                new_gender is None:
                abort(422)

            actor = Actor(name=new_name,
                          age=new_age,
                          gender=new_gender)

            actor.insert()

            return jsonify(
                {
                    "success": True
                }
            )

        except:
            abort(422)


        return 'no posting implemented!'
    
    # Implement the endpoint for the actor patching
    @app.route('/actors/<int:actor_id>',methods = ["PATCH"])
    def patch_actor(actor_id):

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
            
            actor.update()

            actor_formatted = actor.format()

            return jsonify(
                    {
                        "success": True,
                        "actor": actor_formatted
                    }
                )

        except:
            abort(400)
    
    @app.route('/movies/<movie_id>', methods=["PATCH"])
    def patch_movie(movie_id):

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

            movie.update()

            movie_formatted = movie.format()

            return jsonify(
                {
                    "success": True,
                    "movie": movie_formatted
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


    return app


app = create_app()

if __name__ == '__main__':
    app.run()
