# Group Chat APIs
## To run the project:

Create a virtual environment: <br> <br>
`virtualenv env `  <br> <br>
(If virtualenv package is not installed it can be installed with: `pip install virtualenv` ) <br> <br>
Activate the virtual environment: <br> <br>
`source env/bin/activate` <br> <br>
Install the project requirements: <br> <br>
`pip install -r requirement.txt` <br> <br>
Create a superuser:<br> <br>
`python manage.py createsuperuser` <br> <br>
Run the server: <br> <br>
`python manage.py runserver [PORT_NUMBER]` <br>  <br>

Open Postman for Testing and import collection “group_chat_apis.collection” <br> <br>
To test the APIs a bearer token will need be generated. This token can be generated by sending a POST request to /users/login endpoint with following request body in json format (see below screenshot below): <br> <br>
```
{

"user":"admin01@gmail.com" , 

"username": "admin01@gmail.com", 

"password":12345 

}
``` 
<br> 

![image](https://user-images.githubusercontent.com/1689504/218677620-ee5b7ef5-a9c3-4758-a491-c2d6d33ef311.png) <br>

The generated Bearer token needs to be passed in all the subsequent requests under Authorization option in Postman.<br> <br>
![image](https://user-images.githubusercontent.com/1689504/218677691-2ad5ff3f-ac21-4cbc-93ff-8e83abbbd3a7.png) <br>

Following are the results obtained after making requests to few of the endpoints: <br><br>

POST users/createUser/ <br><br>
![image](https://user-images.githubusercontent.com/1689504/218677809-5f240cef-5284-41f8-9b0f-78dec1c20353.png) <br>


POST chatting/createGroup/ <br> <br>

![image](https://user-images.githubusercontent.com/1689504/218677836-9cb77fa0-0d5b-4fdd-ad47-63b3aa0f6f35.png) <br>

POST /chatting/addUser/ <br> <br>
![image](https://user-images.githubusercontent.com/1689504/218677878-f9e09f67-a377-43bb-865b-571ed8ecf961.png) <br>

GET /chatting/searchUser/?search=all <br><br>
![image](https://user-images.githubusercontent.com/1689504/218677899-c7ddeb8f-4119-49a6-8c65-f1b60e5bff86.png) <br>

DELETE /chatting/delUser/ <br> <br>
![deluser](https://user-images.githubusercontent.com/1689504/218755376-c605885d-65a2-436e-93f9-f794be3a22b3.png) <br>

PATCH /users/updateUser/ <br> <br>
![patchuser](https://user-images.githubusercontent.com/1689504/218757020-bf3db0fa-5c9b-4db8-95ac-1d828d90c92c.png) <br> <br>



## To run the Test Cases:  <br> <br>

Run the server: <br> <br>
`manage.py runserver [PORT_NUMBER]` <br>  <br>

In a separate terminal, run the test cases <br> <br>
`manage.py test chatting`









