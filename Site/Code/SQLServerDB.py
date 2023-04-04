import os
import pyodbc

def drivers():
    driver_list =[]
    drivers = pyodbc.drivers()
    for driver in drivers:
        driver_list.append(driver)

    return driver_list

def DBExec(str, db):
    try:
        cnxn_str = os.getenv('connStr')+"Database="+db+";"
        cnxn = pyodbc.connect(cnxn_str)
        cursor = cnxn.cursor()
        cursor.execute(str)
        records = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        tbl = []
        for i in records:
            item = {}
            for j in range(len(columns)):
                item[columns[j]] = i[j]
            tbl.append(item)
        cnxn.close()
        return tbl
    except:
        return

def DBExecCommand(str, db):
    try:
        cnxn_str = os.getenv('connStr') + "Database=" + db + ";"
        cnxn = pyodbc.connect(cnxn_str)
        cursor = cnxn.cursor()
        cursor.execute(str)
        cnxn.commit()
        cnxn.close()
        return True
    except:
        return False

