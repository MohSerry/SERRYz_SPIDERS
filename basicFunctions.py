import os


# Creates a Project File
def createProjectDirectory(fName):
    if not os.path.exists(fName):
        print('Creating Project Folder... ' + fName)
        os.makedirs(fName)


# Create queue and crawled files (if not created)
def createFiles(projectName, baseURL):
    q = os.path.join(projectName, 'queue.txt')
    crawled = os.path.join(projectName,'crawled.txt')
    if not os.path.isfile(q):
        write_file(q, baseURL)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
        f.close()


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass


# Read a file and convert each line to set items
def convert_to_set(fileName):
    result = set()
    with open(fileName, 'rt') as f:
        for ln in f:
            result.add(ln.replace('\n', ''))
    return result


# Iterate through a set, each item will be a line in a file
def convert_to_file(links, fileName):
    with open(fileName,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")
