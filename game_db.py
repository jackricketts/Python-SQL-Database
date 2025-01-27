import sqlite3


def sample_data(): # Loads sample data into database
    cursor.execute("CREATE TABLE IF NOT EXISTS games(gID INTEGER PRIMARY KEY NOT NULL, game_name TEXT, player_count INTEGER, size TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS consoles(cID INTEGER PRIMARY KEY NOT NULL, console_name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS players(pID INTEGER PRIMARY KEY NOT NULL, player_name TEXT, fname TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS player_library(pID INTEGER NOT NULL REFERENCES players(pID), gID INTEGER NOT NULL REFERENCES games(gID), PRIMARY KEY (pID, gID))")
    cursor.execute("CREATE TABLE IF NOT EXISTS game_platforms(cID INTEGER NOT NULL REFERENCES consoles(cID), gID INTEGER NOT NULL REFERENCES games(gID), PRIMARY KEY (cID, gID))")
    cursor.execute("INSERT OR IGNORE INTO players (player_name, fname) VALUES ('j.r.blue', 'Jack')")
    cursor.execute("INSERT OR IGNORE INTO players (player_name, fname) VALUES ('cool_player', 'Ben')")
    cursor.execute("INSERT OR IGNORE INTO players (player_name, fname) VALUES ('glass_X', 'George')")
    cursor.execute("INSERT OR IGNORE INTO players (player_name, fname) VALUES ('pythont', 'Patrick')")
    cursor.execute("INSERT OR IGNORE INTO players (player_name, fname) VALUES ('norths', 'Nathan')")
    cursor.execute("INSERT OR IGNORE INTO consoles (console_name) VALUES ('XBOX')")
    cursor.execute("INSERT OR IGNORE INTO consoles (console_name) VALUES ('PS5')")
    cursor.execute("INSERT OR IGNORE INTO consoles (console_name) VALUES ('Nintendo Switch')")
    cursor.execute("INSERT OR IGNORE INTO consoles (console_name) VALUES ('PC')")
    cursor.execute("INSERT OR IGNORE INTO consoles (console_name) VALUES ('Mobile')")
    cursor.execute("INSERT OR IGNORE INTO games (game_name, player_count, size) VALUES ('Minecraft', '188.8 Million', '~1 GB')")
    cursor.execute("INSERT OR IGNORE INTO games (game_name, player_count, size) VALUES ('Candy Crush', '273 Million', '387.1 MB')")
    cursor.execute("INSERT OR IGNORE INTO games (game_name, player_count, size) VALUES ('Mario Kart 8 Deluxe', 'Not Public Information', '~7 GB')")
    cursor.execute("INSERT OR IGNORE INTO games (game_name, player_count, size) VALUES ('Marvel''s Spiderman Remastered', '2.1 Thousand', '75 GB')")
    cursor.execute("INSERT OR IGNORE INTO games (game_name, player_count, size) VALUES ('Chess.com', '20 Million', 'No Download Required')")
    cursor.execute("INSERT OR IGNORE INTO player_library(pID, gID) VALUES (1, 1)")
    cursor.execute("INSERT OR IGNORE INTO player_library(pID, gID) VALUES (1, 3)")
    cursor.execute("INSERT OR IGNORE INTO player_library(pID, gID) VALUES (1, 5)")
    cursor.execute("INSERT OR IGNORE INTO player_library(pID, gID) VALUES (2, 4)")
    cursor.execute("INSERT OR IGNORE INTO player_library(pID, gID) VALUES (3, 2)")
    cursor.execute("INSERT OR IGNORE INTO player_library(pID, gID) VALUES (3, 3)")
    cursor.execute("INSERT OR IGNORE INTO player_library(pID, gID) VALUES (4, 1)")
    cursor.execute("INSERT OR IGNORE INTO player_library(pID, gID) VALUES (4, 4)")
    cursor.execute("INSERT OR IGNORE INTO player_library(pID, gID) VALUES (4, 5)")
    cursor.execute("INSERT OR IGNORE INTO player_library(pID, gID) VALUES (5, 1)")
    cursor.execute("INSERT OR IGNORE INTO game_platforms(cID, gID) VALUES (1, 1)")    
    cursor.execute("INSERT OR IGNORE INTO game_platforms(cID, gID) VALUES (2, 1)")    
    cursor.execute("INSERT OR IGNORE INTO game_platforms(cID, gID) VALUES (2, 4)")    
    cursor.execute("INSERT OR IGNORE INTO game_platforms(cID, gID) VALUES (3, 1)")    
    cursor.execute("INSERT OR IGNORE INTO game_platforms(cID, gID) VALUES (3, 3)")  
    cursor.execute("INSERT OR IGNORE INTO game_platforms(cID, gID) VALUES (4, 1)") 
    cursor.execute("INSERT OR IGNORE INTO game_platforms(cID, gID) VALUES (4, 4)") 
    cursor.execute("INSERT OR IGNORE INTO game_platforms(cID, gID) VALUES (4, 5)") 
    cursor.execute("INSERT OR IGNORE INTO game_platforms(cID, gID) VALUES (5, 1)") 
    cursor.execute("INSERT OR IGNORE INTO game_platforms(cID, gID) VALUES (5, 2)")   
    cursor.execute("INSERT OR IGNORE INTO game_platforms(cID, gID) VALUES (5, 5)") 



    connection.commit()

