![TeamCity build status](http://188.120.227.87:8111/app/rest/builds/buildType:id:FinalProject_Build/statusIcon.svg)


[![pipeline status](https://gitlab.com/vor.arkadiy/final_project/badges/main/pipeline.svg)](https://gitlab.com/vor.arkadiy/final_project/-/commits/main) 


[![pages-build-deployment](https://github.com/ArkadiyVoronov/Final-project/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/ArkadiyVoronov/Final-project/actions/workflows/pages/pages-build-deployment)


[![Tests build](https://github.com/ArkadiyVoronov/Final-project/actions/workflows/workflow_pytest.yml/badge.svg)](https://github.com/ArkadiyVoronov/Final-project/actions/workflows/workflow_pytest.yml)


[![GitlabSync](https://github.com/ArkadiyVoronov/Final-project/actions/workflows/workflow_gitlabsync.yml/badge.svg)](https://github.com/ArkadiyVoronov/Final-project/actions/workflows/workflow_gitlabsync.yml)

![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)



# Final UI-test Student's Project

## Innopolis University

Final Student's Project for the QA Automation Python Course

Testing app

`https://cypress-tourism-app.herokuapp.com`

Use python 3.8 +

Create and activate virtual environments

`python3 -m venv env`

`source env/bin/activate`

For Windows

`python3 -m venv env`

`env\Scripts\activate`

Run in terminal for install used packages

`pip install -r requirements.txt`

Pre-commit

https://pre-commit.com

`pre-commit run --all-files`

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
