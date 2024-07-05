# ArchiveService

A list of all methods in the `ArchiveService` service. Click on the method name to view detailed information about that method.

| Methods                                           | Description                                                                                                                                                                            |
| :------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_by_year_month_json](#get_by_year_month_json) | Pass in year and month and get back JSON with all articles for that month. The response can be big (~20 megabytes) and contain thousands of articles, depending on the year and month. |
|  |

## get_by_year_month_json

Pass in year and month and get back JSON with all articles for that month. The response can be big (~20 megabytes) and contain thousands of articles, depending on the year and month.

- HTTP Method: `GET`
- Endpoint: `/{year}/{month}.json`

**Parameters**

| Name  | Type | Required | Description     |
| :---- | :--- | :------- | :-------------- |
| year  | int  | ✅       | Year: 1851-2019 |
| month | int  | ✅       | Year: 1-12      |

**Return Type**

`GetByYearMonthJsonOkResponse`

**Example Usage Code Snippet**

```python
from nytarchives_sdk import NytarchivesSdk, Environment

sdk = NytarchivesSdk(
    api_key="",
    base_url=Environment.DEFAULT.value
)

result = sdk.archive.get_by_year_month_json(
    year=2018,
    month=9
)

print(result)
```
