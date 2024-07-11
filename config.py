from dotenv import load_dotenv
import os

load_dotenv()

class config:
    VK_TOKEN = str(os.environ.get("VK_TOKEN"))
    OPENAI_API_KEY = str(os.environ.get("OPENAI_API_KEY"))
    TRIGGER = str(os.environ.get("TRIGGER"))
    MSG_TEXT = str(os.environ.get("MSG_TEXT"))
    GROUP_ID = str(os.environ.get("GROUP_ID"))
    POST_ID = str(os.environ.get("POST_ID"))
    if not os.path.exists("instruct.txt"):
        with open("instruct.txt", "w", encoding="utf-8") as file:
            pass
        with open("instruct.txt", "r", encoding="utf-8") as file:
            system_instruct=file.read()
        
            system_instruct=file.read()
    else:
        with open("instruct.txt", "r", encoding="utf-8") as file:
                system_instruct=file.read()
        
        

