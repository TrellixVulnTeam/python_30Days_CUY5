import os

def template(path):
    file_path = os.path.join(os.getcwd(),path)
    return open(file_path).read()

file_ = "templates/abc.txt"
text = template(file_).format(name="Tahir", date="abc", total=900)
print(text)