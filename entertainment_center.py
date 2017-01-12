import fresh_tomatoes
import tmdbsimple as tmdb
import media


tmdb.API_KEY = '<Your 32 character API Key here>'
base_poster_url = "http://image.tmdb.org/t/p/w185/"
base_trailer_url = "https://www.youtube.com/watch?v="

# Gets Page 1 of the Now Playing List of movies from TMDb
response = tmdb.Movies().now_playing()
result = response['results']

# Keeping only the first 15 movies received in the list.
result = result[:15]

movies_list = list()

for i in range(15):
    # Required movie attributes
    movie_id = result[i]['id']
    title = result[i]['title']
    storyline = result[i]['overview']
    poster_url = base_poster_url + result[i]['poster_path']
    video_url = base_trailer_url

    # Getting all the videos associated with a movie
    videos = tmdb.Movies(movie_id).videos()
    video_list = videos['results']

    # This loop will scan the results and will pick the video which is marked
    # as "Trailer" because there are other types of video media too like
    # Teasers or Featurettes
    for j in range(len(video_list)):
        if 'Trailer' == video_list[j]['type']:
            video_url = video_url + video_list[j]['key']

            # Create MyMovie objects and add them to the list
            current_movie = media.MyMovie(movie_id, title, storyline,
                                          poster_url, video_url)
            movies_list.append(current_movie)
            break

fresh_tomatoes.open_movies_page(movies_list)
