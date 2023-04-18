@echo off

title Pushing to Github
echo Getting Ready...
F:\
cd Coding\"calculator"
git add *
git commit -m "commit made by Elijah through .BAT"
git branch -M main
git remote add origin https://github.com/ElijahPartney/Calculator.git
cls
git push -u origin main
powershell -Command "& {Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show('Push Completed', 'Finished!', 'OK', [System.Windows.Forms.MessageBoxIcon]::Information);}"
cls