from flask import Flask, render_template, url_for, request
import tmdb_client

app = Flask(__name__)


@app.route('/')
def homepage():
    movies_lists = ['now_playing', 'popular', 'top_rated', 'upcoming']
    selected_list = request.args.get('list_type', 'popular')
    if selected_list not in movies_lists:
        selected_list = 'popular'
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template(
        "homepage.html",
        movies=movies,
        current_list=selected_list,
        movies_lists=movies_lists,
    )


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    movie = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=movie, cast=cast)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


''' TO W SUMIE NIEPOTRZEBNE, ALE BYŁO DO ZROBIENIA (?)
def get_movie_info():
    movies = []
    for movie in tmdb_client.get_popular_movies().get('results'):
        title = movie.get('title')
        path = movie.get('poster_path')
        movies.append({
            title: path
        })
    return movies
 '''


if __name__ == '__main__':
    app.run(debug=True)