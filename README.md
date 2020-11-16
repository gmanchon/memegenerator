
DE day 1 recap

# v1 - memegenerator

code : https://github.com/gmanchon/memegenerator/
prod : https://memegenerator450.herokuapp.com/

create a memegenerator package:

``` bash
wagon-make-package memegenerator
```

link it to several github remotes
explain the difference between remotes, pull, push
add some commits, look at history, use diff, make a PR, merge it

add some code in the package lib
add some tests
create a heroku app that installs and runs the package script using a Procfile
push lib to prod
check the logs, see the package logs

add streamlit to display a page showing the package output
add setup.sh and modify the Procfile to install package and run setup.sh and run streamlit
push to heroku

plug CD to existing github CI
create heroku api key
add it to github key (see exercice)
modify yaml conf with correct padding

push to github, check tests are ok and it then pushes to heroku

(explain virtual env if time remains)

# v2 - 2020-11-16

import requests

https://breaking-bad-quotes.herokuapp.com/v1/quotes

* create a new project using wagon-make-package

* create a package module function
* that calls api and retrieves a breaking bad quote

* create a script that exposes this function

* test the code

* push to github + CI

* create a streamlit page showing the content of the page

* push streamlit page to heroku

``` Procfile
web: pip install . -U && sh setup.sh && streamlit run app.py
```

``` setup.sh
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"${HEROKU_EMAIL_ADDRESS}\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

``` bash
heroku login
heroku create app_name
heroku ps:scale web=1
heroku logs --tail
```

* plug to git CI then to git CD

⚠️CHANGE heroku_app_name in yaml file

``` .github/workflows/pythonpackage.yml
  deploy_heroku:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: akhileshns/heroku-deploy@v3.0.4 # This is the action
      with:
        heroku_api_key: ${{secrets.HEROKU_API_KEY}}
        heroku_app_name: "memegenerator450" # Must be unique in Heroku
        heroku_email: ${{secrets.HEROKU_EMAIL}}
```
