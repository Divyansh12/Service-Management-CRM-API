# CRM

### Setup

- Download postgreSQL from https://www.postgresql.org/download/
- Setup postgres Database by using psql command line.
- Get the Database Credentials.
- Create a ```.env``` file in the project folder. 

```
DEBUG=True
DB_NAME=crm
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
SECRET=<Your Secret>
```
  > Note : If no Database credentials are supplied db.sqlite3 will be used.
  ```
  DEBUG=True
  SECRET=<Your Secret>
  ```
- Use ` pip install -r requirements.txt` to install all the dependency for the project.
- Migrate the database by ` python manage.py migrate` 
- Create Super User for the project using ` python manage.py createsuperuser`

### Build

- Use `python manage.py collectstatic` to collect all the static files.
- Change the ALLOWED_HOSTS in `settings.py`.
- Set DEBUG=FALSE in `.env`.
- Set CORS_ORIGIN_WHITELIST in `settings.py`.
> Note :  For now CORS_ORIGIN_ALLOW_ALL is set to True. 


## Usage

#### To create new users

- `/api/v1/auth/register` 
  - _Allowed Methods_ : `POST`
  - `Authorisation`: `Bearer <token>` 
  - Only superuser or management can create new users.
  - Only this API can be used to register new user no other endpoint will work or management and superuser can create new user using Admin Panel. 
  > Note : Only user having is_management or is_superuser True will be allowed to use this to register user
  
- `/api/v1/auth/login`
  - _Allowed Methods_ : `POST`
  - To login each kind of user same login endpoint can be used. 
  - fields: `username, password`
  
- `/api/v1/auth/user`
  - _Allowed Methods_ : `GET`
  - `Authorisation`: `Bearer <token>` 
  - To get the user info.
  
- `/api/v1/manage/user/`
  - _Allowed Methods_ : `GET, PUT, PATCH, DELETE`
  - `Authorisation`: `Bearer <token>` 
  - To manage User details by management.
  
- `/api/v1/auth/user/changepassword`
  - _Allowed Methods_ : `POST`
  - `Authorisation`: `Bearer <token>` 
  - To change user password if logged in (have token).

#### To create and manage clients
- `/api/v1/manage/client/`
  - _Allowed Methods_ : `GET`
  - `Authorisation`: `Bearer <token>` 
  - _Permissions_ : ` Management Team Member`
  - To get all the client details by management.

- `/api/v1/manage/client/{id}/`
  - _Allowed Methods_ : `GET, PUT, PATCH, DELETE`
  - `Authorisation`: `Bearer <token>` 
  - _Permissions_ : ` Management Team Member`
  - To manage the client details by management.

- `/api/v1/client/`
  - _Allowed Methods_ : `GET, POST`
  - `Authorisation`: `Bearer <token>` 
  - _Permissions_ : ` Sales Team Member`
  - To create client by sales team member.
  - To get details of all the clients
- `/api/v1/client/{id}`
  - _Allowed Methods_ : `GET, POST, PUT, PATCH, DELETE`
  - `Authorisation`: `Bearer <token>` 
  - _Permissions_ : ` Sales Team Member`
  - To edit client details.
  - To get details of a particular client.
  - To delete client details.

#### To create and manage contracts
- `/api/v1/manage/contract/`
  - _Allowed Methods_ : `GET`
  - `Authorisation`: `Bearer <token>` 
  - _Permissions_ : ` Management Team Member`
  - To get all the contract details by management.

- `/api/v1/manage/contract/{id}/`
  - _Allowed Methods_ : `GET, PUT, PATCH, DELETE`
  - `Authorisation`: `Bearer <token>` 
  - _Permissions_ : ` Management Team Member`
  - To manage the contract details by management.

- `/api/v1/contract/`
  - _Allowed Methods_ : `GET, POST`
  - `Authorisation`: `Bearer <token>` 
  - _Permissions_ : ` Sales Team Member`
  - To create contract by sales team member.
  - To get details of all the contracts.
- `/api/v1/contract/{id}`
  - _Allowed Methods_ : `GET, POST, PUT, PATCH, DELETE`
  - `Authorisation`: `Bearer <token>` 
  - _Permissions_ : ` Sales Team Member`
  - To edit contract details.
  - To get details of a particular contract.
  - To delete contract details.
  
#### To create and manage events
- `/api/v1/manage/event/`
  - _Allowed Methods_ : `GET`
  - `Authorisation`: `Bearer <token>` 
  - _Permissions_ : ` Management Team Member`
  - To get all the events details by management.

- `/api/v1/manage/event/{id}/`
  - _Allowed Methods_ : `GET, PUT, PATCH, DELETE`
  - `Authorisation`: `Bearer <token>` 
  - _Permissions_ : ` Management Team Member`
  - To manage the event details by management.

- `/api/v1/event/`
  - _Allowed Methods_ : `GET, POST`
  - `Authorisation`: `Bearer <token>` 
  - _Permissions_ : ` Sales Team Member`
  - To create contract by sales team member.
  - To get details of all the events.
- `/api/v1/event/{id}`
  - _Allowed Methods_ : `GET, POST, PUT, PATCH, DELETE`
  - `Authorisation`: `Bearer <token>` 
  - _Permissions_ : ` Sales Team Member`
  - To edit event details.
  - To get details of a particular event.
  - To delete event details.

#### To manage events By Support
- `/api/v1/support/event/`
  - _Allowed Methods_ : `GET`
  - `Authorisation`: `Bearer <token>` 
  - _Permissions_ : ` Support Team Member`
  - To get details of all event assigned to them.

- `/api/v1/support/event/{id}/`
  - _Allowed Methods_ : `GET, PUT, PATCH, DELETE`
  - `Authorisation`: `Bearer <token>` 
  - _Permissions_ : ` Support Team Member`
  - To edit event details assigned to them.
  - To get details of a particular event assigned to them.
  - To delete event details assigned to them.

## Postman Collection 


> _link_ : https://www.getpostman.com/collections/aeed6ed66557d456aebf

