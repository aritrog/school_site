echo ----------------------------
echo killing old docker processes
echo ----------------------------
sudo docker-compose rm -fs

echo ----------------------------
echo building and running docker containers
echo ----------------------------
sudo docker-compose up --build -d
