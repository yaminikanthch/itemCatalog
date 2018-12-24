from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

# Create database and create a shortcut for easier to updation of  database
engine = create_engine('sqlite:///catalogs.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Creating dummy user
User1 = User(name="First Hero", email="yaminikanthch@gmail.com")
session.add(User1)
session.commit()

# Creating category of Action Films
category1 = Categories(user_id=1, name="Action Films")
session.add(category1)
session.commit()


# Creating a Category For Adventure Films
category2 = Categories(user_id=1, name="Adventure Films")
session.add(category2)
session.commit()

# Creating a Category For Comedy Films
category3 = Categories(user_id=1, name="Comedy Films")
session.add(category3)
session.commit()

#Creating a Category For  Crime Films
category4 = Categories(user_id=1, name="Crime Films")
session.add(category4)
session.commit()

#Creating a Category For  Drama Films
category5 = Categories(user_id=1, name="Drama Films")
session.add(category5)
session.commit()

# Creating a Category For Epics/Historical Films
category6 = Categories(user_id=1, name="Epics/Historical Films")
session.add(category6)
session.commit()

#Creating a Category For Horror Films
category7 = Categories(user_id=1, name="Horror Films")
session.add(category7)
session.commit()

#Creating a Category For Musicals (Dance) Films
category8 = Categories(user_id=1, name="Musicals (Dance) Films")
session.add(category8)
session.commit()

#Creating a Category For Science Fiction Films
category9 = Categories(user_id=1, name="Science Fiction Films")
session.add(category9)
session.commit()

#Creating a Category For War (Anti-War) Films
category10 = Categories(user_id=1, name="War (Anti-War) Films")
session.add(category10)
session.commit()

#Creating a Category For Westerns
category11 = Categories(user_id=1, name="Westerns")
session.add(category11)
session.commit()


# Add Items into categories
categoryItem1 = CategoryItem(user_id=1, name="Ek Tha Tiger",
                             description="An Action Film",
                             categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="PARI",
                             description="A Horror Film",
                             categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Veer",
                             description="It is a war based film",
                             categories=category10)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Gazi Attack",
                             description="It is a war based film",
                             categories=category10)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Raazi",
                             description="It is a crime film ",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="3 Idiots",
                             description="Is a comedy  film",
                             categories=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Aashiqi",
                             description="It is a music film ",
                             categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Conquering The Demons",
                             description="It is a western movie",
                             categories=category11)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Danagal ",
                             description="Its a drama movie",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Bahubali ",
                             description="It is a hisotoric movie ",
                             categories=category6)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Krish ",
                             description="It is science fiction movie",
                             categories=category9)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Dhoom",
                             description="An action movie",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Drishyam",
                             description="Crime movie ",
                             categories=category4)
session.add(categoryItem1)
session.commit()
categoryItem1 = CategoryItem(user_id=1, name="It",
                             description="A horror movie",
                             categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Demons Strike Back",
                             description="Is a western movie",
                             categories=category11)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Karwaan",
                             description="It is a drama ",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Love ",
                             description="Its a romantic film",
                             categories=category6)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Star Wars",
                             description="A science fiction movie ",
                             categories=category9)
session.add(categoryItem1)
session.commit()
categoryItem1 = CategoryItem(user_id=1, name="Avtaar",
                             description="A science fiction movie ",
                             categories=category9)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Kick",
                             description="An action movie",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,
                             name="Dark Kingdom",
                             description="An adventerous film",
                             categories=category2)
session.add(categoryItem1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="MummaBhai MBBS",
                             description="A comedy movie ",
                             categories=category3)
session.add(categoryItem1)
session.commit()
categoryItem1 = CategoryItem(user_id=1, name="Lageraho MummaBhai ",
                             description="A comedy movie ",
                             categories=category3)
session.add(categoryItem1)
session.commit()
categoryItem1 = CategoryItem(user_id=1, name="PK",
                             description="A comedy movie ",
                             categories=category3)
session.add(categoryItem1)
session.commit()

print "added category items!"
