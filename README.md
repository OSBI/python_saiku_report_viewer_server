# Saiku Report Viewer Server #
## Python Wrapper ##

This project encapsulates the Saiku Report Viewer Server in a Python module, so
it could be used easily by other Python projects.

## Requirements ##
* Python 3.6 or superior
* pipenv 

## Installation and Usage ##
``` bash
git clone https://github.com/OSBI/python_saiku_report_viewer_server
cd python_saiku_report_viewer_server
pipenv shell
pipenv install
cd src
python -m saiku.main
```
On a browser, open the address `http://localhost:5002` 