import os


def convert():
    pwd = os.getcwd()
    folder = os.path.join(pwd,'Parser/mp4_downloads')

    for filename in os.listdir(folder):
        if filename.endswith('.mp4'):
            old_file = os.path.join(folder, filename)
            new_file = os.path.join(folder, filename[:-4] + '.mp3')
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} to {new_file}')

    print('Renaming complete!')
