def save(content,filename):
    with open (filename, 'w') as file:
        file.write(content)

def read_file(filename):
    with open(filename,'r') as file:
        return file.read()