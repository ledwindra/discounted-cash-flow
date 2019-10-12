#!/bin/bash

echo -e 'Installing requirements. \n'
# install requirements
pip install -r requirements.txt

# run python scripts
echo -e 'Running python scripts. \n'

echo -e 'Running: balance sheet \n'
python src/balance_sheet.py 2017
python src/balance_sheet.py 2018
echo -e 'Finished: balance sheet \n'

echo -e 'Running: income statement \n'
python src/income_statement.py 2017
python src/income_statement.py 2018
echo -e 'Finished: income statement \n'

echo -e 'Running: cash flow \n'
python src/cash_flow.py 2017
python src/cash_flow.py 2018
echo -e 'Finished: cash flow \n'

echo -e "Now you're done! Grab some beers!"