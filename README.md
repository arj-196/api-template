This is a api template repository. It doesn't do anything yet.
You can use this repository as a starting point for building your own API.


Product structure and important files:

- **environment variables**:
  - We have 2 env files: 
    - `.env` contains all the sensitive information which is not tracked in git. So this file needs to be created manually.
    - `.env.docker.env` file is used to configure our app in docker.
    - The app should also be able to run outside docker containers. This makes using debugging tools much easier.
- 
