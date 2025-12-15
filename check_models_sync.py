from sqlalchemy import select
from sqlalchemy.engine import Result

from app.db.models import Base, Tasks, Users
from app.db.session import engine

from app.db.session import SessionLocal


def main():
    print("Creating tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # with SessionLocal() as session:
    #     user_1: Users = Users(email="example@mail.com", password_hash = "hash")
    #     user_2: Users = Users(email="example_1@mail.com", password_hash = "hash_1")
    #     session.add(user_1)
    #     session.add(user_2)
    #     session.commit()

    #     get_user_1: Result = session.get(Users, 1)
    #     print(get_user_1.email)

    #     stmt = select(Users).order_by(Users.id)
    #     users: Result = session.execute(statement=stmt).scalars()
    #     for user in users:
    #         print(f"Email: {user.email}, created at: {user.created_at}")

    
    # Base.metadata.drop_all(bind=engine)


    print("Done.")


if __name__ == "__main__":
    main()
