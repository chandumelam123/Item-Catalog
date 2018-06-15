from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, drop_database, create_database

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
user1 = User(name="Rahul Chandra", email="rahulchandra94944@gmail.com",
             picture='https://www.google.co.in/search?q=nature&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiJ5IzHnNPbAhUMo48KHTyiDboQ_AUICigB&biw=1536&bih=798&dpr=1.25#')
session.add(user1)
session.commit()

# Items for Strings
category1 = Category(name="party games", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Conversation games", user_id=1, description="Conversation games are games that require only conversational ability. Conversation games owe their popularity to their ability to be played almost anywhere with almost anyone and for their ability to generate conversation. Their popularity has gained in part due to the hip hop culture and TV shows like Wild 'N Out and Yo Momma. Below are some good ideas to kill time between two or more people.", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Drinking games", user_id=1,  description="Drinking games are games which involve the consumption of alcoholic beverages. Evidence of the existence of drinking games dates back to antiquity. Drinking games have been banned at some institutions, particularly colleges and universities", category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Guesssing games", user_id=1, description="A guessing game is a game in which the object is to use guessing to discover some kind of information, such as a word, a phrase, a title, or the identity or location of an object.[20] A guessing game has as its core a piece of information that one player knows, and the object is to coerce others into guessing that piece of information without actually divulging it in text or spoken word. Charades is probably the most well-known game of this type, and has spawned numerous commercial variants that involve differing rules on the type of communication to be given, such as Catch Phrase, Taboo, Pictionary, and similar. The genre also includes many game shows such as Win, Lose or Draw, Password and $25,000 Pyramid.", category=category1)

session.add(item3)
session.commit()

# Items for Woodwinds
category2 = Category(name="Tabletop games", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="Board game", user_id=1, description="A board game is a tabletop game that involves counters or pieces moved or placed on a pre-marked surface or board, according to a set of rules. Some games are based on pure strategy, but many contain an element of chance; and some are purely chance, with no element of skill.", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="card games", user_id=1,  description="A card game is any game using playing cards as the primary device with which the game is played, be they traditional or game-specific. Countless card games exist, including families of related games (such as poker). A small number of card games played with traditional decks have formally standardized rules, but most are folk games whose rules vary by region, culture, and person.", category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Miniature games", user_id=1, description="Miniature wargaming is a form of wargaming which incorporates miniature figures, miniature armor and modeled terrain as the main components of play and which was first invented at the beginning of the 19th century in Prussia. Like other types of wargames, they can be generally considered to be a type of simulation game, generally about tactical combat, as opposed to computer and board wargames which have greater variety in scale.", category=category2)

session.add(item3)
session.commit()

# Items for Percussion
category3 = Category(name="Video game", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="arcade game", user_id=1, description="An arcade game or coin-op is a coin-operated entertainment machine typically installed in public businesses such as restaurants, bars and amusement arcades. Most arcade games are video games, pinball machines, electro-mechanical games, redemption games or merchandisers. While exact dates are debated, the golden age of arcade video games is usually defined as a period beginning sometime in the late 1970s and ending sometime in the mid-1980s. Excluding a brief resurgence in the early 1990s, the arcade industry subsequently declined in the Western hemisphere as competing home video game consoles such as the Sony PlayStation and Microsoft Xbox increased in their graphics and game-play capability and decreased in cost.", category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="computer game", user_id=1, description="An arcade game or coin-op is a coin-operated entertainment machine typically installed in public businesses such as restaurants, bars and amusement arcades. Most arcade games are video games, pinball machines, electro-mechanical games, redemption games or merchandisers. While exact dates are debated, the golden age of arcade video games is usually defined as a period beginning sometime in the late 1970s and ending sometime in the mid-1980s. Excluding a brief resurgence in the early 1990s, the arcade industry subsequently declined in the Western hemisphere as competing home video game consoles such as the Sony PlayStation and Microsoft Xbox increased in their graphics and game-play capability and decreased in cost.", category=category3)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Console games", user_id=1, description="The game consists of manipulable images (and usually sounds) generated by a video game console and displayed on a television or similar audio-video system. The game itself is usually controlled and manipulated using a handheld device connected to the console, called a controller. The controller generally contains a number of buttons and directional controls, (such as analogue joysticks), each of which has been assigned a purpose for interacting with and controlling the images on the screen. The display, speakers, console, and controls of a console can also be incorporated into one small object known as a handheld game.", category=category3)

session.add(item3)
session.commit()

# Items for Brass
category4 = Category(name="genre", user_id=1)

session.add(category4)
session.commit()


categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name