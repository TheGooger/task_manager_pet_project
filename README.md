# task_manager_pet_project
This is my first own FastAPI pet project 


## Project structure:
Main directory with app is app/<br>
---main.py *entrance point*<br>
---api/ *routers and deps*<br>
---core/ *configuration (db) and security (auth) files*<br>
---db/ *db models, engine/session init, data processing*<br>
---schemas/ *pydantic schemas*<br>
---services/ *CRUD*<br>
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
