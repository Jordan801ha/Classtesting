#Jordan Harriyou
#sec 004
# Description: A Python program that manages a movie collection

#   using a list of dictionaries. Users can add, find, delete,

#   and display movies through a menu-driven interface.


#list to store movies 
movies = []

#Definition Category Based on rating

def collect_category_rating(rating) :
    if 9 <= rating <=10:
        return "ChiliPepper"
    elif 7 <= rating <= 8 : 
        return "Green Chili"
    elif 6 <= rating <=5 :
        return "Green Pepper"
    elif 5 <= rating <=4 :
        return "Dirt"


  #3. Validate the rating: The input must be an integer between 0 and 10 (inclusive). If the user enters a number outside the 0–10 range, print the following message and prompt again:  
def get_valid_rating() :
    while True:
        try:
            rating = int(input("Enter Your Rating 0-10, 10 Being The Highest: "))
            if 0 <= rating <= 10:
                return rating
            else:
                print("Invalid rating. Please enter a whole number between 0 and 10.")

        except ValueError:  
            print("Invalid rating. Please ender a whole number between 0 and 10")

                #come back

def print_menu () :
    #Display Main Menue"""
    print("Movie Collection Menue") #maybe missing
    print("Add Movie")
    print("Find Movie")
    print("Delete Movie")
    print("Display al Movies ")
    print("Exit") #maybe missing 

def find_movie(title) : 
        #find Movie by entering the title
    title =title.lower ()
    for i, movie in enumerate(movies) : 
            if movies ["title"] .lower() == title :
                return i
    return -1

def add_movie(): 
    #adds a movie to the collection
    title =input("Enter the movie title: ")
    rating = get_valid_rating()
    category = collect_category_rating

    movies.append ({
            "title": title, 
            "rating": rating,
            "category": category
    })

print(f"{'title'} Has been added to your collection!")

def find_movie(): 
    #find/ search for movie\
    title = input("Enter the movie title to search for: ")
    index = find_movie (title)

    if index != -1:
        movie = movie [index]
        print(" Movie not found)")
        print(f"Title: {movie['title']}")
        print(f"rating: {movie['rating']}/10")
        print(f"Category: {movie['category']}")
    else:
        print(f"{title} was not found in your collection.")

        
def delete_movie():
    #this funciton will delet the movie from the collection
    title = input("enter the movie title to delete: ")
    index = find_movie (title)      

    if index != -1: 
        confirm = input(f"are you sure you want to delete {title} yes/no") 
        if confirm.lower() == "yes" :
            removed_title = movies[index]["title"]
        movies.pop(index)
        print(f"{removed_title} has been deleted from your collection.")

    else:
        print(f"{title} was not found in your collection.")


def display_movies():
    #Displays all movies 
    if not movies:
        print ("Your movie colletion is empty.")
    else:
        print("Your Movie Colleciton")
        for movie in movies:
            print(f"Title: {movie['title']}"); Rating: {movie['rating']};  Category: {movie['category']}; ")
            print()

def main() :
    #this will be the main loop
    while True:
        print_menu()#check spelling
        choice = input("Enter your choice: ")

        if choice == "1" :
            add_movie()
        elif choice =="2" :
            find_movie()
        elif choice == "3" :
            delete_movie() 
        elif choice == "4" :
            display_movies
        elif choice == "5" :
            print("Thanks for using the Movie Collection Manager. Goodbye!")
            break
        else: 
            print("Invalid Choice. Please enter a number between 1 and 5.")

if __name__ == "__main__" :
    main()