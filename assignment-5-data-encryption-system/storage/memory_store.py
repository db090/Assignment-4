import json 
import os

#Path to the JSON file
DATA_FILE="data_store.json"

# load all data from  the json file
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE,"r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}
        
#save updated data to the json file
def save_data(data:dict):
    with open(DATA_FILE,"w") as file:
        json.dump(data,file,indent=4)

# Store a new encrypted entry
def store_data(key:str,encrypted_text:str,hashed_passkey:str):
    data=load_data()
    data[key]={
        "encrypted_text":encrypted_text,
        "passkey":hashed_passkey
    }
    save_data(data)

def retrieve_data(key:str):
    data=load_data()
    return data.get(key)

def get_all_keys():
    data=load_data()
    return list(data.keys())

def clear_store():
    save_data({})