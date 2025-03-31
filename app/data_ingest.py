import os
import pandas as pd
import dlt
from dotenv import load_dotenv


FILEPATH = rf'https://data.poltekkes-smg.ac.id/dataset/7627060d-81f1-4393-9ec0-c49740efbf6a/resource/c759b693-ac63-431b-aca8-10bee206188d/download/archive-1.zip'

def data_ingest():
    load_dotenv()
    os.environ['DESTINATION__POSTGRES__CREDENTIALS__USERNAME'] = os.environ.get('DB_USERNAME')
    os.environ['DESTINATION__POSTGRES__CREDENTIALS__PASSWORD'] = os.environ.get('DB_PASSWORD')
    os.environ['DESTINATION__POSTGRES__CREDENTIALS__DATABASE'] = os.environ.get('DB_NAME')
    os.environ['DESTINATION__POSTGRES__CREDENTIALS__PORT'] = os.environ.get('PORT')
    os.environ['DESTINATION__POSTGRES__CREDENTIALS__HOST'] = os.environ.get('HOST')

    df = pd.read_csv(FILEPATH, compression='zip')

    pipeline = dlt.pipeline(
        pipeline_name='breast_cancer',
        destination='postgres',
        dataset_name='public'
    )

    pipeline.run(
        data=df,
        table_name='breast_cancer',
        write_disposition='append',
        )

if __name__ == '__main__':
    data_ingest()
