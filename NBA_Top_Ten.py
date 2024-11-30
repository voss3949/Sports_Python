import sqlite3

# Create a connection to the database
conn = sqlite3.connect('nba.db')

# Create a cursor object to interact with the database
cur = conn.cursor()

# Create a table to store the players
cur.execute('''CREATE TABLE IF NOT EXISTS players
               (id INTEGER PRIMARY KEY,
                name TEXT,
                team TEXT,
                points INTEGER,
                assists INTEGER,
                rebounds INTEGER)''')

# Insert the top ten players into the table
players = [('LeBron James', 'Los Angeles Lakers', 25, 8, 7),
           ('Kevin Durant', 'Brooklyn Nets', 28, 5, 7),
           ('Stephen Curry', 'Golden State Warriors', 29, 6, 5),
           ('Kawhi Leonard', 'Los Angeles Clippers', 26, 5, 7),
           ('Giannis Antetokounmpo', 'Milwaukee Bucks', 27, 5, 11),
           ('James Harden', 'Brooklyn Nets', 25, 11, 8),
           ('Luka Doncic', 'Dallas Mavericks', 29, 8, 9),
           ('Nikola Jokic', 'Denver Nuggets', 27, 8, 11),
           ('Joel Embiid', 'Philadelphia 76ers', 29, 3, 11),
           ('Damian Lillard', 'Portland Trail Blazers', 29, 7, 4)]

for player in players:
    cur.execute("INSERT INTO players (name, team, points, assists, rebounds) VALUES (?, ?, ?, ?, ?)", player)

# Commit the changes to the database
conn.commit()

# Retrieve the top ten players from the database
cur.execute("SELECT * FROM players ORDER BY points DESC LIMIT 10")

# Print the results
print("Top Ten NBA Players:")
for row in cur.fetchall():
    print(row[1], "-", row[2], "- Points:", row[3], "- Assists:", row[4], "- Rebounds:", row[5])

# Close the cursor and the connection to the database
cur.close()
conn.close()

#This code creates a database called "nba.db" and a table called "players" with columns for player name, team, points, assists, and rebounds. It then inserts the top ten NBA players into the table and retrieves them using an SQL query that orders the rows by points and limits the result to the top ten. Finally, it prints the results to the console. Note that the player data used in this example is fictional and not based on any actual NBA statistics.