def give_options(): # Shows base menu
    global current_state
    global flag
    match current_state:
        case 1:
            print("""Database Menu:
1. Load Sample Data
2. Player Functions
3. Console Functions
4. Game Functions
5. Add Game to Player
6. Add Game to Console
7. View Games Owned by Player
8. View Games Available On Console
9. Reset the tables
10. Stop the program""")
            try: # User input
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input! Please enter a new choice")
                return
            if choice == 1:
                sample_data()
            elif choice == 2:
                current_state = 2
            elif choice == 3:
                current_state = 3
            elif choice == 4:
                current_state = 4
            elif choice == 5:
                add_to_player()
            elif choice == 6:
                add_to_console()
            elif choice == 7:
                get_game_by_player()
            elif choice == 8:
                get_game_by_console()
            elif choice == 9:
                reset_tables()
            elif choice == 10:
                flag = True
        case 2:
            print("""Player Menu:
1. View Player List
2. Add Player
3. Search Given Player ID
4. Return to Database Menu""")
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input! Please enter a new choice")
                return
            return_to_menu = player_menu(choice)
            if return_to_menu: current_state = 1
        case 3:
            print("""Console Menu:
1. View Console List
2. Add Console
3. Search Given Console ID
4. Return to Database Menu""")
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input! Please enter a new choice")
                return
            return_to_menu = console_menu(choice)
            if return_to_menu: current_state = 1
        case 4:
            print("""Game Menu:
1. View Game List
2. Add Game
3. Search Given Game ID
4. Return to Database Menu""")
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input! Please enter a new choice")
                return
            return_to_menu = game_menu(choice)
            if return_to_menu: current_state = 1
        case _:
            print("Invalid option, enter a valid value")
        
                
def player_menu(choice): # Menu for player actions
    if choice == 1: # View players
        cursor.execute("SELECT * FROM players;")
        fetched = cursor.fetchall()
        print("{:<9} | {:<15} | {:<15}".format("Player ID", "Player Username", "Player First Name"))
        print("-" * 50)
        for player in fetched:
            print("{:<9} | {:<15} | {:<15}".format(player[0], player[1], player[2]))
    elif choice == 2: # Add player
        while True:
            try:
                username = str(input("Enter the Player's Username: "))
                break
            except:
                print("Invalid input! Please enter a new choice")
                return
        while True:
            try:
                fname = str(input("Enter the Player's First Name: "))
                break
            except:
                print("Invalid input! Please enter a new choice")
                return
        cursor.execute("INSERT OR IGNORE INTO players (player_name, fname) VALUES (?, ?)", (username, fname))
        connection.commit()
    elif choice == 3: # Search for player given ID
        while True:
            try:
                player_id = int(input("Enter Player ID to Look For: "))
                break
            except:
                print("Invalid input! Please enter a new choice")
                return
        cursor.execute("SELECT * FROM players WHERE pID = ?;", (player_id,))
        fetched = cursor.fetchall()
        print("{:<9} | {:<15} | {:<15}".format("Player ID", "Player Username", "Player First Name"))
        print("-" * 50)
        for player in fetched:
            print("{:<9} | {:<15} | {:<15}".format(player[0], player[1], player[2]))
    elif choice == 4: # Back to main menu
        return True

