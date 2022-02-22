api_key = "API Key"
from googleapiclient.discovery import build
resource = build("customsearch", 'v1', developerKey=api_key).cse()
x = str(input("What do you want to search?: "))
result = resource.list(q=x, cx = 'Custom Search Engine ID').execute()
for item in result['items']:
    print(item['title'], ":", item['link'])
