from django.shortcuts import render
import requests
import xmltodict
import json
from zeep import Client
# from django.utils.safestring import SafeString


def home(request):
    url = 'http://dev.usbooking.org/us/UnitedSolutions?wsdl'

    # headers = {'content-type': 'application/soap+xml'}
    headers = {'content-type': 'text/xml'}

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
