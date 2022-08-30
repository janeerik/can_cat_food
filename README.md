## Can cat food?

This app allows to click a button and track when was the cat (or Granny?) last fed.

### Installation

#### Ensure you have at least Python 3.7 installed

```shell
python --version
```

#### Clone the repository

```shell
git clone git@github.com:janeerik/can_cat_food.git
```

#### Create the virtual environment

```shell
python -m venv venv
```

#### Activate the environment

```shell
source venv/bin/activate
```

#### Install the dependencies

```shell
pip install -r requirements.txt
```

#### Create and migrate the database

```shell
flask db upgrade
```

#### Run the application in development mode

```shell
flask --debug run
```
