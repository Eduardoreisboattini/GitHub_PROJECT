scope = ['https://www.googleapis.com/auth/spreadsheets']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)
sheet = client.open('Your Google Sheet Name').sheet1
#Note: Before using these code snippets, you need to set up the Google Sheets API and obtain the necessary credentials. Replace 'Your Google Sheet Name' with the actual name of your Google Sheet and 'credentials.json' with the path to your credentials file.
#These code snippets provide a starting point for working with the Google Sheets API and performing various operations. Feel free to modify them to suit your specific requirements.