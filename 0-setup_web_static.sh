#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static
name="nginx"
dpkg -s $name &> /dev/null
if [ $? -ne 0 ]
then
    sudo apt-get update
    sudo apt-get install $name
fi
FOLDER=("/data" "/data/web_static" "/data/web_static/releases"
"/data/web_static/shared" "/data/web_static/releases/test")
for val in ${FOLDER[@]};
do
    if [ ! -d $val ]
    then
        sudo mkdir $val
    fi
done
file="/data/web_static/releases/test/index.html"
source="/data/web_static/releases/test/"
symbollink="/data/web_static/current"
sudo echo "This is a test" | sudo tee $file
sudo ln -sf $source $symbollink
sudo chown -hR ubuntu:ubuntu /data
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo nginx -s reload