def console_menu(choice): # Consoles menu
    if choice == 1: # View console table
        cursor.execute("SELECT * FROM consoles;")
        fetched = cursor.fetchall()
        print("{:<10} | {:<15}".format("Console ID", "Console Name"))
        print("-" * 50)
        for console in fetched:
            print("{:<10} | {:<15}".format(console[0], console[1]))
    elif choice == 2: # Add a console
        while True:
            try:
                console_name = str(input("Enter the Console's Name: "))
                break
            except:
                print("Invalid input! Please enter a new choice")
                return
        cursor.execute("INSERT OR IGNORE INTO consoles (console_name) VALUES (?)", (console_name,))
        connection.commit()
    elif choice == 3: # View console given ID
        while True:
            try:
                console_id = int(input("Enter Console ID to Look For: "))
                break
            except:
                print("Invalid input! Please enter a new choice")
                return
        cursor.execute("SELECT * FROM consoles WHERE cID = ?;", (console_id,))
        fetched = cursor.fetchall()
        print("{:<9} | {:<15}".format("Console ID", "Console Name"))
        print("-" * 50)
        for console in fetched:
            print("{:<9} | {:<15}".format(console[0], console[1]))
    elif choice == 4: # Return to main menu
        return True

def game_menu(choice): # Game menu
    if choice == 1: # View games table
        cursor.execute("SELECT * FROM games;")
        fetched = cursor.fetchall()
        print("{:<9} | {:<30} | {:<30} | {:<9}".format("Game ID", "Game Name", "Player Count", "Size"))
        print("-" * 100)
        for game in fetched:
            print("{:<9} | {:<30} | {:<30} | {:<9}".format(game[0], game[1], game[2], game[3]))
    elif choice == 2: # Add a game
        while True:
            try:
                game_name = str(input("Enter the Game's Name: "))
                break
            except:
                print("Invalid input! Please enter a new choice")
                return
        while True:
            try:
                p_count = str(input("Enter the Game's Player Count: "))
                break
            except:
                print("Invalid input! Please enter a new choice")
                return
        while True:
            try:
                g_size = str(input("Enter the Game's Size Count: "))
                break
            except:
                print("Invalid input! Please enter a new choice")
                return
        cursor.execute("INSERT OR IGNORE INTO games (game_name, player_count, size) VALUES (?, ?, ?)", (game_name, p_count, g_size))
        connection.commit()
    elif choice == 3: # Search game given ID
        while True:
            try:
                game_id = int(input("Enter Game ID to Look For: "))
                break
            except:
                print("Invalid input! Please enter a new choice")
                return
        cursor.execute("SELECT * FROM games WHERE pID = ?;", (game_id,))
        fetched = cursor.fetchall()
        print("{:<9} | {:<15} | {:<15} | {:<9}".format("Game ID", "Game Name", "Player Count", "Size"))
        print("-" * 50)
        for game in fetched:
            print("{:<9} | {:<15} | {:<15} | {:<9}".format(game[0], game[1], game[2], game[3]))
    elif choice == 4: # Return to main menu
        return True

def add_to_player(): # Add a game to a player
    cursor.execute("SELECT COUNT(gID) FROM games;")
    num_games = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(pID) FROM players;")
    num_players = cursor.fetchone()[0]
    while True:
        try:
            player_id = int(input("Enter Player ID to add a game to: "))
            while player_id > num_players or player_id <= 0:
                player_id = int(input("Player ID does not exist! Enter a new Player ID: "))
            break
        except:
            print("Invalid input! Please enter a new choice")
            return
    while True:
        try:
            game_id = int(input("Enter Game ID to add a game to: "))
            while game_id > num_games or game_id <= 0:
                game_id = int(input("Game ID does not exist! Enter a new Game ID: "))
            break
        except:
            print("Invalid input! Please enter a new choice")
            return
    cursor.execute("INSERT OR IGNORE INTO player_library(pID, gID) VALUES (?, ?)", (player_id, game_id))

