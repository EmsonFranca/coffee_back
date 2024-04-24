# Coffee Recipes

This project, **Coffee Recipes**, was developed as part of the course *Object-Oriented Systems Analysis and Design* in the Bachelor of Information Technology program at UFERSA. It is a system for coffee recipes with caffeine control, simulating a social network where users can register their coffee recipes. Each recipe includes a title, description, ingredients, caffeine quantity, and preparation method.

## Technologies Used

The project was built using the Django Rest Framework and incorporates the following libraries:

- Django: ^5.0.2
- mysqlclient:^2.1.0 
- djangorestframework: ^3.13.1
- django-cors-headers: ^4.0.1
- drf-spectacular: ^0.19.2

## Endpoints

### Recipes

- **GET /api/recipes/** - Retrieve all recipes
- **POST /api/recipes/** - Create a new recipe

### Ingredients

- **GET /api/ingredient/** - Retrieve all ingredients
- **POST /api/ingredient/** - Create a new ingredient

### Authentication

- **POST /api/token-auth/** - Obtain an authentication token
- **POST /user/create/** - Create a new user
- **POST /user/login/** - Log in as a user

### API Schema and Documentation

- **GET /schema/** - API schema
- **GET /swagger/** - Swagger UI for API documentation

## Language

It's worth noting that this project was an opportunity to practice English, so the entire system was developed in English.

## Repository Links

- Frontend Application Repository: [Coffee Recipes Frontend](https://github.com/Luan029/Coffee_recipes)

## Getting Started

To get started with the project, follow these steps:

1. Clone the backend API repository.
2. Install the required libraries listed above.
3. Set up your database configuration in Django.
4. Run migrations to create the necessary database schema.
5. Start the Django development server.

For the frontend application, clone the repository from the provided link and follow the instructions in its README file.

## Contributing

Contributions to Coffee Recipes are welcome! If you'd like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request with a clear description of your changes.

## License

This project is licensed under the [MIT License](link_to_license_file).
