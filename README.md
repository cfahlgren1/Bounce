# Bounce - Basketball Court Finder
##### Dev: Caleb Fahlgren
##### Project Email: bounceapp@protonmail.com
##### URL: https://bouncemap.com
 
# What is Bounce?

Bounce is a web app build in Django that locates and displays the nearest basketball courts in the area. With over 48,000 documented basketball across North America, there is bound to be one near you.

![Image](https://i.ibb.co/Mp1dxwB/readme.jpg)

# Features
  - Basketball court listing of outdoor courts near specified address/location
  - Light and Dark Theme for Maps

# Future Plans!
  - Rate Courts with Like/Dislike Button
  - Favorite Courts that you visit alot
  - Submit Court to be added to Map
  - Authentication with Auth0 (maybe)
  - Rest API

# Tech
Bounce uses a number of open source projects and APIs to work properly:
* [Heroku](https://www.heroku.com/) - PAAS to Host Bounce
* [Django](https://www.djangoproject.com/) - Python Web Framework
* [LocationIQ API](https://locationiq.com/) - used to get reverse geocoding results for markers
* [Mapbox API](https://www.mapbox.com) - used to provide forward-geocoding results and mapping
* [MongoDB](https://www.mongodb.com/) - NoSQL database for scalability and modularity
* [jQuery] - duh

# ToDo
~~* Add 404 Page~~
* Design Homepage
* Build Continous Integration Pipeline through Heroku