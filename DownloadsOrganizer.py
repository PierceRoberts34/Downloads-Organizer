import FileType
import os
import time
import eyed3
import shutil


def fileIdentify(downloadsPath,filepath):
    # Identify Files
    fullpath = os.path.join(downloadsPath,filepath)
    file_tup = os.path.splitext(filepath)

    # Set the filename and extension
    filename = file_tup[0]
    extension = file_tup[1]

    # Get the creation time
    c_time = os.path.getctime(fullpath)
    ti_m = time.ctime(c_time)
    time_obj = time.strptime(ti_m)
    subfolders = ""
    file = ""

    # Define the file type and appropriate subfolder
    match (extension):

        case '.jpg'|'.png'|'.gif'|'.webp':
            date = time.strftime("%Y-%m-%d", time_obj)
            file = FileType.Photo(filename, extension, date)
            subfolders = f"PHOTOS//{file.get_date()}"

        case '.flac'|'.mp3':
            audiotag = eyed3.load(fullpath)
            file = FileType.Music(filename, extension, audiotag.tag.getBestDate(), audiotag.tag.album_artist, audiotag.tag.album)
            if (file.get_extension() == '.mp3'):
                type = "MP3"
            else:
                type = "FLAC"
            subfolders = f"MUSIC//{type}//{file.get_albumartist()} - {file.get_album()} ({file.get_year()})"

        case '.pdf'|'.xls'|'.xlsx'|'.ods'|'.xlsm'|'.csv'|'.doc'|'.docx'|'.odf'|'.docm'|'.ppt'|'.pptx'|'.pptm'|'.odp':
            file = FileType.FileType(filename,extension)
            match file.get_extension():
                case '.pdf':
                    type = "PDF"
                case '.xls'|'.xlsx'|'.ods'|'.xlsm'|'.csv':
                    type = "SPREADSHEET"
                case '.doc'|'.docx'|'.odf'|'.docm':
                    type = "WORD"
                case '.ppt'|'.pptx'|'.pptm'|'.odp':
                    type = "PRESENTATION"
            subfolders = f"DOCUMENTS//{type}"

        case '.mp4'|'.mkv'|'.avi'|'.mov'|'.m4v':
            subfolders = "VIDEOS"

        case '.torrent':
            subfolders = "TORRENTS"

        case '.zip':
            subfolders = "ARCHIVES"

        case '.exe'| '.msi':
            subfolders = "PROGRAMS AND INSTALLERS"

        case _:
            subfolders = "MISC"
    return subfolders
    

def main():
    downloadsPath = os.path.join(os.path.expanduser('~'),'downloads')
    # Create an object for each file
    for filepath in os.listdir(downloadsPath):
        if (os.path.isfile(os.path.join(downloadsPath,filepath))):
            # Identify the proper folder structure
            subfolders = fileIdentify(downloadsPath,filepath)

            source = os.path.join(downloadsPath, filepath)
            folderpath = os.path.join(downloadsPath,subfolders)
            destination = os.path.join(folderpath,filepath)

            # Create needed subfolders
            os.makedirs(folderpath, exist_ok=True)

            # Move the file to the destination
            shutil.move(source, destination)
    



if __name__ == '__main__':
    main()
