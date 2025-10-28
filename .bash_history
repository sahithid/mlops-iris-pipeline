source .env/bin/activate
git init
eval "$(ssh-agent -s)"
ssh-add ssh_key
cd w2_w4Integrated/
git add requirements.txt
git checkout dev
git commit -m "modified requirements.txt"
git push origin dev
git add requirements.txt
git commit -m "modified requirements.txt"
git push origin dev
cd ..
git add w2_w4Integrated
git commit -m "Week 4 Integrated"
git push origin dev
git status
git checkout -b dev2
git add w2_w4Integrated
git add week3
git commit -m "Added week3 and Week4 Integrated folder"
git push origin dev2
git checkout main
git checkout -b dev3
git commit
git push origin dev3
git checkout -b week2
git branch
git checkout week2
git status
git commit -m "week1 and week2 contents"
git push origin week2
git checkout branch dev3
git checkout dev3
git checkout -b week3
git push origin week3
git rm -r artifacts
git rm -r outputs
git rm -r w1_w2
git rm --cached w1_w2
git rm -r --cached w1_w2
git commit -m "clean up week3 branch, delete week2 contents"
git push origin week3
git checkout week2
git checkout dev3
git stash
git checkout dev3
git branch
git stash -u
git status
git clean -n
git checkout main
git branch -d week3
git checkout -b temp-branch
git checkout main
git branch -D week3
git push origin --delete week3
git checkout week2
git add 
git checkout -f main
git checkout dev3
git stattus
git status
git branch -D dev2
git branch -D dev3
git checkout main
git branch -D dev3
git push origin --delete dev2
git push origin --delete dev3
git checkout week2
git rm -r artifacts
git rm -r outputs
git commit -m "Clean up week2"
git push origin week2
git checkout dev
dvc pull
dvc pull data.dvc -v
python test.py
ls
cd w1_w2/
ls
python test.py
dvc pull data.dvc -v
cd ..
git reset --hard origin/main
git clean -n
git clean -f
git status
git checkout week2
git checkout -b week4
dvc status
dvc pull data.dvc
git commit -m "week4 branched out from week2"
ssh-add ssh_key
git config --global user.email "dmsahithi@gmail.com"
git config --global user.name "sahithid"
git commit -m "week4 branched out from week2"
git clean -fd
git commit -m "week4 branched out from week2"
git reset --hard origin/dev
git checkout dev
git pull
python test.py
deactivate
python3 -m venv .env
source .env/bin/activate
git init
git branch
python test.py
pip install dvc
pip install -r requirements.txt 
dvc status
python train_w2.py
cd week4
python train_w2.py
dvc add week4/artifacts/model_v1/w4_model.joblib
dvc add artifacts/model_v1/w4_model.joblib
dvc push
pip install dvc-gs
dvc push
cd ..
git reset --hard
ls
rm -r artifacts
rm -r data
rm -r outputs
ls
git add .
git status
git add week4
git commit -m "added week4 contents"
git config --global user.email "dmsahithi@gmail.com"
gitt config --global user.name "sahithid"
git config --global user.name "sahithid"
git commit -m "added week4 contents"
git push origin dev
git rm -r --cached outputs
git rm -r --cached artifacts
git rm -r --cached data
git commit -m "Remove old_folder from Git tracking"
git push origin dev
git push origin dev --force
git rm -r --cached train_week2.ipynb
git rm -r --cached train_w2.py 
git rm -r --cached iris_classifier.ipynb 
git rm -r --cached requirements.txt 
git rm -r --cached test.py 
git rm -r --cached terminal_commands.txt 
git commit -m "Remove old_files from Git tracking"
git push origin dev --force
cd week4
ls
s artifacts/model_v1/w4_model.joblib.dvc artifacts/model_v1/.gitignore
cd ..
python week4/train_w2.py
python week4/train_w2.py
dvc add week4/artifacts/model_v1/w4_model.joblib
git add week4/artifacts/model_v1/w4_model.joblib.dvc
dvc add week4/outputs/v1/predictions.csv
dvc push
git commit -m "run train"
git push origin dev
python week4/test.py
week4/outputs/v1/predictions.csv
python week4/test.py
git add .
git status
git rm --cached .env
git rm -r --cached .env
nano .gitignore
git add .gitignore
git commit -m "Add .env to .gitignore and stop tracking it"
git push origin dev
git status
git add .
git log
.env/bin/activate
source .env/bin/activate
git checkout dev
dev add .
git add .
git commit
git commit -m  "changes"
git push origin dev
git git config --global user.name "sahithid"
git config --global user.name "sahithid"
git config --global user.email "dmsahithi@gmail.com"
git push origin dev
ssh -T git@github.com
git remote -v
git remote set-url origin https://github.com/sahithid/mlops-iris-pipeline.git
git push origin dev
python week4/test.py
git init
source .env/bin/activate
git pull dev
git init
git checkout dev
dev checkout main
git checkout main
git rm --cached $(find . -name "*.env")
git rm -r --cached $(find . -name "*.env")
nano .gitignore
git add .
git commit -m "remove .env files and add gitignore"
git push origin main
git pull origin main
git -rm .gitconfig
git -r .gitconfig
git rm .gitcongif
git rm .gitconfig
git stash
    rm .gitconfig
