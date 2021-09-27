Projeto criado para o desenvolvimento do Desafio Final do curso de Google Cloud Plataform da Gama Academy em parceria com a Magazine Luiza.

Proposta:
Desenvolvimento de um sistema web utilizando linguagens de Front-end e Back-end.

Instruções para configurar o ambiente e rodar o projeto:

Nos sistemas operacionais MacOs, Windows ou Linux, é possível rodar o projeto num ambiente virtual local. O pré-requisito é ter o python3 instalado na sua máquina.

Para isso, crie o ambiente virtual: python -m venv ambiente_virtual
Ative-o toda vez que desligar a máquina: # Em windows
ambiente_virtual\Scripts\activate    
ambiente_virtual\Scripts\activate.bat

Instalar DJango no ambiente virtual

Suba as alterações iniciais remotamente

Rode o server: python3 manage.py runserver
O projeto estará rodando no http://localhost:8000/

Crie o layout da aplicação

Instale o Jenkins e o configure:
brew install jenkins-lts
brew services start jenkins-lts
sudo nano /usr/local/opt/jenkins-lts/homebrew.mxcl.jenkins-lts.plist

Crie a imagem, tagueie a aplicação e dê docker run:
docker build -t django-kube .
docker tag django-kube mariannesalomao/django-kube:django-kube
docker run django-kube

Instruções para rodar o Kubernetes
São pré-requisitos ter o Kubernetes (kubectl) e o Minikube instalados na sua máquina:
Kubernetes
Minikube

O primeiro passo é baixar a imagem do nosso projeto no dockerhub:

docker pull XXXXXXXXX
E rodá-la na sua máquina:
docker run -d -p 8000:8000 -it samaraborges/XXXXXXX
Em seguida, rodando o terminal na pasta do projeto, é necessário:

iniciar o Kubernetes na máquina

minikube start
pedir para que ele leia o arquivo arquivo criado no projeto

kubectl apply -f deployment.yaml
inclir a imagem no minikube:

docker save XXXXXXX:v1 | (eval $(minikube docker-env) && docker load) e solicitar que ele abra o dashboard

minikube dashboard
Finalmente, quando o dashboard abrir no navegador, escolha a opção "kube-system".

