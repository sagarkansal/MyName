import os
path = '/home/sagar/Documents/MyName/files'
files = os.listdir(path)
i = 0

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.js'))
    i = i+1
