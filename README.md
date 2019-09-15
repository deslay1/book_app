# Git commands!

Begin developing by cloning this repository:
- Entered desired directory to clone into, then:
``` git clone <url> ```

## Adding important .gitignore file!
- Create file named .gitignore in book_app repo locally
- Add on seperate lines: **/vscode/*** and ***.pyc** 
- Feel free to add more files/directories git should ignore


## Steps to add/push changes:

Adding to stagin area:
```
<<<<<<< HEAD
- git checkout branch (to see what branch you're on)
- git add . or git add -A
```
To revert added files from staging area, do **git reset**

Commiting and pushing to remote repo:
```
=======
- git checkout branch (to see what branch SellerOrBuyeru're on)
- git add .
>>>>>>> tobi
- git commit -m "message"
- git push
```


## Switching branches:
```
- git add, commit to save changes
- git checkout "branch"
```


## Creating a new branch:
```
- git branch "new_branch"
- git checkout "branch"
```


## Steps to merge with another branch:
```
- git pull (to download remote updates)
- git add, commit to save changes
- git merge "branch"
```
**Solve eventual conflicts by opening important unstaged files (files that are not associated with the database or end with .pyc)**

Deleting.pyc files from repo:
From powershell:
- type: **cmd**
- run: del /S *.pyc
- **exit** to go back
