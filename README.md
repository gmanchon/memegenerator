
DE day 1 recap

# memegenerator

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
