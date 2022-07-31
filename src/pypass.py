#    PyTenPass A non-interactive  read only Keepass compataible password manager.
#    Copyright 2022 DefaultPFP

#    PyTenPass is free software: you can redistribute it and/or
#    modify it under the terms of the GNU General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or (at
#    your option) any later version.
#
#    PyTenPass is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
#    Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with the PyTenPass.  If not, see <http://www.gnu.org/licenses/>.

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
