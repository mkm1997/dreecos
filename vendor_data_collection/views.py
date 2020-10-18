from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect, HttpResponse
from .models import Vendor,Submitters,GeoLocation,Menu,VendorImage

FORM_DATA={
    'user_type':'',
    'name':'',
    'phone':'',
    'availability':'',
    'vendor_type':'',
    'paytm':'',
    'lat':[],
    'long':[],
    'pin':[],
    'start_hour':[],
    'start_min':[],
    'start_type':[],
    'end_hour':[],
    'end_min':[],
    'end_type':[],
    'hygeine_rating':'',
    'taste_rating':'',
    'menu':{},
    'files':''
}

vendor_instance=''
# Create your views here.

def index(request):
    user_form=forms.user_form()

    if request.method=='POST':
        user_form=forms.user_form(request.POST)
        if user_form.is_valid():
            FORM_DATA['user_type']=user_form.data.__getitem__('user')
            return HttpResponseRedirect('/vendor_data/add/p1/')
        else:
            print(user_form.errors)

    return render(request,'vendor_data/user.html',{'form':user_form})

def add_vendor_p1(request):
    add_vendor_form=forms.add_vendor_form_p1()
    if request.method=='POST':
        add_vendor_form=forms.add_vendor_form_p1(request.POST)
        if add_vendor_form.is_valid():
            FORM_DATA['name']=add_vendor_form.data.__getitem__('name')
            FORM_DATA['phone']=add_vendor_form.data.__getitem__('phone')
            FORM_DATA['availability']=add_vendor_form.data.__getitem__('availability')
            FORM_DATA['vendor_type']=add_vendor_form.data.__getitem__('vendor_type')
            FORM_DATA['paytm']=add_vendor_form.paytm_available = request.POST.get('paytm_available', 'off')
            return HttpResponseRedirect('/vendor_data/add/p2/')

    return render(request,'vendor_data/add.html',{'form':add_vendor_form})

def add_vendor_p2(request):
    add_vendor_locations_form=forms.add_vendor_form_p2()

    if request.method=='POST':
        add_vendor_locations_form=forms.add_vendor_form_p2(request.POST)

        if add_vendor_locations_form.is_valid():
            for i in range(10):
                lat_name='Latitude'+str(i)
                long_name='Longitude'+str(i)
                pin_name='Pin'+str(i)
                start_hour_name='StartHour'+str(i)
                start_minute_name='StartMinute'+str(i)
                start_type_name='StartType'+str(i)
                end_hour_name='EndHour'+str(i)
                end_minute_name='EndMinute'+str(i)
                end_type_name='EndType'+str(i)

                data={'lat':[],'long':[],'pin':[],'start_hour':[],'start_min':[],'start_type':[],'end_hour':[],'end_min':[],'end_type':[]}
                data['lat']=add_vendor_locations_form.data.__getitem__(lat_name)
                data['long']=add_vendor_locations_form.data.__getitem__(long_name)
                data['pin']=add_vendor_locations_form.data.__getitem__(pin_name)
                data['start_hour']=add_vendor_locations_form.data.__getitem__(start_hour_name)
                data['start_min']=add_vendor_locations_form.data.__getitem__(start_minute_name)
                data['start_type']=add_vendor_locations_form.data.__getitem__(start_type_name)
                data['end_hour']=add_vendor_locations_form.data.__getitem__(end_hour_name)
                data['end_min']=add_vendor_locations_form.data.__getitem__(end_minute_name)
                data['end_type']=add_vendor_locations_form.data.__getitem__(end_type_name)

                if data['lat']!='' and data['long']!='' and data['pin']!='':
                    FORM_DATA['lat'].append(data['lat'])
                    FORM_DATA['long'].append(data['long'])
                    FORM_DATA['pin'].append(data['pin'])
                    FORM_DATA['start_hour'].append(data['start_hour'])
                    FORM_DATA['start_min'].append(data['start_min'])
                    FORM_DATA['start_type'].append(data['start_type'])
                    FORM_DATA['end_hour'].append(data['end_hour'])
                    FORM_DATA['end_min'].append(data['end_min'])
                    FORM_DATA['end_type'].append(data['end_type'])
            if FORM_DATA['vendor_type']=='street-food' or FORM_DATA['vendor_type']=='drinks':
                return HttpResponseRedirect('/vendor_data/add/p3/')
            elif FORM_DATA['vendor_type']=='vegetables':
                return HttpResponseRedirect('/vendor_data/finalize/')
            else:
                return HttpResponseRedirect('/vendor_data/add/p4/')

    return render(request,'vendor_data/add_location.html',{'form':add_vendor_locations_form})

