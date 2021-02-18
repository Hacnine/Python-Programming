
# print(os.getcwd())
import os
from datetime import datetime

os.chdir('C:\Var')
# os.makedirs('made by os/made sub dir/make sub sub dir')
# os.mkdir('foleder made by mkdir')
# os.removedirs('made by os/made sub dir/make sub sub dir')
# os.rmdir('made by os/made sub dir/make sub sub dir')

# os.rename('file.txt', 'demo.txt')
# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))
# print(os.listdir())

# to search file and show directory tree
# for dir_path, dir_names, file_names in os.walk('C:\Var'):
#     print('Current Path: ', dir_path)
#     print('Directories: ', dir_names)
#     print('Files: ', file_names)

# Access home directory location by grabbing home environment variable
print(os.environ.g) # Returns a path
# To properly join two files together use os.path.join()
# file_path = os.path.join(os.environ.get('Users'), "demo.txt")
# print(file_path)