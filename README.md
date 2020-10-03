# Bounce - Basketball Court Finder
## Contributors Needed!
##### Creator: Caleb Fahlgren
##### Project Email: bounceapp@protonmail.com
##### URL: https://bouncemap.com
 
# What is Bounce?

Bounce is a web app built in Django that locates and displays the nearest basketball courts in the area. With over 48,000 documented basketball across North America, there is bound to be one near you. The goal of this project is to build a community for basketball and other sports enthusiasts.

![Image](https://i.ibb.co/Mp1dxwB/readme.jpg)

# Features
  - Basketball court listing of outdoor courts near specified address/location
  - Light and Dark Theme for Maps
  - GraphQL / REST API endpoint
  
 # Next Steps
  - Implement more testing and test coverage (API, Model, End to End Testing with [Cypress.io](https://cypress.io)
  - Building CI/CD pipeline and linting for better code reviewing and deployment
  - Interfaces for User Feedback
  - Ensure pages are mobile friendly

# Future Plans!
  - Load courts through REST / GraphQL API
  - User Accounts
    - Court Ratings
    - Save frequently visited courts
    - Submit Court to be added to Map
  - Decouple front and backend

# Tech
Bounce uses a number of open source projects and APIs to work properly:
* [Heroku](https://www.heroku.com/) - PAAS to Host Bounce
* [Django](https://www.djangoproject.com/) - Python Web Framework
* [LocationIQ API](https://locationiq.com/) - used to get reverse geocoding results for markers
* [Mapbox API](https://www.mapbox.com) - used to provide forward-geocoding results and mapping
* [PostgreSQL](https://www.postgresql.org/) - SQL database for scalability, modularity, and geoquerying support
