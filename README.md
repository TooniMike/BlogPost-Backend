# Blog Post API Endpoints

**This project contains API endpoints for a basic Blog Post Application using Django Rest Framework**

## Table of Contents

- [Introduction](#introduction)
- [API Endpoints](#api-endpoints)
  - [User Authentication](#user-authentication)
  - [Blog Post Management](#blog-post-management)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project provides a simple backend API for managing blog posts. It includes user authentication and basic CRUD (Create, Read, Update, Delete) operations for blog posts. The API is built with security in mind, ensuring that only authenticated users can create or update posts.

## API Endpoints

### User Authentication

- **`POST /auth/users/`**  
  Register a new user by providing a username and password in the request body.  
  Example request body:

  ```json
  {
    "username": "your_username",
    "password": "your_password",
    "email": "your_email"
  }
  ```

- **`POST /auth/token/login/`**  
  Log in an existing user and retrieve an authentication token by providing a username and password.
  Example request body:
  ```json
  {
    "username": "your_username",
    "password": "your_password",
  }
  A successful login will return a token:
  {
  "auth_token": "your_token_here"
  }
  ```

## Blog Post Management

- **`GET /blogposts/`**
  Retrieve a list of all blog posts. This endpoint is accessible without authentication.

- **`POST /blogposts/`**
  Create a new blog post. You must provide the Bearer Token in the Authorization header, along with the title and content in the request body.
  Example request body:
  ```json
  {
  "title": "Your Blog Post title",
  "content": "The content of your blog post."
  }
  ```
  Example Authorization header:
  Authorization: Bearer your_token_here

- **`GET /blogposts/<postID>`**
  Retrieve the details of a specific blog post using the postID. This endpoint is accessible without authentication.

- **`PUT /blogposts/<postID>`**
  Update an existing blog post by providing the Bearer Token in the Authorization header. You can modify the title and/or content.
  Example request body:
  ```json
  {
  "title": "Updated Title",
  "content": "Updated content of the blog post."
  }
  ```

- **`GET /myblogposts/`**
  Retrieve a list of all blog posts created by the authenticated user. You must provide the Bearer Token in the Authorization header.

## Contributing

We welcome contributions! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
