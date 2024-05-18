import pickle
from ML_Pipeline.utils import read_data, merge_dataset,drop_col, null_values
from scipy.stats import zscore
import boto3
from io import StringIO
import os

# Use raw string literal or escape backslashes
model_path = r'C:\classification algorithm for digital transformation\mldep-classification-banking\banking-based-classification\banking-classification\FlaskApplication\output\finalized_model.sav'

# Load the model
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)
    
import pandas as pd

s3_resource = boto3.resource('s3', region_name='us-east-1')
s3_client = boto3.client('s3', region_name='us-east-1')


def predictor():
    data1 = pd.read_csv("C:\classification algorithm for digital transformation\mldep-classification-banking\banking-based-classification\banking-classification\FlaskApplication\input\Data1.csv")
    data2 = pd.read_csv("C:\classification algorithm for digital transformation\mldep-classification-banking\banking-based-classification\banking-classification\FlaskApplication\input\Data2.csv")
    final_data = merge_dataset(data1,data2,join_type='inner',on_param = 'ID')
    final_data = drop_col(final_data,['ID','ZipCode','Age'])
    final_data = null_values(final_data)
    if "LoanOnCard" in list(final_data.columns):
        final_data.drop(['LoanOnCard'],axis=1)
    XScaled  = final_data.apply(zscore)
    predictions = model.predict(XScaled).tolist()
    return predictions

def pre_process(s3_path):
    response = s3_client.get_object(
        Bucket=os.environ.get("BUCKET_NAME"), Key=s3_path)
    print("CONTENT TYPE: " + response['ContentType'])
    print(response)
    TESTDATA = StringIO(response['Body'].read().decode("utf-8"))
    dataset = pd.read_csv(TESTDATA)
    return dataset