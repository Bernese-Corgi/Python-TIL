import requests
from bs4 import BeautifulSoup

json1 = {
            "depth":2,
            "text":"복제",
            "path":"/spanner/docs/reference/standard-sql/mathematical_functions"
          }

array = [
  {
    "idx": 17,
    "path": "/spanner/docs/reference/standard-sql/hash_functions"
  },
  {
    "idx": 18,
    "path": "/spanner/docs/reference/standard-sql/string_functions"
  },
  {
    "idx": 19,
    "path": "/spanner/docs/reference/standard-sql/json_functions"
  },
  {
    "idx": 20,
    "path": "/spanner/docs/reference/standard-sql/array_functions"
  },
  {
    "idx": 21,
    "path": "/spanner/docs/reference/standard-sql/date_functions"
  },
  {
    "idx": 22,
    "path": "/spanner/docs/reference/standard-sql/timestamp_functions"
  },
  {
    "idx": 23,
    "path": "/spanner/docs/reference/standard-sql/debugging_functions"
  },
  {
    "idx": 24,
    "path": "/spanner/docs/reference/standard-sql/net_functions"
  },
  {
    "idx": 25,
    "path": "/spanner/docs/reference/standard-sql/ml-predict"
  },
  {
    "idx": 26,
    "path": "/spanner/docs/reference/standard-sql/functions-and-operators"
  },
  {
    "idx": 27,
    "path": "/spanner/docs/reference/standard-sql/data-definition-language"
  },
  {
    "idx": 28,
    "path": "/spanner/docs/reference/standard-sql/dml-syntax"
  },
]

for item in array:
  print(item)
  base_url = 'https://cloud.google.com'
  path = item['path'] + '?hl=ko'
  filename = '.' + "/".join(item['path'].split('/')[:-1]) + "/" + str(item['idx']) + "".join(item['path'].split('/')[-1]) + '.html'

  page = requests.get(base_url + path)
  soup = BeautifulSoup(page.text, "html.parser")

  h1 = soup.select('h1')
  # wholeToc = soup.select('.devsite-mobile-nav-bottom>.devsite-nav-list')
  # toc = soup.select('.devsite-article .devsite-nav-list')
  devsiteArticleBody = soup.select('.devsite-article-body')

  before = '<!DOCTYPE html>\n<html lang="en">\n   <head>\n      <meta charset="UTF-8">\n      <meta http-equiv="X-UA-Compatible" content="IE=edge">\n      <meta name="viewport" content="width=device-width, initial-scale=1.0">\n      <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/gh/moonspam/NanumSquare@2.0/nanumsquare.css">\n      <link href="https://fonts.cdnfonts.com/css/fantasque-sans-mono" rel="stylesheet">\n      <link rel="stylesheet" href="style.css">\n      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.13.1/styles/vs2015.min.css">\n      <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.2.0/styles/base16/atelier-seaside-light.min.css">\n      <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/highlight.min.js"></script>\n      <script>hljs.initHighlightingOnLoad();</script>\n      <title>Document</title>\n   </head>\n   <body>'
  body = devsiteArticleBody[0]
  after = '</body>\n</html>'
  # print(h1)

  # print(f"{before}{h1[0]}{body}{after}")

  file = open(f"{filename}", 'w', encoding='UTF-8')
  file.write(f"{before}\n{h1[0]}\n{body}\n{after}")
  file.close()