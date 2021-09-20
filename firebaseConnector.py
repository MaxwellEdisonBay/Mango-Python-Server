import pyrebase
import uuid
import random


class Firebase:

    def __init__(self):
        self.firebaseConfig = {"apiKey": "AIzaSyAEWZS9ue3Dc066D7wZf5auYVuBCqVMUB0",
                               "authDomain": "mango-a3686.firebaseapp.com",
                               "databaseURL": "https://mango-a3686-default-rtdb.europe-west1.firebasedatabase.app",
                               "projectId": "mango-a3686",
                               "storageBucket": "mango-a3686.appspot.com",
                               "messagingSenderId": "199539274648",
                               "appId": "1:199539274648:web:98dd00665e295c760b71ed",
                               "measurementId": "G-741MXML50Y"}
        self.db = None

    def initDB(self):
        firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.db = firebase.database()

    def fetchUserData(self, userID):
        return dict(self.db.child("users").child(userID).get().val())

    def createDummyProfiles(self, number):
        for i in range(number):
            age = random.randrange(18,50)
            sex = random.choice(["male", "female", "dont say","other"])
            location = random.choice(["Prague", "London", "Moscow", "Kiev","Vienna", "Berlin"])
            data = {"name":f"test_name{number}", "sirname":f"test_sirname{number}", "age":age, "sex":sex,
                    "image_ulr":["img1","img2","img3"], "bio":f"test_bio{number}: blablablablabla", "location":location, "interest_tags":["tag1","tag2","tag3"]}
            self.db.child("test_users").push(data)

    def removeDummyProfilesAll(self):
        self.db.child("test_users").remove()

if __name__ == "__main__":
    fireBase = Firebase()
    fireBase.initDB()
    # fireBase.removeDummyProfilesAll()
    fireBase.createDummyProfiles(10)
    # print(fireBase.fetchUserData("7NhwiPqbkrY3cWingePesqFdfBn1"))
