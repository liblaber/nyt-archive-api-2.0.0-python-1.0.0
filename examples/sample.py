from nytarchives_sdk import NytarchivesSdk

sdk = NytarchivesSdk(api_key="YOUR_API_KEY")

result = sdk.archive.get_by_year_month_json(year=1993, month=2)

print(result.response)
