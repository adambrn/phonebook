import sqlite3

def init_db(db_path):
    conn = sqlite3.connect(db_path)
    sqlite_create_table_query = """
        CREATE TABLE
        if not exists

        people (
            id INTEGER PRIMARY KEY,
            name TEXT ,
            father_name TEXT ,
            last_name TEXT ,
            phone TEXT ,
            comment TEXT 
        );
    """

    conn.execute(
        sqlite_create_table_query
    )
    conn.close()

def db_query(db_path,query,data):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query,data)
    conn.commit()
    conn.close()

def db_insert_people(db_path,data):
    insert_query = 'INSERT INTO people (name ,father_name ,last_name, phone, comment ) VALUES(?,?,?,?,?)'
    db_query(db_path,insert_query,data)
    
def db_insert_peoples(db_path,data):
    print(data)
    insert_query = 'INSERT INTO people (name ,father_name ,last_name, phone, comment ) VALUES(?,?,?,?,?)'
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.executemany(insert_query,data)
    conn.commit()
    conn.close()

def db_update_people(db_path,data,id):
    
    update_query = 'UPDATE people set name=? ,father_name=? ,last_name=?, phone=?, comment=?  WHERE id=?'
    update_tuple = list(data) 
    update_tuple.append(id)
    data_and_id = tuple(update_tuple)
    db_query(db_path,update_query,data_and_id)

def db_get(db_path,table):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor() 
    get_query = f'SELECT * FROM {table}'
    data = cur.execute(get_query)
    data_tuple =[tuple(i) for i in data]
    conn.close()
    return data_tuple

def db_delete(db_path,table,id):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor() 
    delete_query = f'DELETE FROM {table} WHERE id={id}'
    cur.execute(delete_query)
    conn.commit()
    conn.close()

