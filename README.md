# Flask_API_Template
Basic template to init a new API with Flask. This include the basic autentication with JWT.

This API template was based in the example of Matthias Döring posted in the following article:

https://www.datascienceblog.net/post/programming/flask-api-development/

## Execute the API
In the command prompt, you need execute the following commands:
```
py -3 -m venv .venv
.venv\scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
flask run
```

To exit from the virtual env, you need use the command:
```
deactivate
```

## TEST the API with POSTMAN
With the API running you can test the API with the following public Workspace in Postman:
https://www.postman.com/andresgilabert/workspace/flask-api-template

Login examples:
![image](https://user-images.githubusercontent.com/23640134/172045913-8b5b4d64-7c14-42e1-8778-7e23ef7a381b.png)

![image](https://user-images.githubusercontent.com/23640134/172045934-e637ef97-d870-48ac-96a0-6fb1538fe82c.png)

Authenticated Method:
![image](https://user-images.githubusercontent.com/23640134/172046392-a0beb238-62ce-4fe7-8797-8ef441e3e068.png)


## SWAGGER DOC OF THE API
You can access to the URL:
http://127.0.0.1:5000/api/docs

![image](https://user-images.githubusercontent.com/23640134/172046097-b6f27785-4264-470e-b20a-bb762053480b.png)

