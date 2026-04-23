# Can't use matrix_env/bin/activate and deactivate as they are shell functions and makefile cannot call on them. Instead we directly call on the file by its path
# I can delete the env but still be seen as inside the env. This is due to activate just setting the VIRTUAL_ENV environmental var or path flag. It isn't actually checking whether we are inside or not. Deactivate erases the flag.

# Checks if there is a venv. If not, make it
env:
	test -d matrix_env || python3 -m venv matrix_env

# Check for packages installed. If not, install them
pip: env
	matrix_env/bin/pip show pandas > /dev/null 2>&1 || matrix_env/bin/pip install -r requirements.txt

# Run file in venv, pip style
rune: pip
	matrix_env/bin/python3 loading.py

# Run file outside of venv
rung:
	/usr/bin/python3 loading.py

# Install poetry if not installed
install_poet: env
	test -f matrix_env/bin/poetry || matrix_env/bin/pip install poetry

# Boot poetry env if not booted
poet: install_poet
	test -f poetry.lock || matrix_env/bin/poetry install

# Run file inside poetry env
runp: poet
	matrix_env/bin/poetry run python3 loading.py

# Double check files that are to be deleted
clean_check:
	find . -type d -name "*matrix*"
	find . -name "*matrix*"
	find . -name "*poetry*"
	find . -name "*.png"

# Delete generated files
cclean:
	find . -type d -name "*matrix*" -exec rm -rf {} +
	find . -name "*matrix*" -delete
	find . -name "*poetry*" -delete
	find . -name "*.png" -delete

.PHONY: cclean pip poet rune rung env clean_check install_poet
