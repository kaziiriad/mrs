# Movie Rating System Backend
This project is a backend system for an movie rating system developed using Django REST Framework (DRF) and PostgreSQL. The project has been dockerized for easy deployment.

## Description 
The backend system provides essential functionalities for managing courses and enrollments on the online learning platform. It allows users to create or retrieve a list of available movies, give rating retrieve specific movies by their ID and name.

## API Endpoints

### Movie API
- **GET /movies/:** Retrieve a list of available movies.
- **GET /movie/?name={movie_name}:** Retrieve movie details with average rating.
- **POST /movies/:** Add a movie to the database.

### Rating API
- **GET /rating/:** Retrieve a list of available ratings.
- **POST /rating/:** Add rating for a movie.

## Getting Started

To set up and run the project locally, follow these steps:

1. Clone the project.
```bash
git clone https://github.com/kaziiriad/mrs.git
``` 
2. Navigate to the project directory:
```bash
cd mrs/
```
3. Modify the `env.example` to `.env` and add API credentials:

4. Build and run the Docker containers:

```bash
docker-compose up --build
```
5. Access the API endpoints through the appropriate URLs:

- Course API: `http://localhost:8000/api/movies`
- Enrollment API: `http://localhost:8000/api/rating`

## Dependencies
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **Docker**

## Contributors
- [Sultan Mahmud](https://github.com/kaziiriad)

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit).

