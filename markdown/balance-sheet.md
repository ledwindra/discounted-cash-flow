

```python
import os
import pandas
```


```python
balance_sheet = [x for x in os.listdir('financial-statements/') if x.endswith('2.csv')]
```


```python
ticker_code = []
for ticker in balance_sheet:
    ticker_code.append(ticker[ : 4])
```


```python
ticker_code = pandas.DataFrame({'ticker_code': ticker_code})
```


```python
dfs = []
for i in balance_sheet:
    dfs.append(pandas.read_csv(os.getcwd() + '/financial-statements/' + i))
```


```python
df = pandas.concat(dfs, sort=False).reset_index(drop = True)
```


```python
df = pandas.merge(ticker_code, df, how = 'inner', left_index = True, right_index = True)
```


```python
def get_column():
    
    column_name = dict({
        'ticker_code': 'ticker_code',
        'Kas dan setara kas': 'cash_and_equivalents',
        'Piutang usaha pihak ketiga': 'account_receivables_third_party',
        'Piutang usaha pihak berelasi': 'account_receivables_related_party',
        'Jumlah aset lancar': 'total_current_assets',
        'Aset tetap': 'fixed_assets',
        'Jumlah aset tidak lancar': 'total_non_current_assets',
        'Jumlah aset': 'total_assets',
        'Jumlah liabilitas jangka pendek': 'total_current_liabilities',
        'Jumlah liabilitas jangka panjang': 'total_non_current_liabilities',
        'Jumlah ekuitas': 'total_equity'
    })
    
    return column_name
```


```python
df = df.loc[:, df.columns.isin([
    'ticker_code',
    'Kas dan setara kas',
    'Piutang usaha pihak ketiga',
    'Piutang usaha pihak berelasi',
    'Jumlah aset lancar',
    'Aset tetap',
    'Jumlah aset tidak lancar',
    'Jumlah aset',
    'Jumlah liabilitas jangka pendek',
    'Jumlah liabilitas jangka panjang',
    'Jumlah ekuitas'
])]
```


```python
df.columns = get_column().values()
```


```python
df.to_csv(os.getcwd() + '/sample-output/balance-sheet.csv', index = False)
```
