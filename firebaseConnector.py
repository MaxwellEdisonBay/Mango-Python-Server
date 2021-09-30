import pyrebase
import uuid
import json
import random


def import_db_settings(path):
    with open(path) as json_file:
        data = json.load(json_file)
        return data


class Firebase:

    def __init__(self, path='dbConfig.json', user_create_mode='users'):
        self.firebaseConfig = import_db_settings(path)
        firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.db = firebase.database()
        self.user_create_mode = user_create_mode

    def fetchUserData(self, user_id):
        return dict(self.db.child("users").child(user_id).get().val())

    def createUser(self, user_id, user_data):
        self.db.child(self.user_create_mode).child(user_id).set(user_data)

    def createDummyProfiles(self, number):
        for i in range(number):
            age = random.randrange(18, 50)
            sex = random.choice(["male", "female", "dont say", "other"])
            location = random.choice(["Prague", "London", "Moscow", "Kiev", "Vienna", "Berlin"])
            data = {"name": f"test_name{number}", "sirname": f"test_sirname{number}", "age": age, "sex": sex,
                    "image_ulr": ["img1", "img2", "img3"], "bio": f"test_bio{number}: blablablablabla",
                    "location": location, "interest_tags": ["tag1", "tag2", "tag3"]}
            self.db.child("test_users").push(data)

    def removeDummyProfilesAll(self):
        self.db.child("test_users").remove()


if __name__ == "__main__":
    fireBase = Firebase()

    # fireBase.removeDummyProfilesAll()
    # fireBase.createDummyProfiles(10)
    # print(fireBase.fetchUserData("7NhwiPqbkrY3cWingePesqFdfBn1"))