def add_vendor_p3(request):

    add_rating_form=forms.add_vendor_form_p3()

    if request.method=='POST':
        add_rating_form=forms.add_vendor_form_p3(request.POST)
        if(add_rating_form.is_valid()):
            FORM_DATA['hygeine_rating']=add_rating_form.data.__getitem__('hygeine_rating')
            FORM_DATA['taste_rating']=add_rating_form.data.__getitem__('taste_rating')

            return HttpResponseRedirect('/vendor_data/add/p4/')


    return render(request,'vendor_data/add_rating.html',{'form':add_rating_form})


def add_vendor_p4(request):

    if request.method=="POST":
        menu_form_data=request.POST
        categories={}
        for i in menu_form_data:
            if "cat" in i:
                categories[menu_form_data.get(i)]={}
            elif 'item_price' in i:
                arr=i.split("-")
                id=arr[1]
                category_identifier=menu_form_data.get("cat"+arr[0].replace("item_price",""))
                categories[category_identifier][id]['price']=menu_form_data.get(i)
            elif 'item' in i:
                arr = i.split("-")
                id = arr[1]
                category_identifier = menu_form_data.get("cat" + arr[0].replace("item", ""))
                categories[category_identifier][id]={}
                categories[category_identifier][id]['item']=menu_form_data.get(i)
        FORM_DATA['menu']=categories
        return HttpResponseRedirect('/vendor_data/finalize/')



    return render(request,'vendor_data/add_menu.html')

def add_vendor_p5(request):

    if request.method=='POST':
        vendor_image=VendorImage(
            vendor_id=vendor_instance,
            image=request.FILES['file']
        )
        vendor_image.save()
        return render(request,'vendor_data/success.html')

    return render(request,'vendor_data/add_image.html')

def finalize(request):

    data={}
    data['name']=FORM_DATA['name']
    data['phone']=FORM_DATA['phone']
    data['vendor_type']=FORM_DATA['vendor_type']
    data['availability']="Yearly" if FORM_DATA['availability']=='year' else "Seasonal"
    data['paytm']="Available" if FORM_DATA['paytm']=="on" else "Not Available"
    pos_data=[]
    for i in range(len(FORM_DATA['lat'])):
        d=dict()
        d['lat']=FORM_DATA['lat'][i]
        d['long']=FORM_DATA['long'][i]
        d['pin']=FORM_DATA['pin'][i]
        d['start']=FORM_DATA['start_hour'][i]+":"+FORM_DATA['start_min'][i]+" "+FORM_DATA['start_type'][i]
        d['end']=FORM_DATA['end_hour'][i]+":"+FORM_DATA['end_min'][i]+" "+FORM_DATA['end_type'][i]
        pos_data.append(d)
    data['pos_data']=pos_data
    data['hygeine']=FORM_DATA['hygeine_rating']
    data['taste']=FORM_DATA['taste_rating']
    data['files']=FORM_DATA['files']
    menu=dict()
    for i in FORM_DATA['menu']:
        tmp=[]
        for j in FORM_DATA['menu'][i]:
            tmp.append(FORM_DATA['menu'][i][j])
        menu[i]=tmp
    data['menu']=menu

    return render(request,'vendor_data/finalize.html',{'data':data})


def save(request):
    global vendor_instance
    vendor=Vendor(
        name=FORM_DATA['name'],
        phone=FORM_DATA['phone'],
        availability=FORM_DATA['availability'],
        paytm_available=True if FORM_DATA['paytm']=="on" else False,
        vendor_type=FORM_DATA['vendor_type'],
        hygeine_rating=FORM_DATA['hygeine_rating'],
        taste_rating=FORM_DATA['taste_rating'],
    )
    vendor.save()
    vendor_instance=vendor
    sbtr=Submitters(
        submitter=FORM_DATA['user_type'],
        vendor_id=vendor
    )
    sbtr.save()
    for i in range(len(FORM_DATA['lat'])):
        geoloc=GeoLocation(
            vendor_id=vendor,
            lat=FORM_DATA['lat'][i],
            long=FORM_DATA['long'][i],
            pin=FORM_DATA['pin'][i],
            start=FORM_DATA['start_hour'][i]+":"+FORM_DATA['start_min'][i]+" "+FORM_DATA['start_type'][i],
            end=FORM_DATA['end_hour'][i]+":"+FORM_DATA['end_min'][i]+" "+FORM_DATA['end_type'][i]
        )
        geoloc.save()
    for i in FORM_DATA['menu']:
        for j in FORM_DATA['menu'][i]:
            menu=Menu(
                vendor_id=vendor,
                category=i,
                item=FORM_DATA['menu'][i][j]['item'],
                price=FORM_DATA['menu'][i][j]['price']
            )
            menu.save()
    return HttpResponseRedirect('/vendor_data/add/p5/')
