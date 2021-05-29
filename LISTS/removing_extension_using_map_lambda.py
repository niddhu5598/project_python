files = ['demo.png','help.exe','sleep.png','work.doc']
print(files)

# normal
cl_files = []
for file in files:
    name = file.split('.')[0]
    cl_files.append(name)

print(cl_files)

# lambda expression
remove_ext = lambda filename: filename.split('.')[0]
clean_files = list(map(remove_ext,files))

print(clean_files)