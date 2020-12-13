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
# setting GSH keys and git
git config --global user.name "Your Name Here"
git config --global user.email "your_email@youremail.com"
git config --global core.excludesfile ~/.gitignore

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

# install jdk:
brew install --cask oracle-jdk
sudo ln -sfn /usr/local/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
# check jdk
which java

# install VSCode
brew install --cask visual-studio-code

# install PyCharm CE
brew install --cask pycharm-ce

# install Open Office if neccessary
brew install --cask openoffice
```

## 2. Creating python environment using venv

Creating environment using Homebrew is the best way for MacOS. If you need specific version of python which is not provided by Homebrew, then you can choose to download python version you need from www.python.org, then install it.

Homebrew will put python3 into usr/local/opt folder, so it will not replace original python2 and python3 of MacOS. If you choose to install by yourself, your python3 will be installed into usr/local/bin folder, while python2 is still in usr/bin folder. So your python3.x may replace other python3.x version in usr/local/bin folder. I prefer to use Homebrew to install python.

Creating virtual env using Homebrew and anaconda is always my first choice. This part is about how to create env using venv, not anaconda. The venv env will work well in PyCharm because PyCharm has a step to setting virtual env. You just need to go to Python Interpreter and set virtual env by pointing to your env folder. VSCode cannot detect this venv virtual env automatically.

Next part will show how to create env using Homebrew and anaconda. Creating virtual env using anaconda is good for VSCode and JupyterLab. VSCode can detect this conda virtual env automatically.


```bash
# python 3.8.6, current python version of Homebrew
brew install python@3.8

# echo into .zshrc
# see .zshrcorig
echo 'export PATH="/usr/local/opt/python@3.8/bin:$PATH"' >> ~/.zshrc
echo 'export LDFLAGS="-L/usr/local/opt/python@3.8/lib"' >> ~/.zshrc
echo 'export PKG_CONFIG_PATH="/usr/local/opt/python@3.8/lib/pkgconfig"' >> ~/.zshrc

# you may not need these
echo 'export PATH="/usr/local/opt/sqlite/bin:$PATH"' >> ~/.zshrc
echo 'export LDFLAGS="-L/usr/local/opt/sqlite/lib"' >> ~/.zshrc
echo 'export CPPFLAGS="-I/usr/local/opt/sqlite/include"' >> ~/.zshrc
echo 'export PKG_CONFIG_PATH="/usr/local/opt/sqlite/lib/pkgconfig"' >> ~/.zshrc

# check OpenSSL
python3 -c "import ssl; print(ssl.OPENSSL_VERSION)"
# return OpenSSL 1.1.1i

# create virtual env
python3 -m venv ~/path/to/envs/my-env

# activate my-env
source ~/path/to/envs/my-env/bin/activate

# upgrade dependencies
python3 -m pip install -U pip setuptools wheel

# install tensorflow and other packages
pip install -r requirements.txt

# just in case you have Jupyter Notebook
# and you want to have nodejs for Notebook
# install nodejs
# pip install nodeenv
nodeenv -p

# check nodejs
# npm -v
nodejs -v

# build jupyter lab
jupyter lab build

# start jupyter lab
jupyter lab

# close my-env
deactivate
```

## 3. Creating python environment using anaconda

Install anaconda

```bash
brew install --cask anaconda
cd /
usr/local/anaconda3/bin/conda init zsh

# close zsh window, open new window
# you will see
(base) ->
```

Create virtual env

```bash
# create anaconda virtual env at prefered location
conda create --prefix /path/to/project/folder/env-name --file conda_pkgs.txt
# or conda create --prefix /path/to/project/folder/env-name python==3.x.x
conda activate /path/to/project/folder/env-name
# you will see
(/path/to/project/folder/env-name) $

# you may not need this
python3 -m pip install -U pip setuptools wheel

# install other packages
pip install -r pip_pkgs.txt
# or pip install -r requirements.txt

# just in case you have Jupyter Notebook
# and you want to have nodejs for Notebook
# install nodejs
# pip install nodeenv
nodeenv -p

# to come back with local python env
(base) -> conda deactivate

# always be sure which python you are working with
# check python env again
which python3
```

## 4. Creating python environment using pyenv

You will not need this if you already install anaconda, and know how to work with anaconda and Homebrew.
Currently, there is a problem of using pyenv with MacOS Bir Sur ver11.0.1. This command of "pyenv install 3.x.x" failed. So should not use pyenv.

Install pyenv

```bash
# install pyenv using homebrew
brew install pyenv
echo 'if command -v pyenv 1>/dev/null 2>&1; then eval "$(pyenv init -)"; fi' >> ~/.zshrc
source ~/.zshrc

# install virtualenv
brew install pyenv-virtualenv
echo 'if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi' >> ~/.zshrc
source ~/.zshrc
```

Create virtual env

```bash
# using pyenv with virtualenv
pyenv install 3.x.x
pyenv shell 3.x.x  # to make it main python of system
pyenv virtualenv 3.x.x my-env # to create virtual env
cd ~/to_project_folder
# to start my-env automaticaly when cd into project folder
pyenv local my-env # to become env of project
pyenv shell --unset
pyenv uninstall my-env
pyenv uninstall 3.x.x
```

or with miniconda/anaconda

```bash
# pyenv and miniconda
pyenv install miniconda3.x.x
pyenv shell miniconda3.x.x
conda create -n my-env python==3.x.x
conda activate my-env
conda deactivate
pyenv shell —-unset
pyenv uninstall my-env
pyenv uninstall miniconda3.x.x

# or
pyenv shell miniconda3.x.x/envs/my-env
cd /to/project/folder
pyenv local miniconda3.x.x/envs/my-env
```

other pyenv commands

```bash
# other pyenv commands
pyenv install --list
pyenv versions
pyenv virtualenvs
```

## 5. Setting MySQL Server Docker Container

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

## 6. Building app using Dockerfile

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

## 7. Creating environment package list

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

## 8. Installation of JupyterLab extensions and setting

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

## 9. Installation of other kernels in JupyterLab

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

## 10. Setting JupyterLab

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
