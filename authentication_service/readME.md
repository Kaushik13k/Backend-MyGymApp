# Service: Authentication Service
This microservice handles the basic authentication flow for the app

## Contents:
- health check
- signup
- login
- auth token
- forgot password

## Prerequisites
- Rust (1.76.0)
- Docker (~24.0.7)

## Installation
* Install Rust: [Rust Installation](https://doc.rust-lang.org/book/ch01-01-installation.html)
* Install Docker: [Docker Installation](https://docs.docker.com/get-docker/)


## The Folder Structure

```.
├── authentication_service
│   ├── Cargo.lock
│   ├── Cargo.toml
│   ├── src
│   │   ├── database
│   │   │   ├── connection.rs
│   │   │   └── mod.rs
│   │   ├── main.rs
│   │   ├── middleware
│   │   │   ├── middleware.rs
│   │   │   └── mod.rs
│   │   ├── mod.rs
│   │   ├── models
│   │   │   ├── forgot_password.rs
│   │   │   ├── mod.rs
│   │   │   ├── signup.rs
│   │   │   ├── tokens.rs
│   │   │   ├── user_inputs.rs
│   │   │   └── users.rs
│   │   ├── routes
│   │   │   ├── entry_point.rs
│   │   │   ├── health.rs
│   │   │   └── mod.rs
│   │   ├── schema
│   │   │   ├── mod.rs
│   │   │   └── users.rs
│   │   ├── services
│   │   │   ├── forgot_password.rs
│   │   │   ├── get_user.rs
│   │   │   ├── login.rs
│   │   │   ├── mod.rs
│   │   │   ├── mutation.rs
│   │   │   ├── query.rs
│   │   │   ├── signup.rs
│   │   │   └── token.rs
│   │   └── utils
│   │       ├── helpers.rs
│   │       ├── logger.rs
│   │       ├── mod.rs
│   │       └── token.rs
│   └── tests
│       └── unit_test
│           └── test_health.rs
└── resources
    └── docker-compose.yaml
```

## How to run
- Setup Rust in Local https://doc.rust-lang.org/book/ch01-01-installation.html
- Create a directory > run `cargo init`
- Create a `.env` and save -> `DATABASE_URL` and `SECRET_KEY`
- `cd` to `resources` and run `docker-compose up`
- To run the project `cargo run`

## Usage
* Import the Postman collection and run it

## Testing
* Run the unit tests with ```cargo test```