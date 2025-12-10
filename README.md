# task_manager_pet_project
This is my first own FastAPI pet project 


## Project structure:
Main directory with app is app/
---main.py *entrance point*
---api/ *routers*
------auth.py
------tasks.py
---core/ *configuration files*
------config.py
---db/ *work with database*
------session.py *engine and session init*
------models.py *database models*
---schemas/ *pydantic schemas*
------user.py
------task.py
---services/ *CRUD, controllers, logic*
---tests/ *tests*


## Start script
Activate venv, install dependencies 
```
python main.py
```
