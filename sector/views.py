from django.shortcuts import render
import requests
import xmltodict
import json
from zeep import Client # I couldnt use zeep modules



def home(request):
    url = 'http://dev.usbooking.org/us/UnitedSolutions?wsdl'

    #The headers are important. Most SOAP requests will not work without the correct headers.
    # application/soap+xml is probably the more correct header to use (but this api prefers text/xml
    headers = {'content-type': 'text/xml'}

    #payload
    body = """ <soapenv:Envelope  xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:book="http://booking.us.org/">    <soapenv:Header/>    <soapenv:Body>     
      <book:SectorCode>          <strUserId>USERID</strUserId>       </book:SectorCode>    </soapenv:Body>
       </soapenv:Envelope>   """
    response = requests.post(url, data=body, headers=headers)
    r = response.text
    data = xmltodict.parse(r)

    result = json.dumps(data)

    context = {

        'result': result,

    }

    return render(request, 'home.html', context)
