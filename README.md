# task_manager_pet_project
This is my first own FastAPI pet project 


## Project structure:
Main directory with app is app/<br>
---main.py *entrance point*<br>
---api/ *routers*<br>
------auth.py<br>
------tasks.py<br>
---core/ *configuration files*<br>
------config.py<br>
---db/ *work with database*<br>
------session.py *engine and session init*<br>
------models.py *database models*<br>
---schemas/ *pydantic schemas*<br>
------user.py<br>
------task.py<br>
---services/ *CRUD, controllers, logic*<br>
---tests/ *tests*<br>


## Start script
Activate venv, install dependencies 
```
uvicorn app.main:app --reload
```


### Database info:
There are two models for SQLAlchemy. Users and Tasks, connection one-to-many (one user to many tasks). Cascade in users and tasks means delete all tasks when their owner (user) is deleted. <br>
Alembic commands for migrations: <br>
Creating:
```
alembic revision --autogenerate -m "message"
```
Completing:
```
alembic upgrade head
```
