Combiner : merge, rebase
Annuler : reset, revert

# git merge

Combine 2 branches en créant un commit avec 2 parents.

# git rebase

Combine 2 branches en recopiant des commits en bout de branche.

```
          A---B---C topic *
         /
    D---E---F---G master

git rebase master
# or
git rebase master topic

                  A'--B'--C' topic *
                 /
    D---E---F---G master
```
https://git-scm.com/docs/git-rebase

# git pull

When current branch behind remote : fast forward by default

# git reset

Undo last commit putting everything back into the staging area:
```
git reset --soft HEAD^
```

# HEAD^ HEAD~\<num\>

Remonte d'un commit ^ ou plusieurs ~3 commits.

# git branch -f \<commit\>

Force une branche a se replacer à un commit.

# git checkout -b \<new branch\>

Créé et checkout en même temps

# git reset

Annule des changements en déplaçant la branche au commit parent (local).

# git revert

Annule des changements en créant un nouveau commit incluant l'annulation (remote).

# git restore --staged \<file\>

Unstage file

# git status --ignored

Show ignored files

# git rm -r --cached .

Remove all files from git index
Need to commit after

# git log --graph --oneline --all

Show tree

# git stash --include-untracked

Stash including untracked files

# git stash pop

Unstash

# git rebase -i \<commit or branch\>

Permet de choisir les commits a ignorer et les réordonner

# git cherry-pick \<commit\>

Choisi des commits (d'autres branches) à ajouter a la branche courante

# git commit --amend


****
https://learngitbranching.js.org/

