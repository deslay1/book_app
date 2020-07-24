# Information about virtual environments

## Setup
Use the following command to create a virtual environment in your root/main directory:

**Note that you can choose which desired installed python version to use instead of python3 below**
```
python3 -m venv <name of virtual env>
```
To be able to use the **django-heroku** module you **need** python 3.6 or lower in the virtual environment. 

## Activate the virtual environment
```
source <name of virtual env>/bin/activate
```
Now you should see the name of your virtual environment in the terminal and on the bottom menu in editors such as VSCode.

## Installing necessary packages
Now you can install the pip packages in the repository to use them in the virtual environment. Run the following:
```
pip install -r requirements.txt
```
Note that subsequently running the command ```pip freeze > requirements.txt``` will add the packages you added in the **virtual environment**, which is the entire point here :).

## Important notes
If you decide not to use python 3.6 for certain modules to work such as "django-heroku" then use the ```pip freeze``` command to create another requirements file instead with your own preferred packages so that you won't have to correct the requirements.txt file in the master branch.
For example, you can do ```pip freeze > requirements_3_7.txt``` to indicate that you are using python 3.7.
