from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "15f414e140msh6dc384f3d80e80ap1f159cjsna21d4f94ac44"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def helloworldview(request):
   mylist = []
   noofresults = int(response['results'])
   for x in range(0,noofresults):
       mylist.append(response['response'][x]['country'])
   if request.method == "POST":
      selectedcountry = request.POST['selectedcountry']
      noofresults = int(response['results']) 
      for x in range(0,noofresults):
        if (selectedcountry == response['response'][x]['country']):
            new = str(response['response'][x]['cases']['new'])
            active = str(response['response'][x]['cases']['active'])
            critical = str(response['response'][x]['cases']['critical'])
            recovered = str(response['response'][x]['cases']['recovered'])
            total = str(response['response'][x]['cases']['total'])
            deaths = int(total) - int(active) - int(recovered)
      context = {'selectedcountry' : selectedcountry,'mylist' : mylist,'new' : new,'active' : active,'critical' : critical,'recovered' : recovered,'total' : total,'deaths' : deaths}
      return render(request,'helloworld.html',context)
  
   context = {'mylist' : mylist}
   return render(request,'helloworld.html',context)