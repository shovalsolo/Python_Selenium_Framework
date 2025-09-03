#### How to Run the Tests

### Get requirements
1. pip install -r requirements.txt

### to run one test file
2. python -m unittest tests/test_showcase.py

### Run all test files
3. pytest -v --tb=long --capture=no tests/test_showcase.py

4. Run all test files with reports
pytest tests/ --html=reports/report.html --self-contained-html --capture=no -v

5. Run all with reports one line
  pytest --html=reports/full_report.html --self-contained-html -v

6. Run all with reports       test location Python_Selenium_Framework/showcase_framework
pytest tests/ \                                          
  --html=reports/report.html \
  --self-contained-html \
  --capture=no \
  -v


  7. this will generate a report in a new folder with the date

  8. Adding a dev branch