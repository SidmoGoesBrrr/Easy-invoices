import pandas as pd
from datetime import date
from zocrypt import decrypter
from trycourier import Courier
import os
key = os.environ["sidkey"]

auth = decrypter.decrypt_text('my encrypted auth token made using encrypt_auth.py', key)

SHEET_ID="1UWT83GYsDvtabgTPZH7L9M-eT4fStvavwmPbVngAc5c"
SHEET_NAME="Sheet1"
URL=f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

client = Courier(auth_token=auth)

def read_data(url):
    parse_dates=["due_date","reminder_date"]
    df=pd.read_csv(url,parse_dates=parse_dates)
    return df

def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (present >= row["reminder_date"].date()) and (row["has_paid"] == "no"): 
            receiver_email=row["Email"],
            name=row["Name"],
            due_date=row["due_date"].strftime("%d, %b %Y"),  
            invoice_no=row["invoice_no"],
            amount=row["Amount"],


            resp=client.send_message(
            message={
                "brand_id": "69MRB0BK80MPBCNXW919N1KRBBNN",
                "template": "4JPR3NPZK84AWWQ2RK5P4CM54KD2",
                "to": {
                "email": receiver_email[0],
                },
                "data": {
                "Invoice_ID": invoice_no[0],
                "name": name[0],
                "amount": amount[0],
                "invoice_no": invoice_no[0],
                "due_date": due_date[0],
                },
            }
            )
            print(resp['requestId'])
            email_counter += 1
    return f"Total Emails Sent: {email_counter}"

df = read_data(URL)
result = query_data_and_send_emails(df)
print(result)
