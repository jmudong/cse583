## Introduction
Level 1 was just two git commits on a main branch, and Level 2 was just creating and switching to a new branch named bugFix.

In Level 3, I made a commit on both bugFix and main, and merged the two branches. 

In Level 4 was the same as Level 3, but instead of merging I had to switch to the bugFix branch and rebase onto main.

## Ramping Up
Level 1 is just detaching the HEAD to the commit C4, and Level 2 was the same but using the relative ref "^" instead of referencing the commit hash itself.

Level 3 was using refs to move around the main and bugFix branches, as well as HEAD, to other commits. To move main, I had to directly reference the C6 commit hash, as C6 was the most recent commit in our tree. Then, I moved HEAD up to C1 by using "^", then moved bugFix to C0 by referencing "HEAD^".

In Level 4, I used git reset HEAD^ on the local branch since it was just a local repository. Then I switched to the pushed branch, and used git revert HEAD in order to create a commit that saves the revert change. 

## Push & Pull
Level 1 is just a git clone of a remote repository so that we get a local repository. In Level 2, we commit from our local repository, and use a detached HEAD to make another git commit.

Level 3 and Level 4 are just a git fetch and git pull command. In Level 5, I created 2 commits on the remote repository and 1 commit on the local repository, and used git pull to save the changes from the remote onto my local. Level 6 was just two git commits and a git push.

In Level 7, I used git pull --rebase to save the changes from the remote onto my local, and then used git push to save changes from my local to the remote. 

In Level 8, I had to move my local main back in sync with origin/main, and created a branch called feature direclty on C2 and used git push to push it onto the remote. 