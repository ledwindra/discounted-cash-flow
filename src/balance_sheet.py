import os
import pandas
from multiprocessing import Pool, cpu_count


def get_company():
    """
    Returns file name for balance sheet (coded as "2").
    """

    company_list = [x for x in os.listdir('financial-statements/') if x.endswith('2.csv')]

    return company_list


def get_ticker_code():
    """
    Returns a list of ticker code which consists of four letter. It is derived from the first four letter from the file names in the company_list function.
    """

    company_list = get_company()

    ticker_code = []
    for ticker in company_list:
        ticker_code.append(ticker[: 4])

    return pandas.DataFrame({'ticker_code': ticker_code})


def get_dataframe(company_list):
    """
    Reads csv files and stores them in DataFrame format.
    """

    return pandas.read_csv(os.getcwd() + '/financial-statements/{}'.format(company_list))

def get_column_name():
    """
    Returns a list of columns needed. They are hard-coded for practical purpose because there may be unnecessary columns for the analysis.
    """

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


if __name__ == "__main__":

    # read csv files using multiprocessing to increase speed
    dfs = Pool(cpu_count() - 1).map(get_dataframe, get_company())

    # concat files into a single DataFrame
    df = pandas.concat(dfs, sort=False).reset_index(drop=True)

    # merge ticker_code into the DataFrame
    df = pandas.merge(df, get_ticker_code(), how='inner', left_index=True, right_index=True)

    # select only necessary variables
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

    # rename variables into English
    df.columns = get_column_name().values()

    # save files into a .csv format and remove its index numbers
    df.to_csv(os.getcwd() + '/sample-output/balance-sheet.csv', index=False)
