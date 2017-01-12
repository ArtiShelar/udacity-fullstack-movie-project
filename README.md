# Fresh Tomatoes

Fresh Tomatoes creates a simple website of movie trailers from data received from the The Movie Database (TMDb). URL of TMDb is [https://www.themoviedb.org/](https://www.themoviedb.org/).

A list of 15 movies has been retrieved from TMDb along with the images / posters and videos associated with it. A python script then creates a static HTML page displaying these movies. Clicking on the movie poster will play the official trailer of the movie.

Currently, data once retrieved it is populated into a static webpage called `fresh_tomatoes.html`. However, rebuilding the python script will retrieve only those movies which are playing in the theatres at that time.

## Local Setup

Fresh Tomatoes uses the [tmdbsimple 1.4.1 API](https://pypi.python.org/pypi/tmdbsimple) for using the metadata stored in TMDb.

> Installation

Use pip to install:

`pip install tmdbsimple`

or download the .zip from PyPI link given above and install it yourself.

> API Key

<img src="https://www.themoviedb.org/assets/static_cache/2dceae11589334eecd61443249261daf/images/v4/logos/208x226-stacked-green.png" width="60">

You will need an API key to The Movie Database to access the API. To obtain a key, follow these steps:
* Register for and verify an [account](https://www.themoviedb.org/account/signup).
* [Log in](https://www.themoviedb.org/login) to your account.
* Select the API section on left side of your account page.
* Click on the link to generate a new API key and follow the instructions.
> If the API key is to be used for educational purposes like this personal mini-project, then specify so while requesting the key.

Once the API key is obtained, add it to the `entertainment_center.py` file. If the API key obtained is `289e548XXXXXXXXXXXXXXXXXXXXXXXXX` then set the `tmdb.API_KEY` value as follows:  

`tmdb.API_KEY = '289e548XXXXXXXXXXXXXXXXXXXXXXXXX'`

Save and run this python file. The static HTML file generated will be called `fresh_tomatoes.html` and it will open automatically in your default browser.
