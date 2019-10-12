#!/bin/bash

echo -e 'Installing requirements. \n'
# install requirements
pip install -r requirements.txt

# run python scripts
echo -e 'Running python scripts. \n'

echo -e 'Running: balance sheet \n'
python src/balance_sheet.py
echo -e 'Finished: balance sheet \n'

echo -e 'Running: income statement \n'
python src/income_statement.py
echo -e 'Finished: income statement \n'

echo -e 'Running: cash flow \n'
python src/cash_flow.py
echo -e 'Finished: cash flow \n'

echo -e "Now you're done! Grab some beers!"