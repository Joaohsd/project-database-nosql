# Installing python module in order to create new python environment
pip install virtualenv

# Creating new environment based on argument passed to this script
python3 -m virtualenv env

# Activate the Virtual Environment
source env/bin/activate

# Install required dependencies for this Environment
pip install -r scripts/packages.txt

# Saving info about versions of installed packages
pip freeze > scripts/requirements.txt