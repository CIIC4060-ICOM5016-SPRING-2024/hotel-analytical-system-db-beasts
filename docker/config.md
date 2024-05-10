# Docker Configuration
## Create Container (Terminal)
```
docker run --name pruebas -e POSTGRES_PASSWORD=password -e POSTGRES_HOST_AUTH_METHOD=trust -p 5432:5432 -d postgres
```
## Route (Exec)
```
su postgres
psql postgres
```
## Create Database (Exec)
> [!Warning]<br>
> Don't forget the semicolon (;)
```
create database database_name;
create user user1 with encrypted password ‘user1’;
grant all privileges on database test1 to user1;
```
## Create User (Exec)
```
create user user1 with encrypted password ‘user1’;
```
## Grant Privileges (Exec)
```
grant all privileges on database test1 to user1;
```
## Database Owner (Exec)
```
alter database test1 owner to user1;
```