git config --global user.email "119784d4@mozej.com"      
git config --global user.name "t2sae93o"

sudo /etc/init.d/nginx start
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

