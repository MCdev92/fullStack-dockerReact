# Personal Recipe Page 👨🏻‍🍳

The personal recipe page is a full-stack web application built on Python. This application uses reactjs for the frontend and fastApi for the backend. The application is intended to use Docker to have communication between the backend and frontend container using HTTP through the docker network. It is important to know that Docker enables application portability!

## Installation 🏗️

### Prerequisites
* Python 3.7+ --> https://www.python.org/downloads/
* FastApi --> https://fastapi.tiangolo.com/
* React --> https://react.dev/learn/installation
* Docker --> https://docs.docker.com/engine/install/
* SQLite --> https://www.sqlite.org/download.html
* Bootstrap 5 -> https://getbootstrap.com/docs/5.0/getting-started/introduction/

### Setup
1. Clone the repo
   bash<br>git clone https://github.com/MCdev92/fullStack-dockerReact.git<br>
2. Install project dependencies:
   `pip install fastapi uvicorn sqlalchemy` 
   `npm install axios`
   `pip install -r requirements.txt`
3. Run the app
    `docker run --name backend --rm --network recipes -p  8000:8000 backend` 
    `docker run --rm --name frontend  --network recipes -p  3000:3000 frontend`
4. Enable cors in the backend:
    `from fastapi.middleware.cors import CORSMiddleware`
5. Head over to the web broswer and take a look at the delicious recipes! [localhost:3000] (http://localhost:3000/)

## Walkthrough/Demo

![walkthrough](fs-recipe.gif)
         


