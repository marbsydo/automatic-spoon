cd ../webapp/www
port=8080
echo Launching test server on port $port
python -m http.server $port
