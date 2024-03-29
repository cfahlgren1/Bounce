# Bounce - Basketball Court Finder
 
# What is Bounce?

Bounce is a web app built in Django that locates and displays the nearest basketball courts in the area. With over 48,000 documented basketball across North America, there is bound to be one near you. The goal of this project is to build a community for basketball and other sports enthusiasts.

## Home Page
<img width="1719" alt="image" src="https://user-images.githubusercontent.com/13546028/196266949-7b4bedeb-90c1-4633-a23d-bd26cc79dd26.png">

## Courts Page

![Image](https://i.ibb.co/Mp1dxwB/readme.jpg)

# Contributing
### Visit [Contributing.md](https://github.com/cfahlgren1/Bounce/blob/postgis/CONTRIBUTING.md)

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

# Setup

## Docker

0. Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)

1.  Make `docker_entrypoint.sh` executable
    ```bash
    # Linux
    chmod +x docker_entrypoint.sh
    ```

2.  Start and build the 2 containers

    -   `--build` builds the images defined in the `docker-compose.yml` file.
    -   `-d` dettaches the terminal from the building process.
    -   Finally the script from (`docker_entrypoint.sh`) is executed.

    ```bash
    # In the same directory as `docker-compose.yml`
    docker-compose up -d --build
    ```

    - If there are errors you can see the logs
    ```bash
    docker-compose logs
    ```

3. Load Initial Database Models

    - It's also necessary to load in the fixtures when setting up the database:
    ```bash
    docker-compose exec web python manage.py loaddata bounce_data.json
    ```

4. Go to http://localhost:8000

    - You should see the frontend of the project

    <img src="https://i.imgur.com/JDQp06y.png" width="800">

5. Enter a shell within the Docker container

    - To enter an interactive shell (in this case for the "web" service), you can use
    ```bash
    docker-compose exec web bash
    ```

6. Create a superuser (Optional)

    - You may enter an interactive shell within the Docker container
     (in this case the container corresponding to the "web" service)
    - In the same directory as `docker-compose.yml` run
    ```bash
    # This open a bash shell inside the container
    docker-compose exec web bash
    ```

    - Then run `python manage.py createsuperuser`
    
    - Run `exit` to exit the container. It will keep running.

7. To stop the containers run `docker-compose stop`

    - :warning: Be careful with [`docker-compose down`](https://docs.docker.com/compose/reference/down/) which stops the container but also **removes** them.
=======


## Troubleshooting

Ensure that your .env file is present and the required variables are set. 
Sometimes starting fresh can help, since things like volumes will persist
even after a container is removed, which can cause issues. You can remove all 
docker containers and volumes using the command:
```bash
docker-compose down && docker rm -f $(docker ps -a -q) && docker volume rm $(docker volume ls -q)
```
and then trying the above steps again.
