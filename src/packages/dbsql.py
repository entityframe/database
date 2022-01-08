"""

Conección con la base de datos general

"""

import sqlite3

try:
    connect = sqlite3.connect( 'database/db' )
    cursor = connect.cursor()

except Exception as ex:
    print( ex )