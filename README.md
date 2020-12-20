## 1. Install Homebrew and settings

Firstly, install Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Next, install others and settings

```bash
brew install wget

# install iTerm2
brew install --cask iterm2

# install git
brew install git
chsh -s $(which git)
# setting SSH keys and git
git config --global user.name "Your Name Here"
git config --global user.email "your_email@youremail.com"
touch ~/.gitignore
git config --global core.excludesfile ~/.gitignore
git config --global core.editor
# check git setting
git config --list

# install zsh
brew install zsh
chsh -s $(which zsh)
# setting oh my zsh, themes, plugins

# install oh my zsh:
git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc

# install Powerline fonts:
git clone https://github.com/powerline/fonts.git --depth=1
cd fonts
./install.sh
cd ..
rm -rf fonts
# setting fonts in iTerm2 into Meslo LG L DZ for Powerline

# install oh my zsh plugins:
# setting plugin in .zshrc, see .zshrcorig
# zsh-syntax-highlighting is always the last plugin
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone git@github.com:zsh-users/zsh-completions.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-completions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# install jdk
brew install --cask oracle-jdk
sudo ln -sfn /usr/local/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
# check jdk
which java

# install VSCode
brew install --cask visual-studio-code

# install PyCharm CE
brew install --cask pycharm-ce

# install Docker CE
brew install --cask docker
```

## 2. Creating python environment using pyenv, pipenv, conda

Install pyenv

```bash
# install pyenv using homebrew
brew install pyenv
# git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
# echo 'if command -v pyenv 1>/dev/null 2>&1; then eval "$(pyenv init -)"; fi' >> ~/.zshrc
# source ~/.zshrc

# install virtualenv
brew install pyenv-virtualenv
# git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
# echo 'if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
source ~/.zshrc

# install pipenv
brew install pipenv
```

to create virtual env using pyenv-virtualenv

```bash
# using python 3.8.0
pyenv install 3.8.0
# to create virtual env
# it will use venv if existed
pyenv virtualenv 3.8.0 my-env
# a virtual env will be saved at ~/.pyenv/versions/3.8.0/envs/my-env
pyenv activate 3.8.0/envs/my-env
cd ~/to_project_folder
# to start my-env automaticaly when cd into project folder
pyenv local 3.8.0/envs/my-env # to become env of project automatically
pip install -U pip setuptools wheel
pip install -r requirements.txt
# to install nodejs for jupyter notebook
# pip install nodeenv
nodeenv -p
```

or with miniconda/anaconda

```bash
# pyenv and miniconda
pyenv install miniconda3.x.x
pyenv activate miniconda3.x.x
conda update -n base -c defaults conda -y
conda update --all -y
conda create -n my-env python==3.8.0 -y
# a virtual env will be saved at ~/.pyenv/versions/miniconda3.x.x/envs/my-env
# or conda create -p /path/to/project/my-env -f requirements.txt -y
# or pyenv virtualenv miniconda3.x.x my-env
# it will use conda create
pyenv deactivate
pyenv activate miniconda3.x.x/envs/my-env
cd ~/to_project_folder
# to start my-env automaticaly when cd into project folder
pyenv local miniconda3.x.x/envs/my-env # to become env of project automatically
# conda install -c conda-forge package-name -y
pip install -U pip setuptools wheel
pip install -r requirements.txts
```

or with pipenv (Note: VSCode cannot use this virtual env)

```bash
pyenv install 3.8.0 # or pipenv --python 3.8.0
cd ~/project/folder
# to point to python interpreter
pipenv --python ~/.pyenv/versions/3.8.0/bin/python3.8
# a virtual env will be saved at ~/.local/share/virtualenvs/
pipenv install # if Pipfile existed, or Pipfile will be updated
# or
pipenv install -r requirements.txt # Pipfile will be created
# to check security
pipenv check
# to activate virtual env
pipenv shell
# to deactivate
exit
# to check path of virtual env
pipenv --venv
# to remove
pipenv --rm
# to update
pipenv update
pipenv sync  # to sync environments
# to see all dependencies and subdependencies
pipenv graph
# command can be registed as script in Pipfile
[scripts]
test = "python -m unittest discover -v"
# and run
pipenv run test
# to lock package dependencies
pipenv lock  # Pipfile.lock will be created
```

other commands

```bash
# check available pythons
pyenv install -l
# check installed pythons by pyenv
pyenv versions
# check created virtual env list
pyenv virtualenvs
# to set system python of current shell
pyenv shell 3.x.x
pyenv shell --unset
# set global python to 3.x.x
pyenv global 3.x.x
# set global python back to system
pyenv global system
# to set python for current local folder
pyenv local my-env
pyenv local --unset
# to uninstall
pyenv uninstall my-env
pyenv uninstall 3.x.x
pyenv uninstall miniconda3.x.x
pyenv virtualenv-delete my-env
```

