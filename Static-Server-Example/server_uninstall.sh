#stop running service
sudo systemctl stop python_server
#remove python server
sudo apt-get remove --purge python_server
#delete user folder relating to pythadmn
sudo userdel pythadmn
sudo rm -rf /home/pythadmn
