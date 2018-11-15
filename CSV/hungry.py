import csv
import shutil
import datetime
from tempfile import NamedTemporaryFile


def read_data(user_id=None, email=None):
    filename = "data.csv"
    with open(filename, "r", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        items =[]
        unknown_user_id = None
        unknown_email = None
        for row in reader:
            if user_id is not None:
                if int(user_id) == int(row.get("id")):
                    return row
                else:
                    unknown_user_id = user_id
            if email is not None:
                if email == row.get("email"):
                    return row
                else:
                    unknown_email = email
        if unknown_user_id is not None:
            return "User ID {user_id} not found".format(user_id=user_id)
        if unknown_email is not None:
            return "User Email {email} not found".format(email=email)
    return None


def get_length(file_path):
    with open("data.csv") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

def append_data(file_path, name, email):
    fieldnames=['id', 'name', 'email']
    next_id = get_length(file_path)
    with open("data.csv", "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({"id": next_id, "name": name, "email": email})

append_data("data.csv","Tahir","tahirs95@hotmail.com")

filename = "data.csv"
temp_file = NamedTemporaryFile(mode='w', delete=False)
with open(filename, "rt",newline='') as csvfile, temp_file:
    reader = csv.DictReader(csvfile)
    fieldnames=['id', 'name', 'email','amount','sent']
    writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
    writer.writeheader()
    print(temp_file.name)
    for row in reader:
        if int(row['id'])== 4:
            row['sent']=True
            print(row)
        writer.writerow(row)
        # writer.writerow({
        #     "id":row["id"],
        #     "name":row['name'],
        #     "email":row['email'],
        #     "amount":1234,
        #     "sent":''
        # })
    shutil.move(temp_file.name, filename)
