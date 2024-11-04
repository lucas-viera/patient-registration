# Patient Registration
FastAPI project with MySQL and Docker


## Objective
1- An API for patient registration that collects the following information: name, email address, phone number, and a photo of the document.

2- The application must perform validation on user-entered data to ensure that all required fields are provided and valid as needed.

3- Upon successful validation of patient data, store it in a MySQL database.

4- After a patient is successfully registered, asynchronously send a confirmation email to prevent application blocking. It is not necessary to design the email; you can use the framework's default template.

5- Utilize Docker to establish the development environment for the application.

### Features pending
4- After a patient is successfully registered, asynchronously send a confirmation email to prevent application blocking. It is not necessary to design the email; you can use the framework's default template.

## How to run project
First, you need to create a `.env` file with the correct environment variables. Look at `.env.sample` file for more information.

Then you can run the project with Docker using the following commands:

```
docker compose build
docker compose up
```

or

```
docker compose up --build
```

And then connect to the database using any MySQL client such as DBeaver or MySQL Workbench.

## Endpoints
Visit `http://localhost:8000/docs` to see all endpoints

### Implemented endpoints
- `GET /` - check if API is working OK
- `POST /register` - register a new patient

### Future endpoints
- `GET /patients` - get all patients
- `GET /patients/{id}` - get a patient by id
- `DELETE /patients/{id}` - delete a patient by id
- `PUT /patients/{id}` - update a patient by id


## Project build

### Docker
1- Create `Dockerfile`

2- Create `docker-compose.yml` file

3- Create `requirements.txt`

4- Create `.env` file

### FastAPI
1- Create `main.py` file containing the API logic

2- Create `db.py` file containing the database logic and models.


## Libraries
- `pydantic` - for data validation
- `pydantic[dotenv]` - for loading environment variables from `.env` file
- `pymysql` - for MySQL database
- `cryptography` - for encryption
- `python-multipart` - for handling multipart/form-data
- `docker` - for containerization
- `uvicorn` - for running the API

