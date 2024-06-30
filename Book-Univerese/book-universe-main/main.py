#this is Book Universe bookshop inventory system
#this system developed by
#Mohamed Ahmed  #Amr Adel Mansour

#this system Reviewer 
#Ziad Hassan etman 

#this system Documentry
#Mohamed abu gharbiyeh

#how this system works the database is stored in a csv file that must be in the same folder to work
#the main concept is reading the csv file and presenting or modifying the data when needed, according to the user needs
#every option in the menu is sperated and has it is own function, we will provide comments and explanation for each function

import csv

# at the start of the program after importing the csv module we define the main function as known as the root of the application
#we will not call the main function at the moment we will use the dunder method to call it at the end of this file 
# main function is basically an infinte loop that prints the menu and calls functions when needed 
# so using computer termnology we can call it the motherboard of this program connecting every function

def main():
    #inside of the main function the first thing we do is call the intro function, which
    #prints a nice looking intro with the system name and the name of the developers of this system

    intro()

    # in this part of the program this infinite while loop  starts the program logic
    
    while True:
        #inside this loop we print the menu of options also we start accessing the database
        #using the get_database() function
        get_database()
        print_menu()

        option = None

        #in this block of code we check for user input that it matches the input we expect to prevent
        #input errors using the try and except statment to handle any errors
        try:
            option = int(input("Enter your option: "))
        except:
            print("wrong input please use numbers from 1 to 11")

        if option == 1:
            read_data()

        elif option == 2:
            list_data()

        elif option == 3:
            search_by_title()

        elif option == 4:
            search_by_author()

        elif option == 5:
            add_book()

        elif option == 6:
            remove_book()

        elif option == 7:
            add_stock()

        elif option == 8:
            remove_stock()

        elif option == 9:
            Total_value()

        elif option == 10:
            saving()

        elif option == 11:
            exit_system()
        

#this function is called to initialize the database opening the file making it ready to use for other functions
#using the global variable "database" as a file handle 
def get_database():
    global database
    global f
    f = open("main.csv")
    database = csv.DictReader(f)

    
#this function is easy to understand it just prints a fancy welcome screen
#using of course the print function we print the  name line by line
def intro():
    print("==================================================================================")
    print("  ____                 _      _    _         _                              ")
    print(" |  _ \               | |    | |  | |       (_)                             ")
    print(" | |_) |  ___    ___  | | __ | |  | | _ __   _ __   __ ___  _ __  ___   ___ ")
    print(" |  _ <  / _ \  / _ \ | |/ / | |  | || '_ \ | |\ \ / // _ \| '__|/ __| / _ \ ")
    print(" | |_) || (_) || (_) ||   <  | |__| || | | || | \ V /|  __/| |   \__ \|  __/")
    print(" |____/  \___/  \___/ |_|\_\  \____/ |_| |_||_|  \_/  \___||_|   |___/ \___|")
    print("\n                         Bookshop Inventory System")
    print("\n==================================================================================")
    print("\n")
    print("===============================>>>>> Welcome <<<<<================================")
    print("\n\n   Developed by:")
    print("                  • Mohamed Ahmed • Amr Adel")
    print("\n\n   Reviewd by:")
    print("                • Zeyad Hassan etman")
    print("\n\n   Documented by:")
    print("                • Mohammad abu gharbiyeh")
    print("\n\n==================================================================================")


# this function prints the menu using a for loop with an if statment to make the look more clean
# it prints the menu form a dictionary
def print_menu():

    menu_options = {
    1: ' Read Data',
    2: ' List Data',
    3: ' Search by Title',
    4: ' Search by Author',
    5: ' Add a New Book',
    6: ' Delete a Book',
    7: ' Add to the Current Stock of a Book',
    8: ' Remove from the Current Stock of a Book',
    9: ' Show Total Value of the Books',
    10: ' Save Data',
    11: ' Exit'
}

    print("\n\n==================================================================================")
    for key in menu_options.keys():

        if key > 9:
            print (key , ' ->', menu_options[key] )
        else:    
            print (key , '  ->', menu_options[key] )

    print("==================================================================================")



#this function reads the database using the database file handle and the csv.dictreader methods

