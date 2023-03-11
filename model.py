


from sec_api import QueryApi
from sec_api import ExtractorApi

api_key = "b8113d497aa775cb50186f7f03c97c7e8b3158734705787264d31e7f627dc6db"



# Creating a new instance of the queryapi 

queryapi = QueryApi(api_key)
extractorApi = ExtractorApi(api_key)

base_query = {

  "query": { 
      "query_string": { 
          "query": "PLACEHOLDER", # this will be set during runtime 
          "time_zone": "America/New_York"
      } 
  },
  "from": "0",
  "size": "10", # dont change this
  # sort returned filings by the filedAt key/value
  "sort": [{ "filedAt": { "order": "desc" } }]
}

def getURL(ticker,year = 2023):

    universe_query = "ticker:{ticker} AND ".format(ticker = ticker) + \
      "filedAt:[{year}-01-01 TO {year}-12-31] AND ".format(year = year) + \
      "formType:\"10-K\""
    base_query["query"]["query_string"]["query"] = universe_query
    response = queryapi.get_filings(base_query)
    urls_list = list(map(lambda x: x["linkToFilingDetails"], response["filings"]))
    
    print(year)
    if (len(urls_list) == 0):
        return getURL(ticker,year-1)
        
    else:
        url = urls_list[-1] 
        
        return url
    
def getItem(url,item = '1A'):
    section_text = extractorApi.get_section(url, item, "html")
    return section_text

def convertToModelInput(text):
    import re
    from bs4 import BeautifulSoup
    
    start_condition1 = 'font-weight:700;line-height:120%">'
    start_condition2 = 'font-weight:400;line-height:120%">'
    end_condition1 = '</span></div>'
    end_tag = '</span>'
    #pattern = re.compile(start_tag + '(.*?)' + end_tag, re.DOTALL)
    pattern = re.compile('('+start_condition1+'|'+start_condition2+')(.*?)'+end_condition1)
    matches = pattern.findall(text)
    
    output = extractText(matches)
    
    return output
   
def extractText(matches):
    output = []
    currentText = ""
    for block in matches:
        font_weight = int(block[0][12])
        
        
        if font_weight == 7:
           output.append(currentText)
           currentText = ""
           output.append("*"+block[1])
        elif font_weight == 4:
            currentText += block[1]
        
    if(currentText):
        output.append(currentText)

    output = [cell for cell in output if cell != ""]
    outputWithoutHTML = []
    from bs4 import BeautifulSoup
    for cell in output:
        parser = BeautifulSoup(cell,"html.parser")
        text = parser.get_text()
        outputWithoutHTML.append(text)
    return outputWithoutHTML



def renderReportOnPage(ticker):
    url = getURL(ticker)
    text = getItem(url)
    cells = convertToModelInput(text)
    
    html_string = ""

    for entry in cells:
        if entry.startswith("*"):
            html_string += f"<strong>{entry[1:]}</strong>\n"
        else:
            html_string += entry+"\n"
    return html_string

print(renderReportOnPage("AAPL"))

'''
from test import magic

for shit in output:
    if shit[0] == "*":
        print(shit[1:])
        continue
    if shit is None:
        continue
    summaryText = magic(shit)[0]['summary_text']
    print(summaryText)
'''

'''
print(cells[0][1])
for idx,x in enumerate(cells):
    print(x[1])
    print()
'''