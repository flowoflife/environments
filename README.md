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

## 5. Creating environment package list
```bash
# create packgage list files
pip list --format=freeze > pip_pkgs.txt
conda list --explicit > conda_pkgs.txt

# create new environment using package list files
conda create --name NEWENV --file conda_pkgs.txt
pip install -r pip_pkgs.txt

```

## 6. Setting Jupyter Lab extensions

```bash
# Manager
jupyter labextension install @jupyter-widgets/jupyterlab-manager

# Spark
jupyter labextension install jupyterlab_spark

# Table of content
jupyter labextension install @jupyterlab/toc

# Ploty Jupyter Dash
pip install jupyter-dash

# ipympl %matplotlib widget
pip install ipympl

# Tensorboard, should not use
jupyter labextension install jupyterlab_tensorboard

# ipywidgets
pip install ipywidgets
jupyter nbextension enable --py --user widgetsnbextension

# knowledgelab is outdated, should not install
pip install knowledgelab
jupyter labextension install knowledgelab

# itkwidgets
pip install itkwidgets
jupyter labextension install jupyter-matplotlib jupyterlab-datawidgets itkwidgets
# using
from itkwidgets import view
view(image)

# SOS
conda install jupyterlab-sos -c conda-forge
jupyter labextension install transient-display-data
jupyter labextension install jupyterlab-sos

# Lab commands, should not install
pip install jupyterlab_commands
jupyter labextension install jupyterlab_commands
jupyter serverextension enable --py --user jupyterlab_commands

# jupytext
pip install jupytext

# Jupiter lab sql is outdated, should not install
pip install jupyterlab_sql
jupyter serverextension enable jupyterlab_sql --py --user

# Go to definition
jupyter labextension install @krassowski/jupyterlab_go_to_definition 

# Language server
pip install jupyter-lsp
jupyter labextension install @krassowski/jupyterlab-lsp 
conda install -c conda-forge python-language-server r-languageserver
# setting
{
  "language_servers": {
    "pyls": {
      "serverSettings": {
        "pyls.plugins.pydocstyle.enabled": true,
        "pyls.plugins.pyflakes.enabled": false,
        "pyls.plugins.flake8.enabled": true
      }
    },
    "r-languageserver": {
      "serverSettings": {
        "r.lsp.debug": false,
        "r.lsp.diagnostics": false
      }
    }
  }
}

# Error, should not install
jupyter labextension install jupyterlab-drawio

# Latex
pip install jupyterlab_latex
jupyter labextension install @jupyterlab/latex
jupyter serverextension enable --py --user jupyterlab_latex

# Jupyter Lab Code Formatter
pip install autopep8 rpy2
R
install.packages("formatR", repos = "http://cran.rstudio.com")
install.packages("styler")
jupyter labextension install @ryantam626/jupyterlab_code_formatter
pip install jupyterlab_code_formatter
jupyter serverextension enable --py --user jupyterlab_code_formatter
# using, error name rpy2 not defined in R
library(formatR)
sessionInfo()
library("styler")
# setting
{
    "autopep8": {
        "max_line_length": 80,
        "ignore": [
            "E226",
            "E302",
            "E41",
            "E402",
            "E703"
        ]
    },
    "styler": {
        "math_token_spacing": {
            "zero":["'^'"],
            "one":["'+'", "'-'", "'*'","'/'"]
        },
        "reindention": {
            "regex_pattern" : "^###",
            "indention" : 0,
            "comments_only" : true}
    },
    "formatR": {
        "indent": 4,
        "arrow": true,
        "wrap": true,
        "width_cutoff": 150
    },
    "preferences": {
        "default_formatter": {
            "python": "autopep8",
            "r": "styler"
        }
    }
}

# Debugger
jupyter labextension install @jupyterlab/debugger
pip install xeus-python

# Trouble-shooting
# To uninstall and disable extensions
jupyter labextension disable jupyterlab-drawio
jupyter labextension uninstall jupyterlab-drawio 
jupyter labextension disable jupyterlab_sql
jupyter labextension uninstall jupyterlab_sql
pip uninstall jupyterlab_commands
jupyter labextension uninstall jupyterlab_commands
jupyter serverextension disable jupyterlab_commands


# Delete a line or set False of jupyterlab_commands extension in 
# ~/.jupyter/jupyter_notebook_config.json

# Delete file: page_config.json inside folder: 
# ~/opt/miniconda3/envs/myenv/share/jupyter/lab/settings/

# Dissable server extensions
jupyter serverextension list
jupyter serverextension disable jupyterlab_sql
jupyter serverextension disable jupyterlab_sql --user
jupyter serverextension disable jupyterlab_sql --sys-prefix

# Rebuild
jupyter lab clean
jupyter lab build

```