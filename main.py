from flask import Flask, render_template, request
import tmdb_client

app = Flask(__name__)


@app.route('/')
def homepage():
    movies_lists = ['popular', 'now_playing', 'top_rated', 'upcoming']
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


@app.route("/search/")
def search():
    search_query = request.args.get('q')
    if search_query:
        results = tmdb_client.search_movies(search_query)
    else:
        results = ""
    return render_template(
        "search.html",
        search_query=search_query,
        results=results
    )


@app.route("/series/")
def series():
    series = tmdb_client.get_series_airing_today()
    return render_template(
        "series.html",
        series=series
    )


@app.route("/favorite/")
def favorite():
    pass


@app.route("/me/")
def about_me():
    return render_template(
        "me.html",
    )


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


if __name__ == '__main__':
    app.run(debug=True)
