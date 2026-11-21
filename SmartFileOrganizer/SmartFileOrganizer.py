from pathlib import Path

# F:\Frontend\PythonExp\SmartFileOrganizer\Test

path = input("Введіть шлях до папки: ")
folder = Path(path)

folders = ["Images", "Videos", "Documents", "Archives", "Audio", "Code"]

categories = {
    ".png": "Images",
    ".jpg": "Images",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".mp4": "Videos",
    ".pdf": "Documents",
    ".zip": "Archives"
}

def createFolders():
    for name in folders:
        new_folder = folder / name
        new_folder.mkdir(exist_ok=True)
    
def getFile():
    for file in folder.iterdir():
        file_name = file.name
        if file.is_file():
            category = categories.get(file.suffix)
            
            if category:
                (folder / category).mkdir(exist_ok=True)
            if file_name.exists():
                file.rename(folder / category / file_name)
            
            print(f"{file_name} => {category}")
            

def organizer():    
    if folder.exists():
        print("Right!!")
        getFile()
        createFolders()
    else:
        print("Wrong syntacsis!!")
        
organizer()