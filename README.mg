1. Install selenium and put chromedriver.exe in C:\Users\Programs\Python\Python37

#run tests from command line
#windows
python -m pytest -v -c pytest-dev.ini
#linux
pytest -v -c pytest-dev.ini

#run test report
pytest -v -s --alluredir="reports"
allure serve ./reports