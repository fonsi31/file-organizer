import os
import shutil

def get_category(ext, categories):
    for Category, Extensions in categories.items():
        if ext.lower() in Extensions:
            return Category
    
    return "Others"

def sort(directory_path, categories):
    for file in os.listdir(directory_path): #scan the contents of the directory
        file_path = os.path.join(directory_path, file) #full file path

        if os.path.isfile(file_path): #checks if the content is a file and not a directory
            name, ext = os.path.splitext(file)
            category = get_category(ext, categories)

            subfolder_path = os.path.join(directory_path, category)
            if not os.path.isdir(subfolder_path): #if the subfolder doesn't exists yet
                #create that subfolder
                #move the file there
                os.makedirs(subfolder_path, exist_ok=True)
                dst = os.path.join(subfolder_path, file)
                shutil.move(file_path, dst)
            else: #if the subfolder already exists
                dst = os.path.join(subfolder_path, file)
                i = 1
                while os.path.exists(dst):
                    new_name = f"{name}({i}){ext}"
                    dst = os.path.join(subfolder_path, new_name)
                    i += 1
                shutil.move(file_path, dst)  

    print(f"Directory '{directory_path}' is successfuly organized")  

def main():
    categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".c", ".java"],
    "Executables": [".exe", ".msi"],
    "Others": []  # fallback
    }

    while True:
        directory_path = input("Please paste or type the absolute directory path here: ")

        if directory_path.lower() == "exit":
            break

        if not os.path.isdir(directory_path): #if you pass this, enter and access the directory
            print(f"'{directory_path}' doesn't exists")
            continue
  
        sort(directory_path, categories)
        break

if __name__ == "__main__":
    main()