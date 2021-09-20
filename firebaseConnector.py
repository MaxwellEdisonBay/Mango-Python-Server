import pyrebase


def firebase_controller():
    firebaseConfig = {"apiKey": "AIzaSyAEWZS9ue3Dc066D7wZf5auYVuBCqVMUB0",
                      "authDomain": "mango-a3686.firebaseapp.com",
                      "databaseURL": "https://mango-a3686-default-rtdb.europe-west1.firebasedatabase.app",
                      "projectId": "mango-a3686",
                      "storageBucket": "mango-a3686.appspot.com",
                      "messagingSenderId": "199539274648",
                      "appId": "1:199539274648:web:98dd00665e295c760b71ed",
                      "measurementId": "G-741MXML50Y"}

    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()

    data = {'age':40, "address":"New York", "employed":True, "name":"John Smith"}

    db.child("people").child('MAX').set(data)


if __name__ == "__main__":
    firebase_controller()


