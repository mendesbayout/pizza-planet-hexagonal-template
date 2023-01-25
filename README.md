# Pizza Planet hexagonal template

## Development

### Infrastructure

Inside **_infrastructure/local_** folder, create a file called `terraform.tfvars` with the next content:

```terraform
REGION                 = "us-east-1"
TF_AWS_ACCESS_KEY      = "AKI****************"
TF_AWS_SECRET_KEY      = "gL************************"
TF_AWS_SESSION_TOKEN   = ""
ENV                    = "DEV"
```

### Backend:

Inside **_api_** folder, create a `.env` file and copy the same content of the `.env.dev.example` file.

> Empty environment variables are secret and you must ask a member of the auth service team for them.


### Virtual Environment

A good practice is to have an isolated environment for each project. To do so type in your console the following:

```bash
$ cd <project_directory>/api
$ python -m virtualenv .venv # FOR MACOS: python3 -m virtualenv .venv
# Activate the virtual environment
# WINDOWS
$ .\venv\scripts\activate
# LINUX/MACOS
$ source ./venv/bin/activate
# Install dependencies
$ pip install -r requirements.txt
$ pip install -r requirements.test.txt
# You're all set
```

### Develop in local with localstack:

Before you start the setup, make sure you have installed:
- [Docker](https://www.docker.com/products/docker-desktop/), [Docker Compose](https://docs.docker.com/compose/) and optionally [NoSQL Workbench for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.settingup.html) for showing the table's content


After the requirements are satisfied, in the root folder of the project we can execute the next command:

```bash
docker-compose up --build
```

This command should be executed only the first time or if you need to rebuild the services, in most scenarios
we just need to execute the following command every time we want to run the project:

```bash
docker-compose up
```

That's all, the localstack with dynamoDb table should be running.

How to see if the tables were already created.
1. Open NoSQL Workbench
2. In operation builder select new connection
3. Add the DynamoDB local connection with the port 4566
4. Inside Operation builder you should see the table/s defined in the common dynamo module.

You could open the following url:
- [http://localhost:4566/health](http://localhost:4566/health)


and check if the DynamoDb says running

## How to run the backend in a container :whale:

First, make sure you have docker installed in your machine.

1 - Go to your terminal at api level level and prompt, `docker build -t clientapp:latest` to build the image.

2 - Then you should run `docker run -d --name clientapp -p 8080:80 clientapp` to run the image in a conteiner.

3 - The backend should be available at  `http://localhost:8080/docs`.





### PEP8 Compliance
This codebase is pep8 compliant. To apply pep8 rules automatically you have to:

1. Install development testing.

   `pip install -r requirements.test.txt`
1. Run `autopep8`.

    `autopep8 --in-place --aggressive **/*.py`
2. Check if there's any non-compliant code. This is in case that the tool didn't catch it.

    `pycodestyle --quiet --statistics --exclude=.venv,.pytest-cache .`
