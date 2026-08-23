# Assignment1_HV
HV first assignment task
Created a Python flask application which runs on the server and shows the output welcome to the app on accessing the url - http://127.0.0.1:5000/ - which is home
<img width="636" height="206" alt="image" src="https://github.com/user-attachments/assets/a33d4cf7-de11-42d1-9245-a03d491debc1" />
And shows "App is running" while accessing the url - http://127.0.0.1:5000/health - which calls the function health and returns the output
<img width="632" height="206" alt="image" src="https://github.com/user-attachments/assets/e0e57d23-8aaa-4622-ba29-e04d1ff2391d" />
This first version of the application is pushed to online repositoy Assignment1_HV by the following commands
git init - initialising the local repository
git add . - adding the file tothe local repo
git commit -m "Assignment 1, Task 1" - Commits to local repo
git switch -c dev - creates a branch dev
git branch - shows 2 branches main and dev
git remote add origin https://github.com/06Poornima03/Assignment1_HV/ - connecting to online repo
git commit -m "Merge dev to main" - commiting to merge
git switch main - switching back to main
git merge dev - Merging to dev
git push -u origin main - pushing to online repo
Version 2
Created enhancement codes to flask application for voting system
added code for /vote/<name> where name is a variable, when a name is given in the url the function will add it, if its not new, otherwise will create a vote, the url which is accessed is - http://127.0.0.1:5000/vote/Tom - 
<img width="643" height="203" alt="image" src="https://github.com/user-attachments/assets/fba426aa-6e96-416a-9381-4788c401a0af" />
<img width="636" height="209" alt="image" src="https://github.com/user-attachments/assets/93d1c611-080d-4497-aebb-6a4bfd30296c" />
<img width="637" height="203" alt="image" src="https://github.com/user-attachments/assets/f7f031b1-f480-44be-bdd4-b24304b9fb74" />
Results function will give the count of votes (which is dictionary) of voters by jsonify default function in flask with the url - http://127.0.0.1:5000/results
<img width="638" height="206" alt="image" src="https://github.com/user-attachments/assets/899987c2-75db-421d-ba6d-b719ff0bedb6" />
Reset function will clear all the votes and shows a success message, which is accessed by the url - http://127.0.0.1:5000/reset
<img width="638" height="206" alt="image" src="https://github.com/user-attachments/assets/bfda77db-e671-476d-98d4-eec3c4b3c56a" />
<img width="636" height="200" alt="image" src="https://github.com/user-attachments/assets/f510d74c-831d-47ed-95a7-cf3a1c2cf4e7" />
Again following the same git commands to push the changes as version 2 in same repo






