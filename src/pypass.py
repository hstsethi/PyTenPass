import argparse
from pykeepass import PyKeePass
parser = argparse.ArgumentParser()
parser.add_argument("--query", required=True,help="Title of entry which you are looking for.(Case sensitive)")
parser.add_argument("--password", required=True,help="Password for keepass database.")
args = parser.parse_args()
pm = PyKeePass('db.kdbx', password=args.password)       
entry = pm.find_entries(title=args.query,first=True)
print(entry) 
print(entry.password)
