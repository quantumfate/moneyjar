# moneyjar

Application for Money jar financing system.

## TOC

- [Backend](/backend/README.md)
    - [api](/backend/api/README.md)
    - [models](/backend/models/README.md)
    - [utils](/backend/utils/README.md) 
- [Frontend](/frontend/README.md)
    - [components](/frontend/src/components/README.md)
    - [pages](/frontend/src/pages/README.md)
    - [services](/frontend/src/services/README.md)

## Documentation and Initilization of base Project

Most of the documentation and boilerplate code has been generated using the [ChatGPT](https://chat.openai.com/chat) Bot from [OpenAI](https://openai.com/). ChatGPT made a great contribution to the base folder structure.

## Run the application in Docker

To use this Dockerfile to build a Docker image, you can run the following command:

`$ docker build -t my-app .`

This will create a Docker image with the tag my-app. To run the image as a Docker container, you can use the following command:

`$ docker run -p 5000:5000 my-app`

This will start the Docker container and expose the backend on port 5000 of your host machine. You can then access the backend using a GraphQL client, such as Insomnia.

As for the frontend, you will need to start the React Native development server inside the Docker container. To do this, you can use the following command to open a shell inside the Docker container:

`$ docker exec -it <CONTAINER_ID> /bin/bash`

Once you are inside the container, you can navigate to the frontend directory and start the React Native development server using the following commands:

```bash
$ cd /app/frontend
$ npm start
```
This will start the development server for the frontend and print a URL that you can use to access the frontend in a web browser or the [Expo](https://expo.dev/) app on your phone.

I hope this helps! Let me know if you have any questions.

## Contributing

Please have a look at the [contribution section](/.github/CONTRIBUTING.md)

## License

[GPL-3.0 license](/LICENSE)