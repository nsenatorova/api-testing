# API Testing Project

Учебный проект по тестированию REST API

### Шаги для установки и запуска проекта
1. Скачать репозиторий
```
git clone git@gitlab.griddynamics.net:nsenatorova/api-testing-project.git
```
2. Установить требуемые пакеты
```
pip install -r requirements.txt
```
3. Запустить тесты
```
python3 -m pytest --alluredir=allure-report
```
4. Сгенерировать отчет allure
```
allure serve allure-report/
```
