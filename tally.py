import time
from database import DataBaseInterface

db = DataBaseInterface("config.txt")
db.StartServer()

db.SomethingElse();
time.sleep(20)

db.StopServer()
