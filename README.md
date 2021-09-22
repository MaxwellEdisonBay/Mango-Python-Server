# Mango App API

## Idea
The idea is to create a RESTful API and web application for preparing card queries for Kotlin mobile application. 
Mango App API interacts with **Firebase Realtime Database**, gets the required data, applies some search and classification algorithms and provides an output **JSON** for the mobile app. 
Also, API processes smaller requests such as like someone, change user data etc.

### Expected basic functionality
* Database connection and query processing
* Simple requests from Kotlin frontend processing
* Profile search algorithm
* Minimalistic website
  * Login / registration form
  * Beautiful UI/UX
  * Mobile app link

### Future expansions
* Better locations
  * GPS timestamp
  * Distance calculation + search matches in a distance range
  * Google Maps API - more location functionality
* Text bio ML classification algorithm
  * Polynomial Bayes / SVM multi-class classification
  * Hidden user classification, improved search
* Database optimization, SQL
* Events nearby
  * Facebook/VK API
  * Local events parsing into JSON
  * Event recommendations
* Message tips to start up a conversation
* Gamification, more mechanics for comfortable UX _(experimental, A/B-tests)_
* Guidelines violation filter
  * image recognition
  * Keras machine learning classification

## Search algorithm main goals
* Provide the best match for a user according to given parameters
* A user gets content even though there is no matches
* All the given profile bunches must be tracked to avoid unwanted card repetitions
* *developing*

## Packages

### firebaseConnector.py  
Handles all the database interaction, queries processing and data fetching.  

| Method | Arguments | Description | Returns
| --- | --- | --- | --- |
| `requestsProcessor` | | Main HTTP requests listener, calls other methods to process received requests | |
| `submitLike` | _**user_id_send** : String, **user_id_liked** : String_ | Adds user id into liked user's tree in DB, see database structure (**used_id_send** into **users/{user_id_liked}/liked_me**) | Integer _(success/fail code)_|
| `fetchUsersWithParams` | _**search_params**: Params_ | Fetches user profiles JSONs from DB according to given params  | List of User
| `evaluateUser` | _**users**: User, **search_params** : Params_ | Calculates how user profile fits required parameters  | Float _(User weight coefficient)_

### app.py
Main web application package handling incoming HTTP requests and sending prepared data

### test.py
Debug console app for testing HTTP requests on production

### Technologies
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - main web framework
* [Firebase](https://firebase.google.com/) - noSQL database by Google
* [Heroku](https://devcenter.heroku.com/categories/reference) - web application deploy
* [Pyrebase](https://github.com/thisbejim/Pyrebase) _- Firebase python API_
* [Requests](https://docs.python-requests.org/en/latest/) - HTTP requests handling
* [Scikit Learn _(future)_ ](https://scikit-learn.org/stable/) - ML library
* [Keras _(future)_ ](https://keras.io/) - Python deep learning API

### Inspiration
* [Amazing Profile Bio ML AI Model](https://towardsdatascience.com/dating-algorithms-using-machine-learning-and-ai-814b68ecd75e)
* [Distance Between Two Locations](https://towardsdatascience.com/driving-distance-between-two-or-more-places-in-python-89779d691def)
* [Deep Learning Web App Using Keras](https://towardsdatascience.com/a-complete-deep-learning-portfolio-project-9c5dc7f3f2ef)
* [Scikit Learn Classifier Calibration](https://towardsdatascience.com/introduction-to-reliability-diagrams-for-probability-calibration-ed785b3f5d44)
* [Amazing Morphological Analysis Library for NLP](https://github.com/petrpulc/python-majka)
* [Scikit Learn Support Vector Machine in Details](https://towardsdatascience.com/svm-with-scikit-learn-what-you-should-know-780f1bc99e4a)
* [Multiclass ML Classification](https://towardsdatascience.com/machine-learning-multiclass-classification-with-imbalanced-data-set-29f6a177c1a)
## API requests supported

| Request | Arguments | Description | Returns
| --- | --- | --- | --- |
| `like` | _user_id_send, user_id_liked_ | Like another profile and fill **used_id_send** into **users/{user_id_liked}/liked_me** | _result_code_
| `get-cards` | _user_id_send | Prepares and sends a set of profile cards according to user's search preferences  | JSON with a set of users cards

## Firebase Realtime Database

### Users
Main database node containing all the user profile data

![image](https://i.ibb.co/c2mhBKn/users-db.png)

### Chats & Messages
Chats and chat messages nodes  
`* - node header`

![image](https://i.ibb.co/jrxJQVN/chats-messages-db.png)

## Heroku deploy  
**Actual production URL:** `https://mango-friends.herokuapp.com/`  
Web application is easy to be deployed in Heroku by using following commands:  
`$ heroku login`  
`$ git add .`  
`$ git commit -am "Heroku deploy"`  
`$ git push heroku HEAD:master`