def add_to_console(): # Add a game to a console
    cursor.execute("SELECT COUNT(gID) FROM games;")
    num_games = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(cID) FROM consoles;")
    num_consoles = cursor.fetchone()[0]
    while True:
        try:
            console_id = int(input("Enter Console ID to add a game to: "))
            while console_id > num_consoles or console_id <= 0:
                console_id = int(input("Console ID does not exist! Enter a new Console ID: "))
            break
        except:
            print("Invalid input! Please enter a new choice")
            return
    while True:
        try:
            game_id = int(input("Enter Game ID to add a game to: "))
            while game_id > num_games or game_id <= 0:
                game_id = int(input("Game ID does not exist! Enter a new Game ID: "))
            break
        except:
            print("Invalid input! Please enter a new choice")
            return
    cursor.execute("INSERT OR IGNORE INTO game_platforms(cID, gID) VALUES (?, ?)", (console_id, game_id))

def reset_tables(): # Reset the tables so that they are all empty
    cursor.execute("DROP TABLE IF EXISTS players;")
    cursor.execute("DROP TABLE IF EXISTS games;")
    cursor.execute("DROP TABLE IF EXISTS consoles;")
    cursor.execute("DROP TABLE IF EXISTS player_library;")
    cursor.execute("DROP TABLE IF EXISTS game_platforms;")
    
    cursor.execute("CREATE TABLE IF NOT EXISTS games(gID INTEGER PRIMARY KEY NOT NULL, game_name TEXT, player_count INTEGER, size TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS consoles(cID INTEGER PRIMARY KEY NOT NULL, console_name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS players(pID INTEGER PRIMARY KEY NOT NULL, player_name TEXT, fname TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS player_library(pID INTEGER NOT NULL REFERENCES players(pID), gID INTEGER NOT NULL REFERENCES games(gID), PRIMARY KEY (pID, gID))")
    cursor.execute("CREATE TABLE IF NOT EXISTS game_platforms(cID INTEGER NOT NULL REFERENCES consoles(cID), gID INTEGER NOT NULL REFERENCES games(gID), PRIMARY KEY (cID, gID))")

def get_game_by_player(): # View games owned by a given player
    cursor.execute("SELECT COUNT(pID) FROM players;")
    num_players = cursor.fetchone()[0]
    while True:
        try:
            player_id = int(input("Enter Player ID whose games you wish to view: "))
            while player_id > num_players or player_id <= 0:
                player_id = int(input("Player ID does not exist! Enter a new Player ID: "))
            break
        except:
            print("Invalid input! Please enter a new choice")
            return
    cursor.execute("SELECT games.* FROM player_library JOIN games ON player_library.gID = games.gID WHERE player_library.pID = ?;", (player_id,))
    fetched = cursor.fetchall()
    cursor.execute("SELECT players.fname FROM player_library JOIN players ON players.pID = ?;", (player_id,))
    player_name = cursor.fetchone()
    print("{:<15} | {:<9} | {:<30} | {:<30} | {:<9}".format("Player Name", "Game ID", "Game Name", "Player Count", "Size"))
    print("-" * 120)
    for game in fetched:
        print("{:<15} | {:<9} | {:<30} | {:<30} | {:<9}".format(player_name[0], game[0], game[1], game[2], game[3]))

def get_game_by_console(): # View games playable on a given console
    cursor.execute("SELECT COUNT(cID) FROM consoles;")
    num_consoles = cursor.fetchone()[0]
    while True:
        try:
            console_id = int(input("Enter Console ID whose games you wish to view: "))
            while console_id > num_consoles or console_id <= 0:
                console_id = int(input("Console ID does not exist! Enter a new console ID: "))
            break
        except:
            print("Invalid input! Please enter a new choice")
            return
    cursor.execute("SELECT games.* FROM game_platforms JOIN games ON game_platforms.gID = games.gID WHERE game_platforms.cID = ?;", (console_id,))
    fetched = cursor.fetchall()
    cursor.execute("SELECT consoles.console_name FROM game_platforms JOIN consoles ON consoles.cID = ?;", (console_id,))
    console_name = cursor.fetchone()
    print("{:<15} | {:<9} | {:<30} | {:<30} | {:<9}".format("Console Name", "Game ID", "Game Name", "console Count", "Size"))
    print("-" * 120)
    for game in fetched:
        print("{:<15} | {:<9} | {:<30} | {:<30} | {:<9}".format(console_name[0], game[0], game[1], game[2], game[3]))

current_state = 1 # State variable to keep track of menus
connection = sqlite3.connect("games_database_jackr.db") # Create database
cursor = connection.cursor() # Cursor that looks through the database
flag = False # Flag to exit database when program is finished
while not flag:
      give_options()
connection.close()
