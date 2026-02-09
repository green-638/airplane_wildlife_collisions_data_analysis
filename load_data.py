import pandas as pd

def load_data():
    ''' loads dataset into dataframe
    
    Returns:
        dataframe: contains incident year and species name
    '''
    df = pd.read_csv('Public.csv',
                     usecols=['AIRPORT', 'TIME_OF_DAY', 'SKY', 'PHASE_OF_FLIGHT', 'SPECIES', 'INCIDENT_YEAR', 'INCIDENT_MONTH'],
                     na_values=['UNKNOWN'])
    
    # drop rows with N/A values
    df = df.dropna()
    df = df.reset_index(drop=True)
    return df