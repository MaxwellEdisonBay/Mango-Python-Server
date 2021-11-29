import pyrebase
import json
import random
import pandas as pd

from flask import Response


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
            gender = random.choice(["male", "female", "dont say", "other"])
            city_location = random.choice(["Prague", "London", "Moscow", "Kiev", "Vienna", "Berlin"])
            occupation = "Student"
            profile_image_urls = [{"index": 1, "url": "url1"}, {"index": 2, "url": "url2"}]
            reg_date = 121313441
            tags = [{"tier": 1, "text": "Sports"}, {"tier": 2, "text": "Hiking"}]
            university = "CVUT"
            zodiac_sign = "Cancer"
            data = {"name": f"test_name{number}", "lastname": f"test_lastname{number}", "age": age, "gender": gender,
                     "bio": f"My test bio {number}",
                    "location": city_location, "university": university, "occupation": occupation,
                    "reg_date": reg_date, "zodiac_sign": zodiac_sign}

            rec = self.db.child(self.user_create_mode).push(data)
            self.db.child(self.user_create_mode).child(rec["name"]).child("uid").set(rec["name"])
            for j, img in zip(tags, profile_image_urls):
                tagRef = self.db.child(self.user_create_mode).child(rec["name"]).child("tags").push(j)
                self.db.child(self.user_create_mode).child(rec["name"]).child("tags").child(tagRef["name"]).child("tag_id").set(tagRef["name"])
                imgRef = self.db.child(self.user_create_mode).child(rec["name"]).child("profile_image_urls").push(img)
                self.db.child(self.user_create_mode).child(rec["name"]).child("profile_image_urls").child(imgRef["name"]).child("img_id").set(imgRef["name"])

    def removeDummyProfilesAll(self):
        self.db.child(self.user_create_mode).remove()

    def getUsers(self):
        users = self.db.child("users").get()
        user_vals = list(users.val().values())
        for i in user_vals:
            i["tags"] = list(i["tags"].values())
            i["profile_image_urls"] = list(i["profile_image_urls"].values())
        print(user_vals)
        return Response(json.dumps(user_vals), mimetype='application/json')


if __name__ == "__main__":
    fireBase = Firebase(user_create_mode='users')
    # fireBase.createUser("data", {"data":"sdsd", "blab":'sdsd'})
    fireBase.removeDummyProfilesAll()
    fireBase.createDummyProfiles(10)
    # print(fireBase.fetchUserData("7NhwiPqbkrY3cWingePesqFdfBn1"))
