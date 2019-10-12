import os
import pandas
from multiprocessing import Pool, cpu_count
from sys import argv

YEAR = argv[1]

def get_company():
    """
    Returns file name for cash flow (coded as "3").
    """

    company_list = [x for x in os.listdir('financial-statements/') if x.endswith('{}-Audit-6.csv'.format(YEAR))]

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

def get_column():
    """
    Returns a list of columns needed. They are hard-coded for practical purpose because there may be unnecessary columns for the analysis.
    """

    column_name = dict({
        'Jumlah arus kas bersih yang diperoleh dari (digunakan untuk) aktivitas operasi': 'operating_cash_flow',
        'Jumlah arus kas bersih yang diperoleh dari (digunakan untuk) aktivitas investasi': 'investing_cash_flow',
        'Pembayaran untuk perolehan aset tetap': 'fixed_asset_expenditure',
        'Jumlah arus kas bersih yang diperoleh dari (digunakan untuk) aktivitas pendanaan': 'financing_cash_flow',
        'Kas dan setara kas arus kas, awal periode': 'cash_and_equivalents_beginning',
        'Efek perubahan nilai kurs pada kas dan setara kas': 'fx_rate_effect_on_cash',
        'Kenaikan (penurunan) kas dan setara kas lainnya': 'cash_and_equivalents_changes',
        'Kas dan setara kas arus kas, akhir periode': 'cash_and_equivalents_ending',
        'ticker_code': 'ticker_code'
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
    df = df.loc[:, df.columns.isin(list(get_column().keys()))]

    # rename variables into English
    df.columns = get_column().values()

    # add year column
    df['year'] = YEAR

    # save files into a .csv format and remove its index numbers
    df.to_csv(os.getcwd() + '/sample-output/cash-flow-{}.csv'.format(YEAR), index=False)