## 3. Setting MySQL Server Docker Container

```bash
# Pull the latest MySQL docker image (https://store.docker.com/images/mysql)
docker pull mysql:8.0.22      # check available tags for more information

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
-d mysql:8.0.22             # docker mysql image and tag
                                      # Note: no bash here

```

## 4. Building app using Dockerfile

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

## 5. Creating environment package list

```bash
# create packgage list files
pip list --format=freeze > pip_pkgs.txt
conda list --explicit > conda_pkgs.txt

# create new environment using package list files
conda create --name NEWENV --file conda_pkgs.txt
# or conda create --prefix /path/to/project/venv python==3.x.x
conda activate NEWENV
pip install -r pip_pkgs.txt

```

## 6. Installation of JupyterLab extensions and setting

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
# jupyter labextension install jupyterlab_tensorboard

# ipywidgets
pip install ipywidgets
jupyter nbextension enable --py --user widgetsnbextension

# knowledgelab is outdated, should not install
# pip install knowledgelab
# jupyter labextension install knowledgelab

# itkwidgets
pip install itkwidgets
jupyter labextension install jupyter-matplotlib jupyterlab-datawidgets itkwidgets
# using
# from itkwidgets import view
# view(image)

# SOS
conda install jupyterlab-sos -c conda-forge
jupyter labextension install transient-display-data
jupyter labextension install jupyterlab-sos

# Jupyter commands, no need
# pip install jupyterlab_commands
# jupyter labextension install jupyterlab_commands
# jupyter serverextension enable --py --user jupyterlab_commands

# jupytext
pip install jupytext

# Jupiter lab sql is outdated, should not install
# pip install jupyterlab_sql
# jupyter serverextension enable jupyterlab_sql --py --user

# Go to definition
jupyter labextension install @krassowski/jupyterlab_go_to_definition

# Language server
pip install jupyter-lsp
jupyter labextension install @krassowski/jupyterlab-lsp
pip install python-language-server
# R -e 'install.packages("languageserver")'

# Error, should not install
# jupyter labextension install jupyterlab-drawio

# Latex
pip install jupyterlab_latex
jupyter labextension install @jupyterlab/latex
jupyter serverextension enable --py --user jupyterlab_latex

# Jupyter Lab Code Formatter
pip install autopep8 pylint
# pip install rpy2
# R -e 'install.packages("formatR", repos = "http://cran.rstudio.com")'
# R -e 'install.packages("styler")'
jupyter labextension install @ryantam626/jupyterlab_code_formatter
pip install jupyterlab_code_formatter
jupyter serverextension enable --py --user jupyterlab_code_formatter
# using
# %load_ext rpy2.ipython
# library(formatR)
# sessionInfo()
# library("styler")

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
jupyter labextension list
```

## 7. Installation of other kernels in JupyterLab

```bash
# Install Apache Spark Scala kernel
# Prerequirement of Java installation and Apache Spark download
pip install toree
jupyter toree install --spark_home=~/Downloads/spark-3.0.1-bin-hadoop2.7.tgz

# Bash kernel
# pip install ipykernel
pip install bash_kernel
python3 -m bash_kernel.install

# R kernel
# conda install r-base r-essentials
# conda install -c r r-irkernel
# R
# install.packages('IRkernel')
# IRkernel::installspec()

# C kernel
# pip install jupyter-c-kernel
# install_c_kernel --user

# Kernel check
jupyter kernelspec list
jupyter kernelspec remove "kernel-name"
```

## 8. Setting JupyterLab

Go to Settings/Advanced Settings Editor:

Terminal:

```bash
{
    "fontSize": 15,
    "lineHeight": 1.2,
    "scrollback": 200,
    "shutdownOnClose": true
}
```

Text editor:

```bash
{
    "editorConfig": {
        "autoClosingBrackets": true,
        "fontFamily": null,
        "fontSize": 15,
        "lineHeight": 1.2,
        "lineNumbers": true,
        "lineWrap": "on",
        "matchBrackets": true,
        "readOnly": false,
        "insertSpaces": true,
        "tabSize": 4,
        "wordWrapColumn": 80,
        "rulers": [],
        "codeFolding": true
    }
}
```

Language Server:
```bash
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
```

JupyterLab Code Formatter:
```bash
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
```

Go to /Users/you/.config, create pycodestyle file, insert content below

```bash
[pycodestyle]
count = False
ignore = E226,E302,E41,E402,E703
max-line-length = 160
statistics = True
```
