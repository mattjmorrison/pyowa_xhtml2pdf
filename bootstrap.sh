rmvirtualenv pisa
mkvirtualenv pisa --python=python2.7 --no-site-packages
workon pisa
pip install -r requirements.txt -i http://localhost:8000/simple
