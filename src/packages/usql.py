"""

Conección con la base de datos para los usuarios

"""

import sqlite3

try:
    user_connect = sqlite3.connect( 'database/udb' )
    user_cursor = user_connect.cursor()

    def ulist():
        user_cursor.execute( 'SELECT * FROM users' )
        rows = user_cursor.fetchall()

        for row in rows:
            print( row )

except Exception as ex:
    print( ex )