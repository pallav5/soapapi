import requests
url="http://www.dneonline.com/calculator.asmx?wsdl"
#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}
body = """<soapenv:Envelope  xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:book="http://booking.us.org/">    <soapenv:Header/>    <soapenv:Body>       <book:SectorCode>          <strUserId>USERID</strUserId>       </book:SectorCode>    </soapenv:Body> </soapenv:Envelope>"""

response = requests.post(url,data=body,headers=headers)
