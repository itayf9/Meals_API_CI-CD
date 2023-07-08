# Meals_API_CI-CD

## API:
This project implements a RESTful API for meals and extents [Meals And Dishes REST API](https://github.com/itayf9/Meals_And_Dishes_REST_API) by adding Github Actions CI/CD pipeline to it.

An extended version of the API, without the Github Actions additions, can be found in [Meals App With Microservices](https://github.com/itayf9/Meals_App_With_Microservices).

## The Workflow "assignment3":
In addition to the capabillities of the meals API, a GitHub Actions CI/CD pipeline for the dishes and meals is added as a workflow called "assignment3".
- The workflow is triggered by a push event to the repository.
- It builds a Docker image out of the Dockerfile of the meals API service.
- It runs the image on a Docker container, and tests the API.

## The Jobs of "assignment3":
The workflow has 3 different jobs:
- The first job (the "build" job) builds the image for the meals service. If successful, it proceeds to the second job.
- The second job (the "test" job) uses the image from the first job to run it in a container and uses pytest to test the service. If successful, it proceeds to the third job.
- The third job (the "query" job) also runs the image in a container. It issues specific requests to the service and record the results in a file.

## Docker:
The application can run in a Docker container.
