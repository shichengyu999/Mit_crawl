import os
from down_load import down_load

def down_load_di_type(save_path:str, url_base:str, objects:str):
    try:
        try:
            os.mkdir(save_path+"\\"+objects)
        except FileExistsError:
            pass
        if not down_load(url_base+"resources/"+objects+"/", save_path+"\\"+objects):
            os.removedirs(save_path+"\\"+objects)
    except:
        print(f"Failed to download {objects}, maybe the content not exist. ")

object_list=["assignments","exams","lecture-notes","recitations","labs"]

list_input = []
with open("settings.txt",'r',encoding='utf-8') as f:
    text = f.read()
list_input = text.split("\n")
    
j = 0
for i in range(len(list_input)//2):
    url_base = list_input[j]
    save_path = list_input[j+1]
    for object in object_list:
        down_load_di_type(save_path,url_base,object)
    j += 2 
        
print("Download finished!")