def read_data():
    books = 0
    all_books = 0
    print("reading data...")
    
    for row in database:
        books = books + 1
        all_books = all_books + int(row["Quantity"])

    print(f"succeeded, the system found {books} unique books, the total quantity of books is {all_books} books")


#this function prints the database in a nice formate using .formate method on the rows returned
#using a for loop and the the csv.dictreader

def list_data():
    print("==================================================================================================================")
    print("{:<10} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format('Book_ID','Title','Author','Category','Quantity','Unit_price','Total_price'))
    print("==================================================================================================================")
    #listing the data using a for loop and the .format() method
    for row in database:
        print("{:<10} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(row['Book_id'],row['Title'],row['Author'],row['Category'],row['Quantity'],row['Unit_price'],row['Total_price']))




#this function gets input from the user and compares it to the database:Title column  using a for loop and the find method
def search_by_title():
    title = input("Search by title: ")
    
    n = 0

    print("==================================================================================================================")
    print("{:<10} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format('Book_ID','Title','Author','Category','Quantity','Unit_price','Total_price'))
    print("==================================================================================================================")
    # here we are searching the database using a for loop and returning the resualts
    for row in database:
        
        index = row["Title"].find(title)
        
        if index > -1:
            print("{:<10} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(row['Book_id'],row['Title'],row['Author'],row['Category'],row['Quantity'],row['Unit_price'],row['Total_price']))
            n = n+1
    if n == 0:
        print("\n\n=============Matching title not found=============")


#this function gets input from the user and compares it to the database:author column  using a for loop and the find method
def search_by_author():
    author = input("Search by author: ")
    
    n = 0

    print("==================================================================================================================")
    print("{:<10} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format('Book_ID','Title','Author','Category','Quantity','Unit_price','Total_price'))
    print("==================================================================================================================")
    # here we are searching the database using a for loop and returning the resualts
    for row in database:
        
        index = row["Author"].find(author)
        
        if index > -1:
            print("{:<10} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(row['Book_id'],row['Title'],row['Author'],row['Category'],row['Quantity'],row['Unit_price'],row['Total_price']))
            n = n+1
    if n == 0:
        print("\n\n=============MatchSalamaing author not found=============")



#adding a book this function gets user input and stores it temporarily in variables then writes them to the database
# using csv.dictwriter to write to the database
def add_book():
    #here inside this loop we are checking the user input to make sure the id is correct
    #using the try and except statments to catch errors and handle them
    while True:
        try:

            Book_id = int(input("Enter book id: "))
            break
        except:
            print(" wrong input book id should be only numbers ")
        
    Title = input("Enter book Title :")
    Author = input("Enter book Author :")
    Category = input("Enter book Category :")

    #here inside this loop we are checking the user input to make sure the quantity is correct
    #using the try and except statments to catch errors and handle them

    while True:
        try:
            Quantity = int(input("Enter book Quantity : "))
            break
        except:
            print(" wrong input quantity should be only numbers ")

    #here inside this loop we are checking the user input to make sure the unit_price is correct
    #using the try and except statments to catch errors and handle them
    while True:
        try:
            Unit_price = float(input("Enter book unit price : "))
            break
        except:
            print(" wrong input unit price should be only numbers ")

    total = float(Quantity) * Unit_price
    
    #writing the data to the database using the csv.dictwriter
    with open("main.csv", "a") as f:
        writer = csv.DictWriter(f, fieldnames=["Book_id","Title","Author","Category","Quantity","Unit_price","Total_price"])
        writer.writerow({"Book_id":Book_id ,"Title":Title ,"Author": Author ,"Category": Category,"Quantity": Quantity,"Unit_price": Unit_price,"Total_price": total})

    print("==================================================================================")
    print("book added successfully")
    print("==================================================================================")



#this function removes a book from the database by reading the database and rewrites it without the book you want to remove

def remove_book():

    id = int(input("enter ID to delete:"))
    lines = []
# here we are using the with  statment to handle reading the file and closing it when we are no longer need the file
    with open("main.csv", "r") as l:
        lines = l.readlines()

# here we are using the with  statment to handle reading the file and closing it when we are no longer need the file
    with open("main.csv", "w") as w:
        for line in lines:
            index = line.find(str(id))
            if index == -1:
                w.write(line)

    print("==================================================================================")
    print("book deleted successfully")
    print("==================================================================================")
        
    
#adding stock is  more complicated we first get the id of the book and the number of the stocks to add then we reads the database
#after reading the databse we store it in list then we  modify the items inside of the list then rewrite it to the database with the changes
# we also need to update the total value and make sure  to convert the  strings to intgers and vice versa when needed for calcuations

def add_stock():
    book_id = input("Enter ID to add stock:")
    stock_to_add = int(input("Enter number of books to add:"))

    lines = []

    # Using the with statement to handle reading the file and closing it when not needed
    with open("main.csv", "r") as file:
        lines = file.readlines()

    line_to_add_to = None

    for line in lines:
        if book_id in line:
            line_to_add_to = line
            break

    if line_to_add_to is not None:
        i = lines.index(line_to_add_to)

        # Splitting the line into a list
        line_to_add_to = line_to_add_to.split(",")

        # Modifying the list items and calculating the new total value
        line_to_add_to[4] = str(int(line_to_add_to[4]) + stock_to_add)
        line_to_add_to[6] = str(int(line_to_add_to[5]) * int(line_to_add_to[4]))

        # Adding the modified row back to the list to apply to the database
        lines[i] = ",".join(line_to_add_to) + "\n"

        # Writing to the database line by line after the changes
        with open("main.csv", "w") as file:
            for line in lines:
                file.write(line)
    else:
        print("Book ID not found.")

    print("==================================================================================")
    print("stock added successfully")
    print("==================================================================================")



#removing stock is  more complicated we first get the id of the book and the number of the stocks to remove then we reads the database
#after reading the databse we store it in list then we  modify the items inside of the list then rewrite it to the database with the changes
# we also need to update the total value and make sure  to convert the  strings to intgers and vice versa when needed for calcuations


def remove_stock():

    id = input("enter ID to remove stock:")

    stock = int(input("enter number of books to remove:"))
    

    lines = []
# here we are using the with  statment to handle reading the file and closing it when we are no longer need the file
    with open("main.csv", "r") as l:
        lines = l.readlines()
    
    line_to_add_too = None

    for line in lines:
        index = line.find(id)
        if index == 0:
            line_to_add_too = line

    i = lines.index(line_to_add_too)

    line_to_add_too = list(line_to_add_too.split(","))

#checking if the stock to remove is more than the current inventory and raising an exception
    if int(line_to_add_too[4]) < stock:
        raise Exception("stock cant be  negative")

#modifying the list items and removing the stock and calculating the  new total value

    line_to_add_too[4] = int(line_to_add_too[4]) - stock

    line_to_add_too[6] = int(line_to_add_too[5]) * line_to_add_too[4]

    book_total = line_to_add_too[6]

    Current_stock = line_to_add_too[4]

    line_to_add_too[4] = str(line_to_add_too[4])


    line_to_add_too[5] = str(line_to_add_too[5])

    line_to_add_too[6] = str(line_to_add_too[6])
    #   here we are adding the modified row back to the list to apply to the database

    c = ","
    n = "\n"
    line_to_add_too = c.join(line_to_add_too)
    line_to_add_too = line_to_add_too + n
    lines[i] = line_to_add_too
    #writing to the data base line by line after the changes
# here we are using the with  statment to handle reading the file and closing it when we are no longer need the file
    with open("main.csv", "w") as w:
        for line in lines:
            w.write(line)
    
    print("==================================================================================")
    print("stock removed successfully")
    print(f"the current stock of this book is {Current_stock} value of it is {book_total}")
    print("==================================================================================")

#Calucating the value but adding all the total values togther using a for loop
def Total_value():
    total = 0
    for row in database:
        total += float((row['Total_price']))
    print("==================================================================================")
    print(f"total value of books in the database is {total}")
    print("==================================================================================")



# closing the database and reopening it again causeing a quick save
def saving():
    print("==================================================================================")
    f.close()
    print("database saved successfully")
    get_database()
    print("==================================================================================")

# this funcion closes the program using the exit function
def exit_system():
    print("\n\n==================================================================================")

    print("thanks for using Book Universe, goodbye")

    print("==================================================================================")
    exit()

#this is the dunder method we mentioned in the first lines of the code it  uses an if statment 
# to call the main function starting the program 
#we can call the main function using other ways but this is recommended and is one of 
# the best practicese while coding
if __name__ == "__main__":
    main()
