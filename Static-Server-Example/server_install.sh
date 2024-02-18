#create pythadmn user
sudo useradd --create-home pythadmn
sudo usermod --shell /bin/bash pythadmn

#copy python server app to appropriate folder
sudo cp app.py /home/pythadmn

sudo su - pythadmn -c "mkdir public"

sudo cp public/index.html /home/pythadmn/public

#copy service file to appropriate folder
sudo cp python_server.service /etc/systemd/system/python_server.service

#reload to activate new service
sudo systemctl daemon-reload

#start python server
sudo systemctl start python_server
