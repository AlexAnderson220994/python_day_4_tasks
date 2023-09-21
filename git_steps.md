# Steps to use *Git* & *GitHub*

## Initialising

- Make sure you're signed in on first use with `git config --global user.email "you@example.com"`.
- *use arrows to navigate in the terminal*.

1) `git status`- use often (shows where you are).
2) `pwd` - print working directory - shows current directory.
2) `ls` - shows folders within current directory.
3) `cd (name)` - change directory to one of the folders shown in `ls`.
4) `cd .` - change to current directory.
5) `cd ..` - change to previous directory (one step back).

## Adding
- Avoid making a repository within a repository.
1) `git init` - initialises an empty Git repository within the working directory.
2) `git add .` - adds all folders to the Git repository (if you include ".").
3) `.gitignore` - open up a new file called ".gitignore" then do ./"folder name" to include folders to be ignored by Git.

## Committing
- Do a `git status` first to check what's going on.
1) `git commit -m "add comment"` - Does a git commit (be sure to add a short comment detailing what the commit is for).

## Pushing
- To push to **GitHub**.
- It will require you to sign into your **GitHub** account on first use.
- Make a new repository on **GitHub** first.
- `Your Profile` - `Respositories` - `New`
- There are instructions on **GitHub**.

![New Repository.jpg](..%2F..%2F..%2FOneDrive%20-%20Sparta%20Global%2FPictures%2FGitHub%20Screenshots%2FNew%20Repository.jpg)

1) `git remote add origin (URL to GitHub Repository)` - Step 1
2) `git branch -M main` - Step 2
3) `git push -u origin main`- Step 3

## Difference between *Git* and *GitHub*


### Diagram showing differences between **Centralise** and **Distributed**
![differences.jpg](..%2F..%2F..%2FOneDrive%20-%20Sparta%20Global%2FPictures%2FGitHub%20Screenshots%2Fdifferences.jpg)

