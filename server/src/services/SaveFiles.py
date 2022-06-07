from os import rename,path
import uuid


from config.conf import ALLOWED_EXTENSIONS,IMAGE_PATH,VIDEO_PATH
def safeFile(file):
    left_index = file.lfind('.')
    right_index = file.rfind('.')
    if(left_index == right_index):
        for extention in ALLOWED_EXTENSIONS:
            if(file.endswith(extention)):
                new_file_name = uuid.uuid4()
                return new_file_name
        return False
    return False

def File(file):
    file_extension = path.splitext(file)[1]
    if(not safeFile(file.filename)):
        return False
    new_file = safeFile(file.filename)+'.'+file_extension
    rename(file.filename,new_file)
    if(file.filename.endswith('.mp4')):
        file.save(path.join(VIDEO_PATH, file.filename)) 
    file.save(path.join(IMAGE_PATH, file.filename))   


def Files(files) -> bool:
    safe_files = []
    for file in files:
        file_extension = path.splitext(file)[1]
        if (not safeFile(file.filename)):
            return False
        new_file = safeFile(file.filename)+'.'+file_extension
        rename(file.filename,new_file)
        safe_files.append(new_file)
    for file in safe_files:
        if(file.filename.endswith('.mp4')):
            file.save(path.join(VIDEO_PATH, file.filename)) 
        file.save(path.join(IMAGE_PATH, file.filename))        
               
