# Python and FastApi

Groupe IGS / IPI Toulouse - Master IL 

## Requirements
- Python 3
- Pip 3

```bash
pip install -r requirements.txt
```

## Virtual environment for MAC OS

```bash
# Create your virtual environment
virtualenv -p python3 <desired-path>
```

```bash
# Activate your virtual environment
source <desired-path>/bin/activate
```

```bash
# Deactivate your virtual environment
deactivate
```

## FastApi

```bash
# Install FastApi
pip install fastapi
```

```bash
# Install Unicorn
pip install uvicorn
```

Create a new directory

Create a `main.py` file

```bash
cd fastApi
```

```bash 
uvicorn main:app
# OR
uvicorn main:app --reload
```

→ http://127.0.0.1:8000

→ http://127.0.0.1:8000/docs

## Set your DB environment

**With `dotenv`**

Copy/Past `.env.example` and rename file into `.env` then add correct values

**Without `dotenv`**

Copy/Past `database.example.py` and rename file into `database.py` then modify `DATABASE_URL`variable 
Replace `DIALECT`, `DRIVER`, `USER`, `PWD`, `DATATABLE`, `PORT` with your own values.

## Routes

**Pokemon**
- [x] Get all
- [x] Get one by ID
- [x] Get one by name
- [x] Create one
- [ ] Delete one
- [ ] Update one
    
**Type**
- [x] Get all
- [x] Get one by ID
- [x] Get one by name
- [ ] Create one
- [ ] Delete one
- [ ] Update one

**Sprite**
- [x] Get all
- [x] Get one by ID
- [ ] Create one
- [ ] Delete one
- [ ] Update one

**Ability**
- [x] Get all
- [x] Get one by ID
- [x] Get one by name
- [ ] Create one
- [ ] Delete one
- [ ] Update one

**User**
- [ ] Get all
- [ ] Get one by ID
- [ ] Get one by name
- [ ] Create one
- [ ] Delete one
- [ ] Update one

**When Pokémon is creating :**
- `Type` and `Ability` are create if no existe in database
- Relations `pokemon-ability` and `pokemon-type` are also created


## AUth with JWT Token

* Create an account `/signin`
* Login to an account `/login`
* Logout to an account `/logout`
* Delete account `/delete`

To have actions on `PUT`, `POST` and `DELETE` request you have to be login _via_ `/login`
**If not account** : create an account with a name and password _via_ `/signin`.
To secure our routes add a middleware on your router, check if request are receive with a valid **JWT TOKEN**

## Middleware


## Database with using ORM SQLAlchemy

```bash
# Install SQLAlchemy
pip install SQLAlchemy
```

```bash
# Install MySQL Driver
pip3 install PyMySQL
```

### Datatables

- Pokemon
- Ability
- Sprite
- Type
- User

#### Relation

One **Pokémon** have One **Sprite**

One **Sprite** have One **Pokémon**

→ One to One

One **Pokémon** have many **Ability**

One **Ability** have many **Pokémon**

→ Many to Many

One **Pokémon** many **Type**

One **Type** many **Pokémon**

→ Many to Many
