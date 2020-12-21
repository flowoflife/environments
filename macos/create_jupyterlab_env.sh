pip install -U pip setuptools wheel
pip install -r ~/projects/environments/macos/requirements.txt
conda install nodejs==10.13.0 -c conda-forge -y
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install jupyterlab_spark
jupyter labextension install @jupyterlab/toc7
jupyter nbextension enable --py --user widgetsnbextension
jupyter labextension install jupyter-matplotlib jupyterlab-datawidgets itkwidgets
jupyter labextension install @krassowski/jupyterlab_go_to_definition
jupyter labextension install @krassowski/jupyterlab-lsp
jupyter labextension install @jupyterlab/latex
jupyter serverextension enable --py --user jupyterlab_latex
jupyter labextension install @ryantam626/jupyterlab_code_formatter
jupyter serverextension enable --py --user jupyterlab_code_formatter
jupyter labextension install @jupyterlab/debugger
jupyter toree install --spark_home=~/Downloads/spark-3.0.1-bin-hadoop2.7.tgz
python -m bash_kernel.install
install_c_kernel --user
jupyter lab clean
jupyter lab build
