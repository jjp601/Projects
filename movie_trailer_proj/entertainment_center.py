import fresh_tomatoes
import media

# Creates each instance from the Class Movie
dark_knight_rises = media.Movie("The Dark Knight Rises",
                        "Batman takes on his toughest adversary yet",
                        "https://images-na.ssl-images-amazon.com/images/I/51k98elC6mL._SY450_.jpg",
                        "https://www.youtube.com/watch?v=GokKUqLcvD8")

inception = media.Movie("Inception",
                     "An expert of dream theory takes it to the next level",
                     "http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-7.jpg",
                     "https://www.youtube.com/watch?v=YoHD9XEInc0")

force_awakens = media.Movie("The Force Awakens",
                     "A young girl learns about the force",
                     "http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2015/10/star-wars-force-awakens-official-poster.jpg",
                     "https://www.youtube.com/watch?v=sGbxmsDFVnE")

ironman = media.Movie("Ironman",
                     "A Wealthy businessman becomes a super hero",
                     "http://www.bluemaize.net/im/baby/iron-man-poster-6.jpg",
                     "https://www.youtube.com/watch?v=8hYlB38asDY")

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                     "A group of misfits save the galaxy",
                     "http://1.media.dorkly.cvcdn.com/26/95/18b149286ca6f2920e017bd5d2ffcbf5.jpg",
                     "https://www.youtube.com/watch?v=d96cjJhvlMA&t=24s")

avengers = media.Movie("The Avengers",
                     "The world's super heroes come together to stop its biggest threat",
                     "https://s-media-cache-ak0.pinimg.com/736x/ee/51/b9/ee51b98cfe29f8f8943f09766398c606--avengers-movie-avengers-poster.jpg",
                     "https://www.youtube.com/watch?v=eOrNdBpGMv8")                                                               

# Adds each instance to the template to be rendered
movies = [dark_knight_rises, inception, force_awakens, ironman, guardians_of_the_galaxy, avengers]
fresh_tomatoes.open_movies_page(movies)
