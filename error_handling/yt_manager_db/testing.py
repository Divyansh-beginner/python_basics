import sqlite3 as sql

_conn = None
def get_connection()->sql.Connection:
    global _conn
    if _conn is None :
        _conn = sql.connect("text.db")
    return _conn

def get_cursor(conn:sql.Connection)->sql.Cursor:
    cur = conn.cursor()
    cur.execute('''
    create table if not exists video_list(
    id integer primary key autoincrement,
    video_name text not null,
    duration text not null,
    position integer not null
    );
    ''')
    conn.commit()
    return cur

conn = get_connection()
cur = get_cursor(conn)
i:int = 1
given_number = 5
# cur.execute('''
# update video_list set position = position +1 where position >= (?);
# ''',(given_number,))
# cur.execute("insert into video_list(video_name , duration , position) values(?,?,?);",(f"newvideo{i}" , f"{5+i-1}min" , i))
# cur.execute("update video_list set position = 2 , video_name = 'newvideo2' , duration = '6min' where id = 2;")
cur.execute("update video_list set position =(?) ,video_name = (?) ,duration =(?) where id = 1;",(3 , "nnn" , "45min"))
conn.commit()
i += 1
vlist = list(cur.execute("select position ,video_name , duration from video_list order by position;"))
print(vlist)
# cur.execute("drop table video_list;")

