# Python and FastApi

Groupe IGS / IPI Toulouse - Master IL 

## Requirements
- Python3
- Pip

## Get dependencies

```bash
pip install -r requirements.txt
```

## If your are using virtual environment for MAC OS

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

## If your are creating a new project with FastApi

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

## Launch project 

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

```bash
pip install python-dotenv
```

Copy/Past `.env.example` and rename file into `.env` then add correct values

**Without `dotenv`** _(our case)_

Copy/Past `database.example.py` and rename file into `database.py` then modify `DATABASE_URL`variable 
Replace `DIALECT`, `DRIVER`, `USER`, `PWD`, `DATATABLE`, `PORT` with your own values.

> If you are using **MySql**, you can install and use the driver `PyMySQL`
> 
>```bash
>pip install PyMySQL
>```
>
>
Example to set your **database_url**

```python
database_url = "mysql+pymysql://root:root@localhost/MyTable"
```

## Other install

```bash
# Install HTTPX
pip install httpx
```

## Routes

**Pokemon**
- [x] Get all
- [x] Get one by ID
- [x] Get one by name
- [x] Create one
- [ ] Delete one
- [x] Update one
    
**Type**
- [x] Get all
- [x] Get one by ID
- [x] Get one by name
- [x] Create one
- [ ] Delete one
- [x] Update one

**Sprite**
- [x] Get all
- [x] Get one by ID
- [x] Create one
- [x] Delete one
- [ ] Update one

**Ability**
- [x] Get all
- [x] Get one by ID
- [x] Get one by name
- [ ] Create one
- [ ] Delete one
- [x] Update one

**User**
- [ ] Get all
- [ ] Get one by ID
- [ ] Get one by name
- [x] Create one
- [x] Delete one
- [ ] Update one

> **When Pokémon is creating :**
> - `Type` and `Ability` are create if no existe in database
> - Relations `pokemon-ability` and `pokemon-type` are also created

### Test your routes

- With direct access to [FastApi Doc](http://127.0.0.1:8000/docs)
- or with `request.http`

#### For routes without using Middleware
For routes `GET` you don't need to have to be **login** and you can try this routes directly on **FastApi Doc**

#### For routes using Middleware

For routes `POST` `PUT` and `DELETE` you have to be **login** and have a token.
You can try and use this routes with `request.http` file.

> ##### How to get your token ?
> 
> If you don't have an account : you have to create your account with `name` and `password` with `/signin` route
> 
> In the FastApi Doc launch the `login` route to get your token.
>
> Or in `request.http` file, use the first request **Get your token**

Copy your new token and in `request.http` file replace `{{ TOKEN }}` with your new token.

⚠️ In `request.http` for `DELETE` routes, replace `id` with a value in the URL

⚠️ If you want to know witch routes you can use and test go to **Routes** section

## Auth with JWT Token

```bash
# generate and verify the JWT tokens in Python
pip install "python-jose[cryptography]"
```

```bash
# handle password hashes
pip install "passlib[bcrypt]"
```

```bash
# Generate random secret key
openssl rand -hex 32  
```

Copy/past `jwt/conf.example.py` and rename file into `conf.py`
Add your own secret key

* Create an account `/signin`
* Login to an account `/login`
* Delete account `/delete`

To have actions on `PUT`, `POST` and `DELETE` request you have to be login _via_ `/login`
**If not account** : create an account with a name and password _via_ `/signin`.
To secure our routes add a middleware on your router, check if request are receive with a valid **JWT TOKEN**

## Middleware

Add your middleware to your route in the parameter of your function

```python
# Example
@router.delete("/{id}")
async def delete(id, current_user: Annotated[User, Depends(get_current_user)]):
    if current_user:
        pass
```
## Database with using ORM SQLAlchemy

```bash
# Install SQLAlchemy
pip install SQLAlchemy
```

```bash
# Install MySQL Driver
pip install PyMySQL
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

![Diagram](../.github/diagram.png "BDD diagram")

