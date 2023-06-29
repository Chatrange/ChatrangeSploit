import os
import sys
import sqlite3
import shutil

cookie_file_names = ['Cookies', 'Cookies-journal']
cookie_folder_path = os.path.join(os.environ['LOCALAPPDATA'], 'Google\\Chrome\\User Data\\Default')

for file_name in cookie_file_names:
    file_path = os.path.join(cookie_folder_path, file_name)
    backup_path = file_path + '.backup'
    if os.path.exists(file_path):
        shutil.copy(file_path, backup_path)
        with sqlite3.connect(file_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM cookies')
            cookies = cursor.fetchall()
            for cookie in cookies:
                print(cookie)

