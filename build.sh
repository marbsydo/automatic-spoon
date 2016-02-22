# Generate HTML
pushd tools
python gensite.py
popd

# Generate CSS
sass --update scss/:webapp/www/static/css/ --style expanded
#sass --update scss/:webapp/www/static/css/ --style compressed

# Generate docker image
pushd webapp
docker build -t sample-website .

# Generate ZIP
zip ../webapp.zip -r * .[^.]*
popd
