# Git commands!

Begin developing by cloning this repository:

- Entered desired directory to clone into, then:
  `git clone <url>`


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

## Creating a new branch:

```
- git checkout -b "new branch name"
```

## Switching branches:
```
- git add, commit to save changes
- git checkout "branch"
```

## Steps to merge with another branch:

```
- git pull (to download remote updates)
- git add, commit to save changes
- git merge "branch"
```

**Solve eventual conflicts by opening important unstaged files (files that are not associated with the database or end with .pyc)**

## Deleting branch:
### Deleting locally:
```
- git branch -d "branch name"
```
or to force delete if branch has not been commited and pushed:
```
- git -D "branch name"
```
### Deleting remotely (github):
```
- git push origin --delete "branch name"
```

## Going back to a commit

```
- git reset --hard <commit hash (from github)>
```

## Deleting.pyc files from repo:

From powershell:

- type: **cmd**
- run: del /S \*.pyc
- **exit** to go back
