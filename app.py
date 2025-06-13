import os
from flask import Flask
from models import setup_db
from flask_cors import CORS

def create_app(test_config=None):

    app = Flask(__name__)
    print('__name__ = ' + __name__)
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
        return_statement = 'The endpoint for getting actors is not yet implemented'
        return return_statement
    
    # Implement the endpoint for getting all movies
    @app.route('/movies')
    def get_movies():
        return 'No movies implemented yet.'
    
    # Implement the endpoint for deletion of actors
    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    def delete_actor(actor_id):
        return 'No deletion of actors implemented, yet!'

    # Implement the endpoint for deletion of movies
    @app.route("/movies/<int:movie_id>", methods=["DELETE"])
    def delete_movie(actor_id):
        return 'No deletion of movies implemented, yet!'
    
    # Implement the endpoint for movie posting
    @app.route("/movies", methods=["POST"])
    def post_movie():
        return 'no posting implemented!'

    # Implement the endpoint for actor posting
    @app.route("/actor", methods=["POST"])
    def post_actor():
        return 'no posting implemented!'
    
    # Implement the endpoint for the actor patching
    @app.route('/actors/<int:actor_id>',methods = ["PATCH"])
    def patch_actor(actor_id):
        return 'No Patching implmented'
    
    @app.route('/movies/<movie_id>', methods=["PATCH"])
    def patch_movie(movie_id):
        return 'No Patching of movies implmented'


app = create_app()

if __name__ == '__main__':
    app.run()
