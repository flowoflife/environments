## How to use Git

Noted by Phan Hoang Phuong

2021 Jan 22

### 1. Git setting

```bash
# check git version
git --version
# set user name
git config --global user.name "your name"
# set user email
git config --global user.email "youremail@email.com"
# set default gitignore
vi ~/.gitignore   # fill in files to ignore
ESC :wq!
git config --global core.excludesfile ~/.gitignore
# set git editor
git config --global core.editor vim
git config --list
```

some common commands

```bash
git reset   # remove files from staging area

git add -A /path/to/folder
# add all changed files in folder to staging area
# even in upper folders if they are all tracked by git

# or
git add ~/folder/  # -A is default

# or
git add -u   # add all but not untracked files

# or only at current directory
git add .

# not recommend to use
git add *
```

### 2. Setting Git for local project

```bash
cd /project/folder
git init

# check status
git status

# to remove git tracking, remove .git folder
rm -rf .git

# add files to staging area to commit to repository
git add -A   # or git add .

# to remove a file from staging area
git reset <file-name>

# to commit files from stating area to repository
git commit -m "git commit message"

# push to repository
git pull original master
# if there is no change from master, then push
git push

# to check git log
git log
```

Example to create a new repository on the command line

```bash
echo "# Title" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:account_name/repository_name.git
git push -u origin main
```

or push an existing repository from the command line

```bash
git remote add origin git@github.com:account_name/reposiroty_name.git
git branch -M main
git push -u origin main
```

### 3. Cloning a repository, pushing to master repository

```bash
cd /project/folder
git clone <https://.... git clone URL.git>

# list reposiotory info
git remove -v   # or git branch -a

# create a branch for you to work at local
git branch <your-branch-name>

# change to your branch
git checkout <your-branch-name>

# push to your branch
git pull
git push -u origin <your-branch-name>

# to push to or merge with origin master
git checkout master
git pull origin master
git branch --merged
git merge <your-branch-name>
git push origin master

# remove branch
git branch --merged  # to check your branch
git branch -d <your-branch-name>  # to delete your branch localy

# to delete your branch on remote repository
git branch -a   # to check your branch
git push origin --delete <your-branch-name>
```

### 4. Fixing mistakes

```bash
# fix a file which was wrongly changed/edited
git checkout <file-name>
# check again
git status   # also check file to see all changes were removed

# fix a wrong commit message
git commit --amend -m "new commit message"

# fix a wrong commit to undesired branch
# first, check info
git log
git log --stat
git branch
# to see if we commit to wrong branch
# move a commit to desired branch
git checkout <desired-branch-name>
git cherry-pick <hash of the wrong commit>
# note: cherry-pick just move, not delete the commit

# to remove wrong commit from undesired branch
git checkout <undesired-branch-name>
git reset --soft <hash of the commit>
git log
# you will see --soft cancell the commit
# but did not remove the files on staging area

# use reset default
git reset <hash of the commit>
git log
git status
# now the files are back to local working directory,
# not on staging area

# use reset --hard
git reset --hard <hash of the commit>
git log
git status
# now --hard deleted all of tracked/changed files

# to remove all tracked directory and files
git clean -df  # d = directory, f = file

# to check what we did
git reflog
# it will show all of changes and their hashes

# to get back or recover those changes, just use the hash
git checkout <hash of the change we did>

# the best way is to move all those changes to a backup branch
git branch <backup-branch-name>
# then go back to the master branch
git checkout <master>
git branch
git reflog

# Fix wrong pull/checkout of other members
git revert <hash of the wrong pull>
git log
git diff <hash of the wrong pull> <hash of the reverted pull>

# so git revert will undo all change before git pull by other members
```

### 5. Managing changes using git stash

```bash
# make change and save change using stash
git stash save 'save message: eg, explain what was changed'
# check what was changed
git diff
# get list of stash
git stash list
# want to apply a saved change by stash
git stash apply stash{0}   # it will make change, but not remove stash list
# use pop, it will make change using stash{0}, and drop the stash from list
git stash pop
# remove a stash
git stash drop stash{0}
# remove all stash
git stash clear
```

### 6. Moving change to other branch using git stash

```bash
# make change and save change using stash
git stash save 'save message: eg, explain what was changed'
# checkout other branch
git checkout <other-branch-name>
# apply stash
git stash pop
git add .
git commit -m "commit message"
# return previous branch
git checkout <previous-branch-name>
```

### 7. Setting DiffTool and DiffMerge

ref: https://medium.com/@vitorhsb/how-to-set-diffmerge-as-git-merge-and-diff-tool-unix-40df346c11c4

```bash
# install diffmerge
brew install --cask diffmerge

# setting git config
git config --global merge.tool diffmerge
git config --global mergetool.diffmerge.cmd "/usr/local/bin/diffmerge --merge --result=\"\$MERGED\" \"\$LOCAL\" \"\$BASE\" \"\$REMOTE\""
git config --global mergetool.diffmerge.trustExitCode true
git config --global mergetool.keepBackup false
git config --global diff.tool diffmerge
git config --global difftool.diffmerge.cmd "/usr/local/bin/diffmerge --nosplash \"\$LOCAL\" \"\$REMOTE\""

# check config
git config --global --list

# use difftool to fix confict between files
git difftool

# use diffmerge to fix conflict between branches
git diffmerge
```
