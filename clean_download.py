import os
import pathlib
import json
import time

from watchdog.observers import Observer

from watchdog.events import FileSystemEventHandler


def makeDirs(our_folders):
    for folder in our_folders:
        if not os.path.exists(folder):
            os.makedirs(folder)


def move_files(file_type_doc, file_type_vid, file_type_pic, file_type_zip, file_type_torrent, file_type_model,
               dirs):
    makeDirs(MyHandler.folders)
    files = os.listdir()
    print("Before Move: " + str(len(files)))

    for file in files:
        e = pathlib.Path(file).suffix

        if e in file_type_doc:
            new_path = dirs[0] + '/' + file
            os.rename(file, new_path)

        elif e in file_type_vid:
            new_path = dirs[1] + '/' + file
            os.rename(file, new_path)

        elif e in file_type_pic:
            new_path = dirs[2] + '/' + file
            os.rename(file, new_path)

        elif e in file_type_zip:
            new_path = dirs[3] + '/' + file
            os.rename(file, new_path)

        elif e in file_type_torrent:
            new_path = dirs[4] + '/' + file
            os.rename(file, new_path)

        elif e in file_type_model:
            new_path = dirs[5] + '/' + file
            os.rename(file, new_path)

        elif e == ' ':
            new_path = dirs[6] + '/' + file
            os.rename(file, new_path)

        # else:
        #     new_path = dirs[4] + '/' + file
        #     os.rename(file, new_path)

    print('Files moved')
    files = os.listdir()
    print("After Move: " + str(len(files)))


class MyHandler(FileSystemEventHandler):
    os.chdir('/home/shivam/Downloads')

    ext = []

    folders = ['Documents', 'Videos', 'Pictures', 'zips', 'torrent', 'model', 'Others']

    our_docs_type = ['.odt', '.pdf', '.xls', '.xlsx', '.ods', '.ppt', '.pptx', '.txt', '.docx', '.csv', '.doc']
    our_pic_type = ['.tif', '.jpg', '.gif', '.png', '.jpeg']
    our_vid_type = ['.mp4', '.avi', '.flv', 'wmv', '.mov', '.webm', '.mkv']
    our_zip_type = ['.a', '.ar', '.cpio', '.shar', '.lbr', '.iso', '.mar', '.sbx', '.tar', '.gz', '.lz', '.7z',
                    '.apk', '.jar', '.rar', '.tar.gz', '.tgz', '.zip', '.zipx', '.zz', '.tar.xz', '.deb', '.xz', '.sh']
    our_torrent_type = ['.torrent']
    our_model_type = ['.h5', '.pt']

    def on_modified(self, event):
        move_files(self, MyHandler.our_docs_type, MyHandler.our_vid_type, MyHandler.our_pic_type,
                   MyHandler.our_zip_type,
                   MyHandler.our_torrent_type, MyHandler.our_model_type, MyHandler.folders)


folder_to_track = '/home/shivam/Downloads'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    observer.stop()

observer.join()
