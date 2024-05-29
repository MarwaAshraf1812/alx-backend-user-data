#!/usr/bin/env python3
"""
Main file
"""

# get_db = __import__('filtered_logger').get_db

# db = get_db()
# cursor = db.cursor()
# cursor.execute("SELECT COUNT(*) FROM users;")
# for row in cursor:
#     print(row[0])
# cursor.close()
# db.close()

# hash_password = __import__('encrypt_password').hash_password

# password = "MyAmazingPassw0rd"
# print(hash_password(password))
# print(hash_password(password))

hash_password = __import__('encrypt_password').hash_password
is_valid = __import__('encrypt_password').is_valid

password = "MyAmazingPassw0rd"
encrypted_password = hash_password(password)
print(encrypted_password)
print(is_valid(encrypted_password, password))