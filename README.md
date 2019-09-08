# Git processes:

## Switching branches:
```
- git add, commit to save changes
- git checkout <branch>
```


## Steps to add/push changes:
```
- git checkout branch (to see what branch you're on)
- git add .
- git commit -m "message"
- git push
```

## Steps to merge with another branch:
```
- git pull (to download remote updates)
- git add, commit to save changes
- git merge <branch>
```
**Solve eventual conflicts by opening important unstaged files (files that are not associated with the database or end with .pyc)**




<!--
%% not done %%
git fetch: updates without making changes on the remote tracking branch.
git merge: merge the remote tracking branch to local branch.
git pull: git fetch + git merge !!!!
-->
