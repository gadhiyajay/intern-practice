import shutil
src = '/home/trootech/Jay_Intern/Python_Excerise/poem.txt'
dest = '/home/trootech/Jay_Intern/Python_Excerise/new.txt'

output = shutil.copy(src, dest)

print(output)