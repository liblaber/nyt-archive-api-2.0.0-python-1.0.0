# Article

**Properties**

| Name             | Type             | Required | Description                                                                  |
| :--------------- | :--------------- | :------- | :--------------------------------------------------------------------------- |
| abstract         | str              | ❌       | Document abstract.                                                           |
| lead_paragraph   | str              | ❌       | Lead paragraph.                                                              |
| web_url          | str              | ❌       | Article URL.                                                                 |
| snippet          | str              | ❌       |                                                                              |
| print_page       | int              | ❌       | Page in print (e.g. 1).                                                      |
| print_section    | str              | ❌       | Section in print (e.g. A).                                                   |
| source           | str              | ❌       |                                                                              |
| multimedia       | List[Multimedia] | ❌       |                                                                              |
| headline         | Headline         | ❌       |                                                                              |
| keywords         | List[Keyword]    | ❌       |                                                                              |
| pub_date         | str              | ❌       | Publication date.                                                            |
| document_type    | str              | ❌       | Document type (article, multimedia).                                         |
| news_desk        | str              | ❌       | Desk in the newsroom that worked on the story (Foreign, Metro, Sports, ...). |
| section_name     | str              | ❌       | Section that the article appeared in (New York, Sports, World, ...).         |
| subsection_name  | str              | ❌       |                                                                              |
| byline           | Byline           | ❌       |                                                                              |
| type_of_material | str              | ❌       | Type of asset (Correction, News, Op-Ed, Review, Video, ...).                 |
| \_id             | str              | ❌       |                                                                              |
| word_count       | int              | ❌       | Number of words in the article.                                              |
| uri              | str              | ❌       | Uniquely identifies an asset.                                                |
