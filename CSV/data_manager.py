import csv
import shutil
import datetime
import os
from tempfile import NamedTemporaryFile

file_item_path = os.path.join(os.getcwd(),"abc.csv")
def read_data(user_id=None, email=None):
    filename = file_item_path
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