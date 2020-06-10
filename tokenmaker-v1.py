#!/usr/bin/env python3

import hashlib
import sys

# Author: Bardiya Xhorshidi
# https://github.com/xbforce/
# https://twitter.com/xbforce
# licensed under the GNU General Public License v3.0


if __name__ == '__main__':
    # Usage; print if the user doesn't use python3
    if sys.version_info < (3,0,0):
        print("Usage: python3 tokenmaker.py\nThis code requires python3, but you are running python version " + str(sys.version[0]))
        sys.exit(1)

    print('''***********************************************************************
! tokenmaker-v1.py -- Make SHA256 tokens - https://github.com/xbforce/
***********************************************************************
''')

    ask_salt = input(str('Type a salt code: '))
    ask_key = input(str('Add your preferred key: '))
    ask_password = input(str('Type a password: '))


def token_func(user_salt, user_key, user_password):
    """Make SHA256 tokens. First we mix a chosen password with a chosen salt code to create a hash. Then we add a key and mix it with the hash created from the password and the salt to make the final token."""
    user_salt = ask_salt

    user_key = ask_key

    user_password = ask_password

    # Mix the password and the salt code
    pass_salt = hashlib.sha256(user_password.encode() + user_salt.encode()).hexdigest()

    # Make the token by mixing the key and pass_salt
    token_maker = hashlib.sha256(user_key.encode() + pass_salt.encode()).hexdigest()

    # Return the result
    return '\n' + str(user_password) + ' = ' + token_maker

print(token_func('user_salt', 'user_key', 'user_password'))

