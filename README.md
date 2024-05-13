# Execution du projet Python

## 1. Ubuntu

### 1. Télécharger le script d'installation d'Anaconda

wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh

### 2. Installer les paquets de développements

sudo apt-get install libxcb-xinerama0

### 3. Exécuter le script d'installation d'Anaconda

bash Anaconda3-2024.02-1-Linux-x86_64.sh

### 4. Activer l'environnement virtuel dans Anaconda

cd ../..
source /home/user/anaconda3/bin/activate
conda activate

### 5. Initialiser la configuration de conda

conda init

### 6. Installer les packages Python

pip install PyQt6 typing-extensions Self pandas datetime numpy xarray tk pyexcel_ods

### 7. Installer les paquets de développements

sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
sudo apt install qtwayland5

### 8. Executer le programme

python app.py

## 2. Windows

### 1. Installer VSCode

https://code.visualstudio.com

### 2. Installer les packages Python

pip install PyQt6 typing-extensions Self pandas datetime numpy xarray tk pyexcel_ods

### 3. Executer le programme

python app.py

# Mise à jour du projet Python avec Github

## Ubuntu

### 1. Créer un compte Github

https://github.com

### 2. Installer Github

sudo apt update
sudo apt install git

### 3. Configurer Git avec l’adresse mail de l’utilisateur

git config --global user.email "usergmail.com"

Sert à configurer l'adresse e-mail associée aux commits Git au niveau global sur le système de l'utilisateur. Chaque fois que l'utilisateur effectue un commit dans un projet Git, cette adresse e-mail sera utilisée pour identifier l'auteur du commit.

### 4. Générer une nouvelle paire de clés SSH

ssh-keygen -t rsa -b 4096 -C "user@gmail.com"

Permet à l'utilisateur d'authentifier son accès à GitHub de manière sécurisée. Les clés SSH sont utilisées pour établir une connexion sécurisée entre l'utilisateur et les serveurs GitHub, évitant ainsi la nécessité de saisir un mot de passe à chaque fois qu'une opération Git est effectuée.

### 5. Ajouter la clé SSH à l’agent SSH

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

Nécessaire pour que l'agent SSH puisse gérer la clé privée et fournir automatiquement la clé au serveur lors de l'authentification. Cela évite à l'utilisateur de devoir saisir le mot de passe de la clé privée à chaque fois qu'une connexion SSH est établie.

### 6. Copier la clé SSH public dans le presse-papiers

sudo apt install xclip
xclip -sel clip < ~/.ssh/id_rsa.pub

### 7. Ajouter la clé SSH au compte Github

Connectez-vous à votre compte GitHub.
Allez dans Paramètres > Clés SSH et GPG > Nouvelle clé SSH.
Collez la clé que vous avez copiée et enregistrez-la.

### 8. Vérifier la connectivité SSH

ssh -T git@github.com

Pour s'assurer que la clé SSH a été correctement configurée et ajoutée au compte GitHub. Cela permet de vérifier que l'utilisateur peut se connecter avec succès aux serveurs GitHub à l'aide de la clé SSH sans rencontrer d'erreurs d'authentification. Si la connectivité SSH réussit, cela signifie que l'utilisateur est prêt à utiliser Git avec GitHub de manière sécurisée.

### 9. Créer un répertoire pour le futur projet

### 10. Cloner le projet privé

git clone url_projet

### 11. Mettre à jour localement le projet privé

git pull origin main