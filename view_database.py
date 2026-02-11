import sqlite3

# Connect to database
conn = sqlite3.connect('d:/django/db.sqlite3')
cursor = conn.cursor()

# View all skills
print("=== SKILLS ===")
cursor.execute("SELECT * FROM portfolio_app_skill")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Title: {row[1]}, Description: {row[2]}")

print("\n=== PROJECTS ===")
cursor.execute("SELECT * FROM portfolio_app_project")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Title: {row[1]}, Description: {row[2]}")

print("\n=== CONTACT MESSAGES ===")
cursor.execute("SELECT * FROM portfolio_app_contactmessage")
for row in cursor.fetchall():
    print(f"From: {row[1]}, Email: {row[2]}, Subject: {row[3]}")

conn.close()
