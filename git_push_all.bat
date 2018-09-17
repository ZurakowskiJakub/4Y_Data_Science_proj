@ECHO OFF

set /p message="Commit message: "

git add .
git commit -m "%message%""
git push