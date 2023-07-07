from os import scandir, rename
from os.path import exists, join, splitext
from shutil import move
import logging

#DIRECTORIES
source_dir = 'C:\\Users\\Bob\\Downloads'
dest_sounds = 'C:\\Users\\Bob\\Desktop\\Sounds'
dest_music = 'C:\\Users\\Bob\\Desktop\\Music'
dest_videos = 'C:\\Users\\Bob\\Desktop\\Videos'
dest_images = 'C:\\Users\\Bob\\Desktop\\Images'
dest_documents = 'C:\\Users\\Bob\\Desktop\\Documents'

image_extensions = ['.jpg','.jpeg','.jpe','.jif','.jfi','.png','.gif','webp','.tif','.tiff','.k25','.bmp','.dib','.heif','.heic','.ind','.indt','.indd','.jp2','.jk2','.jpf' '.jfif']

video_extensions = ['.webm','.mpg','.mp2','.mpeg','.mpe','.mpv','.ogg','.mp4','.mp4v','.m4v','.avi','.wmv','.mov','.qt','.flv','.swf','.avchd']

audio_extensions = ['.m4a','.flac','.mp3','.wav','.wma','.aac']

document_extensions = ['.doc','.docx','.odf','.pdf','.xls','.xlsx','.ppt','.pptx']

def make_unique(dest,name):
    filename, extension = splitext(name)
    counter = 1
    while exists(f'{dest}/{name}'):
        name = (f'{filename}({str(counter)}){extension}')
        counter += 1

    return name

def move_file(dest,entry,name):
    if exists(f'{dest}/{name}'):
        unique_name = make_unique(dest,name)
        old_name = join(dest,name)
        new_name = join(dest,unique_name)
        rename(old_name,new_name)
    move(entry,dest)

def desktop_cleaner():
    with scandir(source_dir) as entries:
        for entry in entries:
            name = entry.name
            check_audio_files(entry,name)
            check_video_files(entry,name)
            check_image_files(entry,name)
            check_document_files(entry,name)

def check_audio_files(entry,name):
    for audio_extension in audio_extensions:
        if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
            if entry.stat().st_size < 10_000_000 or 'SFX' in name:
                dest = dest_sounds
            else:
                dest = dest_music
            move_file(dest,entry,name)
            logging.info(f'Moved audio file: {name}')


def check_video_files(entry,name):
    for video_extension in video_extensions:
        if name.endswith(video_extension) or name.endswith(video_extension.upper()):
            dest = dest_videos
            move_file(dest,entry,name)
            logging.info(f'Moved video file: {name}')

def check_image_files(entry,name):
    for image_extension in image_extensions:
        if name.endswith(image_extension) or name.endswith(image_extension.upper()):
            dest = dest_images
            move_file(dest,entry,name)
            logging.info(f'Moved image file: {name}')


def check_document_files(entry,name):
    for document_extension in document_extensions:
        if name.endswith(document_extension) or name.endswith(document_extension.upper()):
            dest = dest_documents
            move_file(dest,entry,name)
            logging.info(f'Moved document file: {name}')


desktop_cleaner()