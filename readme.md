# CRM

### Setup
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








   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>