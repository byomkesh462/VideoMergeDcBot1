import os

class Config(object):
	API_HASH = os.getenv('API_HASH','1d9a53fb735d8548a6dac47dd764f8bc')
	BOT_TOKEN = os.getenv('BOT_TOKEN','5550978601:AAE8Ysf3E5xBm9xN3K8hb80ozS0TJ_6zy1c')
	API_ID = int(os.getenv('API_ID','16388679'))
	OWNER = int(os.environ.get('OWNER','5127754268'))
	OWNER_USERNAME = os.getenv('OWNER_USERNAME','ullastv')
	PASSWORD = os.getenv('PASSWORD','@ullastv')
	DATABASE_URL=os.environ.get("DATABASE_URL","mongodb+srv://erichdaniken:erichdaniken@cluster0.c13qk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
	FLAG = int(os.getenv('FLAG',1))		# Dont Change this(unfinished feature!!) or else bot will stop working
