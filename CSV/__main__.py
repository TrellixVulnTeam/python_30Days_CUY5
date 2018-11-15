from argparse import ArgumentParser
from data_manager import read_data
from templates import get_template, render_context
from data_class import UserManager

parser = ArgumentParser(prog="hungry")
parser.add_argument('--user_id', '-id', type=int)
parser.add_argument('-e', '--email', type=str)
args = parser.parse_args()
# print(args)
# print(args.user_id)
# print(read_data(user_id=args.user_id))
# print(read_data(email=args.email))
#print(UserManager().get_user_data(user_id=args.user_id, email=args.email))
print(UserManager().message_user(user_id=args.user_id, email=args.email))