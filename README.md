# Final-project
Test automation project in python, which will show what we have learned during the training

![TeamCity build status](http://188.120.227.87:8111/app/rest/builds/buildType:id:FinalProject_Build/statusIcon.svg)

![Gitlab pipeline status](https://img.shields.io/gitlab/pipeline-status/gitlab.com/vor.arkadiy/final_project?branch=master)


# Final UI-test Student's Project

## Innopolis University

Final Student's Project for the QA Automation Python Course

Purpose of Project:

    Auto-testing of UI the app https://cypress-tourism-app.herokuapp.com using framework Pytest
# TODO: перенести task вниз?
Tasks:

    writing autotests:
        searching of products (positive and negative);
        adding products in the basket;
        in the basket: adding and removing product, deleting product, buying;
    configuring and running test in CI;
    writing test cases;
    receiving reports on tests results.

Testing app

https://cypress-tourism-app.herokuapp.com

Use python 3.8 +

Create and activate virtual environments

for linuxFor Mac OS

python3 -m venv env

source env/bin/activate

For Windows

python3 -m venv env

env\Scripts\activate

Run in terminal for install used packages

pip install -r requirements.txt

Pre-commit

https://pre-commit.com

pre-commit run --all-files

CI - GitHub Actions

python-publish.yml

test.py
Report - pytest-html

For testing with getting report run in terminal

pytest --html=report.html --self-contained-html

Open the actual report (Ctrl+leftclick for opening in other page)






Check list:
 + [ ] Необходимо настроить CI (GitHub Actions). В проекте должен присутствовать файл настроек, который описывают логику взаимодействия с CI

 + [ ] Необходимо настроить линтер (программа, которая проверяет код на соответствие стандартам в соответствии с определенным набором правил), который должен запускаться локально/на стороне travis-ci

 + [ ] К каждому тесту должны присутствовать тест кейсы 
 https://voronov1project.testrail.io/index.php?/projects/overview/1
            
 + [ ] README.md заполнен и содержит актуальную информацию

 + [ ] В файле README.md стоят бейджики GitHub Actions

 + [ ] Доступна инструкция по установке зависимостей

 + [ ] Описано как запустить тесты

 + [ ] Есть информация о цели тестирования и краткое описание проекта

 + [ ] Для тестирования используется фреймворк pytest 

 + [ ] Результатом тестирования является сгенерированный отчет (например, Allure)
