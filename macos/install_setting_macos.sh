# install homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# install wget
brew install wget

# install iTerm2
brew install --cask iterm2

# install git
brew install git
chsh -s $(which git)
git config --global user.name "phuong phan"
git config --global user.email "p.h.phan2006@gmail.com"
touch ~/.gitignore
git config --global core.excludesfile ~/.gitignore
git config --global core.editor vim

# install zsh
brew install zsh
chsh -s $(which zsh)

# install oh my zsh:
git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh

# install Powerline fonts:
git clone https://github.com/powerline/fonts.git --depth=1
cd fonts
./install.sh
cd ..
rm -rf fonts

# install oh my zsh plugins
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone git@github.com:zsh-users/zsh-completions.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-completions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# install jdk
brew install --cask oracle-jdk
sudo ln -sfn /usr/local/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

# install VSCode
brew install --cask visual-studio-code

# install PyCharm CE
brew install --cask pycharm-ce

# install Docker CE
brew install --cask docker

# install pyenv
brew install pyenv

# install virtualenv
brew install pyenv-virtualenv

# install pipenv
brew install pipenv

# install R
brew install --cask xquartz
brew install r
brew install --cask rstudio

# install others
brew install --cask slack
brew install --cask zoom

brew upgrade
brew update
brew cleanup