git pull origin main
git config --global user.email “dmsahithi@gmail.com”
 git config --global user.name “sahithid”
git pull origin main
git add *
git stash
git pull
git add -A
git stash
git pull
git add
git add .
git commit -m 'changes'
git push origin  main
    git push --force-with-lease origin main
git checkout dev
git pull dev
clear
git checkout  main
git commit  -m "changes"
git commit -a
git add .
git commit -m "changes"
git psh origin dev
git push origin dev
git checkout main
git merge dev
git config --global user.email “dmsahithi@gmail.com”
git config --global user.name “sahithid”
git merge dev
git rm .gitconfig
git rm gitconfig
nano .gitignore
git rm gitconfig
mv .gitconfig /
nano .gitconfig
nano .gitignore
git add .gitignore
    git commit -m "Stop tracking .gitconfig and add it to .gitignore"
git push origin main
git merge dev
clear
git checkout dev
git add .
git commit -m "cloud file"
git  push origin main
git checkout dev
python train_w2.py
python week4/train_w2.py
dvc add week4/artifacts/model_v1/w4_model.joblib
git add week4/artifacts/model_v1/w4_model.joblib.dvc
git commit -m "trained model added"
git push origin dev
dvc push
python test.py
python week4/test.py
git add .
git commit -m "after test"
git push origin dev
nano .gitignore
git add .
git commit -m  "add gitignore"
git prune
git commit -m  "add gitignore and prune"
git push origin dev
git pull origin dev
git merge dev
git push origin dev
git checkout main
nano .gitignore
git pull main
git pull origin  main
git merge  main
git merge dev
eval $(ssh-agent -s)
ls -al ~/.sshls -al ~/.ssh
ls -al ~/.ssh
ssh-keygen -t ed25519 -C "dmsahithi@gmail.com"
ssh-add key
git branch
git merge dev
git config --global user.email "dmsahithi@gmail.com"
git config --global user.name "sahithid"
git merge dev
git add .
git commit -m "update gitignore"
nano .gitignore
git add .
git commit -m "update gitignore"
git push origin main
git add .
git commit -m "update gitignore"
git push origin main
git rm key
git commit --amend
git push
git commit --amend --all
git push
git push
git push
git merge dev
git checkout dev
git checkout -b main
git checkout -b main2
git add .
git commit -m "Creating Main"
git push origin main2
source .env/bin/activate
git init
gi branch
git branch
git checkout dev
git checkout -b week5
git branch
git push -u origin week5
git log
git push -u origin week5
git add .
git commit -m "clean up"
touch .gitignore
nano .gitignore
ls
touch .dvcignore
nano .dvcignore
git add .
git commit -m "Update gitignore, add dvcignore"
git rm -r --cached .
git add .
git commit -m "clean  up"
git push -u origin week5
git stats
git status
exit
