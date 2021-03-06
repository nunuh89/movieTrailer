import media
import fresh_tomatoes
"""
    script to store movie attributes & call fresh_tomatoes to generate the page

"""

la_la_land = media.Movie(
    "La La Land",
    "Musical drama about pursing dreams",
    "http://alturl.com/zv2j8",
    "https://www.youtube.com/watch?v=0pdqf4P9MB8")

the_lobster = media.Movie(
    "The Lobster",
    "David will be turned into an animal if fails"
    " to find true love within 45 days",
    "http://alturl.com/ob99y",
    "https://www.youtube.com/watch?v=TR_NcqD-Gfs")

hacksaw_ridge = media.Movie(
    "Hacksaw Ridge",
    "American hero soldier in WWII to fight on "
    "the front lines without a weapon",
    "http://alturl.com/sfzhk",
    "https://www.youtube.com/watch?v=s2-1hz1juBI")

arrival = media.Movie(
    "Arrival",
    "When mysterious spacecrafts arrive, linguist"
    " Louise must decode their language to save the world.",
    "http://alturl.com/vycfr",
    "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

zootopia = media.Movie(
    "Zootopia",
    "Judy becomes the first police officer of Zootopia",
    "http://alturl.com/ycq75",
    "https://www.youtube.com/watch?v=jWM0ct-OLsM")

deadpool = media.Movie(
    "Deadpool",
    "Deadpool hunts down the man who nearly destroyed his life",
    "http://alturl.com/if4vn",
    "https://www.youtube.com/watch?v=9vN6DHB6bJc")

movies = [la_la_land, the_lobster, hacksaw_ridge, arrival, zootopia, deadpool]

fresh_tomatoes.open_movies_page(movies)
