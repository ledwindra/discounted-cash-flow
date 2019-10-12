

```python
import os
import pandas
```


```python
company_profile = [x for x in os.listdir('financial-statements/') if x.endswith('1.csv')]
```


```python
dfs = []
for i in company_profile:
    dfs.append(pandas.read_csv(os.getcwd() + '/financial-statements/' + i))
```


```python
df = pandas.concat(dfs, sort=False).reset_index(drop = True)
```


```python
def get_column():
    
    column_name = dict({
        'Nama entitas': 'company_name',
        'Kode entitas': 'ticker_code',
        'Industri utama entitas': 'industry',
        'Sektor': 'sector',
        'Subsektor': 'subsector',
        'Informasi pemegang saham pengendali': 'controlling_shareholder_info',
        'Jenis entitas': 'entity_type',
        'Periode penyampaian laporan keuangan': 'period',
        'Mata uang pelaporan': 'currency',
        'Kurs konversi pada tanggal pelaporan jika mata uang penyajian selain rupiah': 'fx_rate',
        'Pembulatan yang digunakan dalam penyajian jumlah dalam laporan keuangan': 'rounding',
        'Jenis opini auditor': 'auditor_opinion',
        'Auditor tahun berjalan': 'auditor_name'
    })
    
    return column_name
```


```python
df = df.loc[:, df.columns.isin([
    'Nama entitas',
    'Kode entitas',
    'Industri utama entitas',
    'Sektor',
    'Subsektor',
    'Informasi pemegang saham pengendali',
    'Jenis entitas',
    'Periode penyampaian laporan keuangan',
    'Mata uang pelaporan',
    'Kurs konversi pada tanggal pelaporan jika mata uang penyajian selain rupiah',
    'Pembulatan yang digunakan dalam penyajian jumlah dalam laporan keuangan',
    'Jenis opini auditor',
    'Auditor tahun berjalan'
])]
```


```python
df.columns = get_column().values()
```


```python
df.to_csv(os.getcwd() + '/output/company-profile.csv', index = False)
```
