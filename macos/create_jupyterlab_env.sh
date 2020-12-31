pip install -U pip setuptools wheel
conda install -c conda-forge pandas -y
conda install -c conda-forge matplotlib -y
conda install -c conda-forge seaborn -y
conda install -c conda-forge jupyterlab==2.2.2 -y
conda install -c conda-forge scikit-learn -y
conda install -c conda-forge autopep8 -y
conda install -c conda-forge pylint -y
conda install -c conda-forge pytest -y
conda install -c conda-forge sphinx -y
conda install -c conda-forge tensorflow-datasets -y
conda install -c conda-forge tensorflow -y
pip install -r ~/projects/environments/macos/pip_requirements.txt
pip install nodeenv
nodeenv -p
jupyter labextension install @jupyter-widgets/jupyterlab-manager
# jupyter labextension install jupyterlab_spark
jupyter labextension install @jupyterlab/toc
jupyter nbextension enable --py --user widgetsnbextension
jupyter labextension install jupyter-matplotlib jupyterlab-datawidgets itkwidgets
jupyter labextension install @krassowski/jupyterlab_go_to_definition
jupyter labextension install @krassowski/jupyterlab-lsp
# jupyter labextension install @jupyterlab/latex
# jupyter serverextension enable --py --user jupyterlab_latex
jupyter labextension install @ryantam626/jupyterlab_code_formatter
jupyter serverextension enable --py --user jupyterlab_code_formatter
# jupyter labextension install @jupyterlab/debugger
# jupyter toree install --spark_home=~/Downloads/spark-3.0.1-bin-hadoop2.7.tgz
# python -m bash_kernel.install
# install_c_kernel --user
jupyter lab clean
jupyter lab build
