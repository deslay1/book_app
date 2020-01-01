
Live through Heroku: https://djangobookmarket.herokuapp.com/
Note: Currently there is a problem with loading any images on the site. The images are uploaded to an AWS-S3 bucket, which works fine, but the images do not load due to a signature-related problem that hopefully will be fixed asap.

# Git commands!

Begin developing by cloning this repository:

- Entered desired directory to clone into, then:
  `git clone <url>`

## Adding important .gitignore file!

- Create file named .gitignore in book_app repo locally
- Add on seperate lines: **/vscode/\*** and **\*.pyc**
- Feel free to add more files/directories git should ignore

## Steps to add/push changes:

Adding to stagin area:

```
- git checkout branch (to see what branch you're on)
- git add . or git add -A
```

To revert added files from staging area, do **git reset**

Commiting and pushing to remote repo:

```
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

## Going back to a commit

```
- git reset --hard <commit hash (from github)>
```

## Deleting.pyc files from repo:

From powershell:

- type: **cmd**
- run: del /S \*.pyc
- **exit** to go back
