# Generate HTML
pushd tools
python gensite.py
popd

# Generate CSS
sass --update scss/:webapp/www/static/css/ --style expanded

# Run test server
pushd tools
./server.sh
popd
