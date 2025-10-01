import json
import typing
import os

class ExitLoop(Exception):
    pass

class FileError(Exception):
    pass

try :
    file = None
    file = open("lists.json" , "r+")
    file.seek(0)
    video_list:list[dict[str, str]] = json.load(file)
except json.decoder.JSONDecodeError :
    video_list = []
except Exception as e:
    input(f"An error {e} was occurred while writing to file! Enter to close the App!")
    raise FileError()
finally : 
    if file != None:
        file.flush()
        os.fsync(file.fileno())
        file.close()

def dump_list_in_file(video_list:list[dict[str,str]])->None:
    try:
        file = open("lists.json","w")
    except Exception as e:
        input(f"An error {e} was occurred while writing to file! Enter to close the App!")
        raise FileError()
        
    file.seek(0)
    json.dump(video_list,file)
    file.flush()
    os.fsync(file.fileno())
    file.close()
    

def show_entire_list(video_list:list[dict[str,str]])->None:
    os.system("clear")

    if video_list == [] : 
        print("list is empty , please select option 2 to atleast add one video in list")
        input("press Enter to continue !")
        return

    for obj in enumerate(video_list , start =1):
        print(f"{obj[0]}. video name : {obj[1]["name"]} and duration is : {obj[1]["time"]}")

    print("*"*55)
    input("press Enter to continue !") 

def add_video_in_list(video_list:list[dict[str,str]])->None:
    os.system("clear")
    flag:bool = True

    if video_list != []:
        input("press Enter to see the current list to select the position to add the video!")
        show_entire_list(video_list)
    else : 
        print("The list is empty , enter the details of first video: ")
        flag = False

    video_name:str = input("enter the new video name: ")
    video_time:str = input("enter the new video duration: ")

    if flag:
        try:
            video_index:int = int(input("enter the position you want to add this video , if none given or invalid input given then added at end as default: "))-1
        except Exception: 
            print("Invalid input was given, adding the video at end!")
            video_index = len(video_list)
    else :
        print("Since the list is Empty , Adding the video to first position!")
        video_index:int = 0

    video_list.insert(video_index,{"name":video_name , "time":video_time})
    os.system("clear")
    input(f"\n the video {video_name} was added successfully at position : {video_index+1} press Enter to see the new list!")
    show_entire_list(video_list)
    dump_list_in_file(video_list)

def update_video_in_list(video_list:list[dict[str,str]])->None:
    os.system("clear")
    input("press Enter to see the current list and to select the video to update! ")
    show_entire_list(video_list)
    if video_list ==[] : return

    try:
        video_index:int = int(input("enter the position of video to be updated: "))-1
    except Exception: video_index = len(video_list)

    while(video_index>=len(video_list)):
        try:
            video_index:int = int(input("Invalid position , please select a valid position: "))-1
        except Exception: video_index = len(video_list)

    video_name:str = input("enter the new video name: ")
    video_time:str = input("enter the new video duration: ")
    old_video_name:str = video_list[video_index]["name"]
    video_list[video_index] = {"name":video_name , "time":video_time}
    os.system("clear")
    input(f"\n The video {old_video_name} was updated successfully at position : {video_index+1} by new video {video_name} ! press Enter to see the new list!")
    show_entire_list(video_list)
    dump_list_in_file(video_list)

def delete_video_in_list(video_list:list[dict[str,str]])->None:
    os.system("clear")
    input("press Enter to see the current list and to select the video to delete! ")
    show_entire_list(video_list)
    if video_list ==[] : return

    try:
        video_index:int = int(input("enter the position of video to be deleted: "))-1
    except Exception: video_index = len(video_list)

    while(video_index>=len(video_list)):
        try:
            video_index:int = int(input("Invalid position , please select a valid position: "))-1
        except Exception: video_index = len(video_list)

    old_video_name:str = video_list[video_index]["name"]
    video_list.__delitem__(video_index)
    os.system("clear")
    input(f"\n The video {old_video_name} was deleted successfully at position : {video_index+1} ! press Enter to see the new list!")
    show_entire_list(video_list)
    dump_list_in_file(video_list)

def execute_choice(choice:str)->typing.Optional[Exception]:
    match choice :
        case "1" : show_entire_list(video_list)
        case "2" : add_video_in_list(video_list)
        case "3" : update_video_in_list(video_list)
        case "4" : delete_video_in_list(video_list)
        case "5" : raise ExitLoop()
        case _ : input(f"invalid input,{choice} please press Enter to reselect !")