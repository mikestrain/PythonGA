#Mike Strain, 2019-12-05 Python Class #2
movie_title = "Back to the Future"
movie_ratings = 8
search_or_ratings = 3

#not used, but still kept
def printMovieTitle():
    print(movie_title)

#used for option 1
def listSearchResults(movieTitles):
    for movie in movieTitles:
        print("\t",movie)

# used for option 2
def printMovieRating():
    print(movie_ratings)

#used in "else" statement
def printSingleMovieRating():
    print(r"The rating for " + movie_title + " is " + str(movie_ratings))

#used by default in the main function
def printAllRatings(movieList):
    for movie in movieList:
        print("The movie", movie, "has a great rating!")

def main():
    default_movie_list = ["Back to the Future", "Blade", "Spirited Away"]
    printAllRatings(default_movie_list)
    if search_or_ratings == 1:
        listSearchResults(default_movie_list)
    elif search_or_ratings == 2:
        printMovieRating()
    else:
        printSingleMovieRating()

if __name__ == "__main__":
    main()