## 1. Setting MySQL Server Docker Container
```bash
# Pull the latest MySQL docker image (https://store.docker.com/images/mysql)
docker pull mysql:8.0.3      # check available tags for more information

# Create instance of your MySQL server docker container
docker run --restart always  \  
--network my-network-name \  # optional
# set your mysql server container name
--name my-mysql-container-server-name \       
# link your local database folder with container                                
-v ~/my/own/datadir:/var/lib/mysql/ \       
# set your database password
-e MYSQL_ROOT_PASSWORD=my-secret-pw \  
# set your database name, MySQL will create it automatically
 -e MYSQL_DATABASE=my-database-name \   
 # set connection port of mysql server
 -p 3306:3306           \                                   
-d mysql:8.0.3              # docker mysql image and tag
                                      # Note: no bash here

```

## 2. Building app using Dockerfile

Put Dockerfile and requirements.txt files below in a working directory.

Build docker image
```bash

docker build -t your-docker-image-name:tag  ~/path-to-folder-of-Dockerfile/

```

Now run the docker container

```bash

docker run -itd --restart always --name your-app-name -v ~/your-local-folder/:/root/ -p 6006:6006 your-docker-image-name:tag bash

```

```bash

docker exec -it your-app-name bash

```

Test if TensorFlow works well or not, create a python test.py below and run: python3 test.py
```bash
#
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
#
```
You will see: Hello, TensorFlow!

## 3. How to use TensorBoard to visualize training and prediction results

To run TensorBoard, use the following command (alternatively python -m tensorboard.main)

```bash
tensorboard --logdir=path/to/log-directory
e.g.: tensorboard --logdir=/opt/project/tensorboard/
```

If this logdir directory contains subdirectories which contain serialized data from separate runs,
then TensorBoard will visualize the data from all of those runs. Once TensorBoard is running, navigate your web browser to localhost:6006 to view the TensorBoard.

## 4. Setting Django project

Check if Django had been installed well or not
```bash
python3 -m django --version
```

Create project
```bash
django-admin startproject project-name
```

Move inside project folder and edit settings.py. 
Change "ALLOWED_HOSTS = []" into ALLOWED_HOSTS = ['*'] (do not set this at production stage) 
and set TIME_ZONE to match with local timezone.

Try development server
```bash
python3 manage.py runserver 0:8000
```

Open web browser and go to http://localhost:8000 to test server.
Create django apps and pull files using git.

```bash
python3 manage.py startapp numberz
```

Finally, structure of project folder should be like this.

```bash
Project_folder/
    project_name/
        app_name/
            __init__.py
            static/
            templates/
            admin.py
            apps.py
            models.py
            views.py         
        project_name/
            __init__.py
            settings.py
            urls.py
            wsgi.py
        static/
        templates/ 
        .gitignore  
        db.sqlite3
        Dockerfile
        manage.py
        README.md
        requirements.txt   
``` 

List of Django manage.py commands

```bash
python3 manage.py runserver
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py diffsettings
python3 manage.py check
python3 manage.py createsuperuser
```
