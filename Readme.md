## About

PyTenPass is a non-interactive, read-only, keepass compataible password manager written in Python.



## Installation 

 * Clone this repository.

 `git clone https://github.com/defaultpfp/pytenpass/`

* Install all dependencies.

 ` pip install --requirement requirments.txt`

* Change database name.

`sed -i 's/db.kdbx/DataBaseName.kdbx/g' pypass.py`

Replace Word "DataBaseName" with your database name.


## Usage

* Get password of an entry named "Test". 

`python pykeypass.py  --query Test`

Entry: "Test (FooBar)"

qwerty

* Show help.

` python pykeypass.py --help `
