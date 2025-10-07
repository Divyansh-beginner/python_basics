import os
import sqlite3 as sql
from typing import Optional
_conn = None

class ExitLoop(Exception) : pass

def get_connection()->sql.Connection:
    global _conn
    if _conn is None :
        _conn = sql.connect("yt_videos_list.db")
    return _conn
 
def close_connection()-> None:
    conn = get_connection()
    conn.close()

def get_cursor_from_connection_and_make_table_if_not_exists(conn:sql.Connection)->sql.Cursor:
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

def execute_query_to_get_list()->list[tuple[int , str , str]]:
    conn = get_connection()
    cur = get_cursor_from_connection_and_make_table_if_not_exists(conn)
    vid_list = list(cur.execute('''
    select position , video_name , duration from video_list order by position;
    '''))
    return vid_list

def execute_query_to_add_vid_name_time_and_position(name:str , time:str , pos:int)->None:
    conn = get_connection()
    cur = get_cursor_from_connection_and_make_table_if_not_exists(conn)
    vid_list:list[tuple[int , str, str]] = execute_query_to_get_list()

    if vid_list == []: 
        print("the list is empty , adding the first video at first position")
        pos = 1
    elif pos>len(vid_list)+1 : 
        pos = len(vid_list)+1
        print(f"given position is invalid , adding video at end at last position {pos}")
    else : print(f"adding the video at {pos} position")

    cur.execute('''
    update video_list set position = position+1 where position>=(?);
    ''',(pos,))
    cur.execute('''
    insert into video_list(position , video_name , duration) values(?,?,?);
    ''',(pos , name , time))
    conn.commit()
    input("successfully added video , press Enter to continue. ")

def execute_query_to_update_video_at_given_position(name:str , time:str ,pos:int)->None:
    conn = get_connection()
    cur = get_cursor_from_connection_and_make_table_if_not_exists(conn)
    vid_list:list[tuple[int , str, str]] = execute_query_to_get_list()

    while(pos>len(vid_list)):
        pos = int(input("invalid position , enter the valid position: "))

    cur.execute('''
    update video_list set video_name = (?) , duration = (?) where position = (?);
    ''',(name , time , pos))
    conn.commit()

def execute_query_to_delete_video_at_given_position(pos:int)->None:
    conn = get_connection()
    cur = get_cursor_from_connection_and_make_table_if_not_exists(conn)
    vid_list:list[tuple[int , str, str]] = execute_query_to_get_list()

    while(pos>len(vid_list)):
        pos = int(input("invalid position , enter the valid position: "))

    cur.execute('''
    delete from video_list where position = (?);
    ''',(pos,))
    cur.execute('''
    update video_list set position = position-1 where position>(?)
    ''',(pos,))
    conn.commit()

def execute_query_to_delete_table()->None:
    conn = get_connection()
    cur = get_cursor_from_connection_and_make_table_if_not_exists(conn)
    cur.execute("drop table video_list;")
    conn.commit()

#------------------------------------------------------------------------

def get_name()->str:
    name = input("enter the name of video: ")
    return name

def get_time()->str:
    time = input("enter the duration: ")
    return time

def get_position()->str:
    msg = "enter the position: "
    position:int = 1
    
    while(True):
        try: 
            position = int(input(msg))
        except ValueError: 
            msg = "invalid input , Enter a valid input: "
            continue
        if position<1 : msg = "position can't be below 1, enter a valid position: "
        else : break

    return position

def print_the_list(vlist:list[tuple[int , str , str]])->None:
    os.system("clear")
    if vlist == [] :
        print("the list is empty!")
    else: 
        for entries in vlist :
            print(f"{entries[0]}. video name: {entries[1]} , duration: {entries[2]}")
    print("*"*55)
    input("press Enter to continue")

#------------------------------------------------------------------------

def show_list()->bool:
    vid_list = execute_query_to_get_list()
    print_the_list(vid_list)
    return not (vid_list == [])

def add_video()->None:
    flag:bool = show_list()
    name = get_name()
    time = get_time()
    position = 1
    if flag:
        position = get_position()
    execute_query_to_add_vid_name_time_and_position(name , time , position)
    show_list()

def update_video()->None:
    flag:bool = show_list()
    if flag:
        position = get_position()
        name = get_name()
        duration = get_time()
        execute_query_to_update_video_at_given_position(name , duration ,position)
        show_list()

def delete_video()->None:
    flag:bool = show_list()
    if flag:
        position = get_position()
        execute_query_to_delete_video_at_given_position(position)
        show_list()

def delete_list()->None:
    confirmation:str = input("Are you sure you want to Delete the list? enter 'y' or 'Y' to delete , anything else to keep: ")
    if confirmation == 'y' or confirmation == "Y": 
        execute_query_to_delete_table()
    else : return

#--------------------------------------------------------------------------

def print_choices()->None:
    os.system("clear")
    print("Welcome to yt manager app, this version of app uses sqlite db , choose an option: ")
    print("1. To show the entire list of videos.")
    print("2. To add a video in the list.")
    print("3. To update a video details.")
    print("4. To delete a video.")
    print("5. To delete all entries and make a new list.")
    print("6. To exit the app.")

def execute_choice(choice:str)->Optional[Exception]:
    match choice :
        case "1" : show_list()
        case "2" : add_video()
        case "3" : update_video()
        case "4" : delete_video()
        case "5" : delete_list()
        case "6" : raise ExitLoop()
        case _   : input(f"invalid input '{choice}' , please press Enter to reselect !")

def get_final_choice_to_exit_app()->bool:
    os.system("clear")
    confirmation = input("Do you want to exit the app? enter 'y' or 'Y' to exit else anything to continue in app: ")
    os.system("clear")
    choice:bool = (confirmation == 'y' or confirmation == 'Y')
    if choice : close_connection()
    return choice
