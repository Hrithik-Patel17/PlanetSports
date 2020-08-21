from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
from random import *
from .utils import *
from random import randint
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings

from .checksum import generate_checksum, verify_checksum
from django.views.decorators.csrf import csrf_exempt



# Create your views here.


def sportsClubMembership(request):
    return render(request,"sportsfinal/Sports Club Membership Registration form a Flat Responsive Widget Template __ w3layouts.html")
def loadIndex(request):
    return render(request,"sportsfinal/index.html")

def CricketForm(request):
    return render(request,"sportsfinal/cricket_form.html")    

def VendorRegistrationPage(request):
    return render(request,"sportsfinal/Vendor-Registration.html")

def AddEventpage(request):
    return render(request,"sportsfinal/Add-Event.html")

def loadLoginRegister(request):
    return render(request,"sportsfinal/login-register.html")

def Error404(request):
    return render(request,"sportsfinal/404.html")

def Allfixture(request):
    return render(request,"sportsfinal/all-fixture.html")

def BlogDetailWsound(request):
    return render(request,"sportsfinal/blog-detail-wsound.html")

def BlogDetailWvid(request):
    return render(request,"sportsfinal/blog-detail-wvid.html")

def BlogDetail(request):
    return render(request,"sportsfinal/blog-detail.html")

def BlogGridWls(request):
    return render(request,"sportsfinal/blog-grid-wls.html")

def BlogGridWrs(request):
    return render(request,"sportsfinal/blog-grid-wrs.html")

def BlogGrid(request):
    return render(request,"sportsfinal/blog-grid.html")

def BlogLargeWls(request):
    return render(request,"sportsfinal/blog-large-wls.html")

def BlogLargeWos(request):
    return render(request,"sportsfinal/blog-large-wos.html")
    
def BlogLarge(request):
    return render(request,"sportsfinal/blog-large.html")

def Checkout(request):

    check = ShopD.objects.all()
    print(check)
    return render(request,"sportsfinal/checkout.html",{'check':check})

def ContactUs(request):
    return render(request,"sportsfinal/contact-us.html") 

def FixtureDetail(request):
    return render(request,"sportsfinal/fixture-details.html")

def FixtureList(request):
    return render(request,"sportsfinal/fixture-list.html")

def GalleryClassic(request):
    return render(request,"sportsfinal/gallery-classic.html")

def GallerySimple(request):
    return render(request,"sportsfinal/gallery-simple.html")

def checkoutPlayer(request):
    check1 = ShopP.objects.all()
    print(check1)
    return render(request,'sportsfinal/checkoutplayer.html',{'check1':check1})

def PlayerDetail(request,pk):
    if request.session.get('id'):
        ad2 = AddPlayer.objects.get(pk=pk)
        if request.method == 'POST':
            u1 = Admin.objects.get(pk=request.session['id'])
            sdd1 = ShopP.objects.create(Admin5=u1, palyerP6=ad2)
            return HttpResponseRedirect(reverse('player-grid'))
        check1 = ShopP.objects.all()
        
        return render(request,"sportsfinal/player-detail.html",{'ad2':ad2})
    else:
        return HttpResponse("Login First")

def PlayerGrid(request):
    pros2 = AddPlayer.objects.all()
    check1 = ShopP.objects.all()
    subtotal1 = 0
    for c in check1:
        subtotal1 += c.total1
    return render(request,"sportsfinal/player-grid.html",{'pros2':pros2,'check1':check1,'subtotal1':subtotal1})


def PlayerListWls(request):
    return render(request,"sportsfinal/player-list-wls.html")

def PlayerListWrs(request):
    return render(request,"sportsfinal/player-list-wrs.html")                                        

def PlayerList(request):
    return render(request,"sportsfinal/player-list.html") 

def SearchResult(request):
    return render(request,"sportsfinal/search-result.html")

def ShopDetail(request,pk):
    if request.session.get('id'):
        ad1 = AddProd.objects.get(pk=pk)
        if request.method == 'POST':
            quntity4 = request.POST['quantity']
            size4 = request.POST['Size']
            u = Admin.objects.get(pk=request.session['id'])
            total = int(quntity4) * int(ad1.nameprice)
            sdd = ShopD.objects.create(Quantity4=int(quntity4),size=int(size4),Admin4=u,productP5=ad1,total=total)
            return HttpResponseRedirect(reverse('shop-grid'))
        check = ShopD.objects.all()
        
        return render(request,"sportsfinal/shop-detail.html",{'ad1':ad1})
    else:
        return HttpResponse("Login First")

def ShopGridWls(request):
    return render(request,"sportsfinal/shop-grid-wls.html")

def ShopGridWrs(request):
    return render(request,"sportsfinal/shop-grid-wrs.html")

def ShopGrid(request):
    pros1 = AddProd.objects.all()
    check = ShopD.objects.all()
    subtotal = 0
    for c in check:
        subtotal += c.total
    return render(request,"sportsfinal/shop-grid.html",{'pros1':pros1,'check':check,'subtotal':subtotal})

def ShoppingCart(request):
    return render(request,"sportsfinal/shopping-cart.html")

def AuthResetPassword(request):
    return render(request,"planetsportsadmin/auth-reset-password.html")

def RepairingZ(request):
    return render(request,"sportsfinal/Repairingzone.html")

         

def RegisterUser(request):
    print("\n\nRegister User Function =====",request.POST.get('role'))
    try:
        if request.POST['role']=="user":
            role = request.POST['role']
            print("Role--------------->",role)
            
            password = request.POST['password']
            confirmpassword = request.POST['confirmpassword']
            address = request.POST['address']
            mobile = request.POST['mobile']
            email = request.POST['email']
            print("EMAIL--------------->",email)
            firstname = request.POST["firstname"]
            lastname = request.POST["lastname"]
            birthday = request.POST['bday']

            user = Admin.objects.filter(email=email)
            print("User----------------->",user)
            if user:
                msg = "User exists"
                return render(request,"sportsfinal/login-register.html",{'message':msg})
            else:
                print("\n\n======== Else ==========")
                if password==confirmpassword:
                    print('==========1===========')
                    # otp = randint(1000000,999999)
                    Otp = randint(10000,99999)
                    print("=========2===========")
                    newadmin = Admin.objects.create(email=email,password=password,role=role,otp=Otp)
                    print("===========3============")
                    print("NewAdmin----------->",newadmin)
    
                    newuser = User.objects.create(admin_id=newadmin,mobile=mobile,firstname=firstname,lastname=lastname,address=address,birthdate=birthday)
                    print("=============4=============")
                    print("NewUSer------------->",newuser)
                    print("NewAdmin----------------->",newadmin,mobile,firstname,lastname,address)
                    subject="CakeArt : Account Verification"
                    sendmail(subject,'mail_template',email,{'name':firstname,'otp':Otp,'link':'http://localhost:8000/enterprise/user_verify/'})
                    return HttpResponseRedirect(reverse('otp'))
                
                    
                  
                else:
                    msg = "Password does not match"
                    return render(request,"sportsfinal/login-register.html",{'message':msg})

        elif request.POST['role']=="vendor":
            role = request.POST['role']
            print("Role ------------>:",role)
            password = request.POST['password']
            confirmpassword = request.POST['confirmpassword']
            address = request.POST['address']
            mobile = request.POST['mobile']
            email = request.POST['email']
            print("EMAIL--------------->",email)
            firstname = request.POST["firstname"]
            lastname = request.POST["lastname"]
            birthday = request.POST['bday']
            print("==========1============")
            vendor_admin = Admin.objects.filter(email=email)

            print("vendor----------------->",vendor_admin)
            if vendor_admin:
                print("--------------If Vendor----------------")
                msg = "vendor exists"
                return render(request,"sportsfinal/login-register.html",{'message':msg})
            else:
                print("\n\n======== Else ==========")
                if password==confirmpassword:
                    print('==========1===========')
                    # otp = randint(1000000,999999)
                    Otp = randint(10000,99999)
                    print("=========2===========")
                    newadmin = Admin.objects.create(email=email,password=password,role=role,otp=otp)

                    print("===========3============")
                    print("NewAdmin----------->",newadmin)
                    try:
                        newvendor = vendor.objects.create(admin_id=newadmin,mobile=mobile,firstname=firstname,lastname=lastname,Address=address,birthdate=birthday)
                        print("=============4=============")
                        print("Newvendor------------->",newvendor)
                        print("NewAdmin----------------->",newadmin,mobile,firstname,lastname,address)
                        subject="CakeArt : Account Verification"
                        sendmail(subject,'mail_template',em,{'name':fnm,'otp':Otp,'link':'http://localhost:8000/enterprise/user_verify/'})
                        return HttpResponseRedirect(reverse('otp'))
                    except Exception as e:
                        print("Error--------------->",e)
                    
                    return HttpResponseRedirect(reverse('VendorRegistrationPage'))
                else:
                    msg = "Password does not match"
                    return render(request,"sportsfinal/login-register.html",{'message':msg})
        else:
            print("New vendor Comming soon--------------------------->")
                    
                   

    except Exception as e:
        print("\n\n============= Error ====",e)
        return HttpResponse(e)
    
def LoginUser(request):
    print("\n\n====================== LOGIN User ===============================")
    print("Role : ",request.POST['role'])
    if request.POST['role']=='user':
        email = request.POST['email']
        print("Email : ",email)
        password = request.POST['password']
        user = Admin.objects.filter(email=email)
        print("User obj : ",user)
        if user:
            if user[0].password==password and user[0].role == 'user':
                e_user = User.objects.get(admin_id = user[0])
                request.session['email'] = user[0].email
                request.session['role'] = user[0].role
                request.session['id'] = user[0].id
                
                return HttpResponseRedirect(reverse('home'))
            else:
                msg = 'Your password is incorrect or user dosen\'t exist'
                return render(request, "sportsfinal/login-register.html",{'message':msg})
        else:
            msg = 'user dosen\'t exist'
            return render(request, "sportsfinal/login-register.html",{'message':msg})

    elif request.POST['role']=='vendor':
        email = request.POST['email']
        password = request.POST['password']
        vendor = Admin.objects.filter(email=email)
        if vendor:
            if vendor[0].password==password and vendor[0].role == 'vendor':
                e_vendor = vendor.objects.get(admin_id = vendor[0])
                request.session['email'] = vendor[0].email
                request.session['role'] = vendor[0].role
                request.session['id'] = vendor[0].id
                
                return HttpResponseRedirect(reverse('home'))
            else:
                msg = 'Your password is incorrect or vendor dosen\'t exist'
                return render(request, "sportsfinal/login-register.html",{'message':msg})
        else:
            msg = 'vendor dosen\'t exist'
            return render(request, "sportsfinal/login-register.html",{'message':msg})



def  home(request):
    if 'email' in request.session and 'role' in request.session:
        if request.session['role'] == 'user':
            all_user = User.objects.all()
            return render(request, 'sportsfinal/index.html', {'all_user':all_user})
        else:
            print('Vendor module dosen\'t exist')

    elif 'email' in request.session and 'role' in request.session:
        if request.session['role'] == 'vendor':
            all_vendor = vendor.objects.all()
            return render(request, 'sportsfinal/index.html', {'all_vendor':all_vendor})


def otp_load(request):
    return render(request,"sportsfinal/otp.html")

def VendorRegistration(request):
      
        Name_of_firm = request.POST['strNameofFirmCompany']
        Type_of_firm = request.POST['fk_intConstitutionFirmID']
        Country = request.POST['str_country']
        Status_of_company  = request.POST['int_fk_CompanyStatusID']
        GST_no = request.POST['strGSTNo']
        PAN_no = request.POST['strPANNo']
        PIN_no = request.POST['str_pin']
        STDCODE_with_Phone_no = request.POST['strPhone1']
        Fax = request.POST['strFax']
        Website = request.POST['strWebsite1']
        Name_of_contactperson = request.POST['strNameContactPerson']
        Designation_of_contactperson  = request.POST['strDesignationofContactPerson']
        Is_your_firm_MSME = request.POST['strTypeofIndustry']
        Brief_discription_of_company = request.POST['str_companydesc']
        Types_of_items_intrested_for_supply = request.POST['strRegistrationApplied']
        address = request.POST['strCorrespondenceAddress']
        city = request.POST['str_city']
        state = request.POST['str_state'] 
        email = request.POST['strEmail']
        mobile = request.POST['strMobile']

        New_vendor = vendorRegistration.objects.create(Type_of_firm = Type_of_firm,Country = Country,Status_of_company = Status_of_company,GST_no = GST_no,PAN_no = PAN_no, PIN_no = PIN_no,STDCODE_with_Phone_no = STDCODE_with_Phone_no,Fax = Fax,Website = Website,Name_of_contactperson = Name_of_contactperson, Designation_of_contactperson = Designation_of_contactperson,Is_your_firm_MSME = Is_your_firm_MSME,Brief_discription_of_company = Brief_discription_of_company,Types_of_items_intrested_for_supply = Types_of_items_intrested_for_supply,address = address,city = city,state = state)
        return render(request,"sportsfinal/index.html")
        
def AddEventData(request):
    if request.POST['role']=="customer2":
        role = request.POST['role']
        Sports_Event_Categories = request.POST['fk_intSportsEventCategories']
        Country = request.POST['str_country']
        Games = request.POST['int_fk_Games']
        GST_no = request.POST['strGSTNo']
        PAN_no = request.POST['strPANNo']
        PIN_no = request.POST['str_pin']
        STDCODE_with_Phone_no = request.POST['strPhone1']        
        Website = request.POST['strWebsite1']
        Name_of_contactperson = request.POST['strNameContactPerson']
        Designation_of_contactperson  = request.POST['strDesignationofContactPerson']
        Brief_discription_of_Event = request.POST['str_Eventdesc']
        Types_of_items_intrested_for_supply = request.POST['strRegistrationApplied']
        address = request.POST['strCorrespondenceAddress']
        city = request.POST['str_city']
        state = request.POST['str_state'] 
        email = request.POST['strEmail']
        mobile = request.POST['strMobile']
        S1 = request.POST['selector1']
        S2 = request.POST['selector2']
        S3 = request.POST['selector3']
        S4 = request.POST['selector4']

        customer2 = AddEvent.objects.create(role = role,Sports_Event_Categories = Sports_Event_Categories,Country = Country,GST_no = GST_no,PAN_no = PAN_no, PIN_no = PIN_no, Games = Games,STDCODE_with_Phone_no = STDCODE_with_Phone_no,Website = Website,Designation_of_contactperson = Designation_of_contactperson,Brief_discription_of_Event = Brief_discription_of_Event,Types_of_items_intrested_for_supply = Types_of_items_intrested_for_supply,address = address,city = city,state = state,email = email,mobile = mobile)
        return render(request,"sportsfinal/index.html")

    else: 
          request.POST['role']=="vendor2"
          role = request.POST['role']
          Sports_Event_Categories = request.POST['fk_intSportsEventCategories']
          Country = request.POST['str_country']
          Games = request.POST['int_fk_Games']
          GST_no = request.POST['strGSTNo']
          PAN_no = request.POST['strPANNo']
          PIN_no = request.POST['str_pin']
          STDCODE_with_Phone_no = request.POST['strPhone1']        
          Website = request.POST['strWebsite1']
          Name_of_contactperson = request.POST['strNameContactPerson']
          Designation_of_contactperson  = request.POST['strDesignationofContactPerson']
          Brief_discription_of_Event = request.POST['str_Eventdesc']
          Types_of_items_intrested_for_supply = request.POST['strRegistrationApplied']
          address = request.POST['strCorrespondenceAddress']
          city = request.POST['str_city']
          state = request.POST['str_state'] 
          email = request.POST['strEmail']
          mobile = request.POST['strMobile']

          vendor2 = AddEvent.objects.create(role = role,Sports_Event_Categories = Sports_Event_Categories,Country = Country,GST_no = GST_no,PAN_no = PAN_no, PIN_no = PIN_no, Games = Games,STDCODE_with_Phone_no = STDCODE_with_Phone_no,Website = Website,Designation_of_contactperson = Designation_of_contactperson,Brief_discription_of_Event = Brief_discription_of_Event,Types_of_items_intrested_for_supply = Types_of_items_intrested_for_supply,address = address,city = city,state = state,email = email,mobile = mobile)
          return render(request,"sportsfinal/index.html")

def EventMembership(request):

       Ownername = request.POST['username']
       Email = request.POST['email']
       Address = request.POST['address']
       Country = request.POST['country']
       State = request.POST['street']
       Zip_code = request.POST['zipcode']
       Team_Count = request.POST['day']
       Mobile_no = request.POST['phone number']
       City = request.POST['city']
       S1 = request.POST['Select']

       New_Membership = SportsEventMembership.objects.create(EO_name = Ownername,EO_email = Email,EO_address = Address,EO_country = Country,EO_state = State,EO_Zip_code = Zip_code,EO_TeamCount = Team_Count,EO_mobile = Mobile_no,EO_city = City,Select_1 = S1)
       return render(request,"sportsfinal/index.html")

def TournamentForm(request):
     
      TeamName = request.POST['TeamN']
      ManagerName = request.POST['ManagerN']
      ManagerEmail = request.POST['EmailAD']
      ManagerMobile1 = request.POST['WorkP']
      ManagerMobile2 = request.POST['otherP']
      CaptainName = request.POST['captainN']
      CaptainEmail = request.POST['capEmail']
      CaptainMobile1 = request.POST['capHomeN']
      CaptainMobile2 = request.POST['capworkP']
      CaptainMobile3 = request.POST['capotherP']
      FinalTournamentPayment = request.POST['payment']
      TeamManagerSign = request.POST['sign']
      TeamUp = request.POST['N']
      
      New_Form = TournamentParticipationForm.objects.create(Team_Name = TeamName,Manager_Name = ManagerName,Manager_Email = ManagerEmail,Manager_Mob_Work = ManagerMobile1,Manager_Mob_Other = ManagerMobile2,Captain_Name =  CaptainName,Captain_Email = CaptainEmail,Captain_Mob_Home = CaptainMobile1,Captain_Mob_Work = CaptainMobile2, Captain_Mob_Other = CaptainMobile3,Final_Payment = FinalTournamentPayment,Team_manager_Sign_Date = TeamManagerSign,Team_N = TeamUp)
      return render(request,"sportsfinal/index.html")


# def AddDataSportsClubMembership(request):
    
    


############################# ADMIN PANEL ################################

def AdminTable(request):
    vendors = User.objects.all()
    return render(request,"Admin/tbl_bootstrap.html",{'vendors':vendors})

def Edit(request,pk):
    admin_user =  User.objects.get(pk=request.GET['id']) 
    return render(request,'Admin/edit.html',{'a_user':admin_user})

def updateUser(request,pk):
    updateU = User.objects.get(pk=pk)
    updateU.firstname = request.POST['fname']
    updateU.lastname = request.POST['lname']
    updateU.mobile = request.POST['mobile']
    updateU.save()
    return HttpResponseRedirect(reverse('AdminTable'))

def deleteUser(request,pk):
    userdelete = User.objects.get(pk=pk)
    userdelete.delete()
    return HttpResponseRedirect(reverse('AdminTable'))



############################ VENDOR PANEL ##################################
def prod(request):
    return render(request,"Admin/productAdd.html")

def addpro(request):
        ProductName = request.POST['quick']
        ProductPrice = request.POST['pri5']
        ProductDescrip = request.POST['Productdescription']
        print("Enetr Data")
        ProductImage = request.FILES['categoryimg']
        qtyy2 = request.POST['Quantityy']

        Npro =  AddProd.objects.create(nameprod=ProductName,nameprice=ProductPrice,namedescrip= ProductDescrip,nameimg=ProductImage,quantity9=qtyy2)
        return HttpResponseRedirect(reverse('showprod'))

def Showprod(request):
    pros = AddProd.objects.all()
    print("All Pro --------->",pros)
    # <td style="font-family: Arial, Helvetica, sans-serif;font-size:20px;"><img src="{{MEDIA_URL}}{{p.nameimg.url}}" height="120" width="120"></img></td>
    print(pros)
    return render(request,"Admin/showprod.html",{'pros':pros})

def editprod(request,pk):
    v_edit= AddProd.objects.get(pk=pk)
    return render(request,'Admin/editprod.html',{'v_edit':v_edit})

# def updateprod(request,pk):
#     print("***************Update Product Views**************")
#     try:
#         updatepro = AddProd.objects.get(pk=pk)
#         updatepro.ProdName = request.POST['pnm']
#         updatepro.ProdPrice = request.POST['pprc']
#         updatepro.ProdDescrip = request.POST['pdesc']
#         updatepro.Prodqtyy2 = request.POST['pqty']
#         updatepro.ProdImage  = request.FILES['pimage1']
#         updatepro.save()
#         return HttpResponseRedirect(reverse('showprod'))

#     except Exception as p1:
#         print("Update Product Exception -------------->",p1)

def updateprod(request,pk):
    try:
        print("\n\n======================== UPDATE PROD ==========================")
        updatepro = AddProd.objects.get(pk=pk)
        print("Product ---------->",updatepro)
        print("BEFORE NAME == ",updatepro.nameprod)
        updatepro.nameprod = request.POST['pnm']
        print("After  NAME == ",updatepro.nameprod)
        updatepro.nameprice = request.POST['pprc']
        updatepro.namedescrip = request.POST['pdesc']
        updatepro.quantity9 = request.POST['pqty']
        updatepro.nameimg  = request.FILES['pimage1']
        updatepro.save()
        print("=========================== END UPDATE PROD ====================== \n\n")
        return HttpResponseRedirect(reverse('showprod'))
    except Exception as p1:
        print("Update Product Exception -------------->",p1)
        
    

def deleteprod(request,pk):
    proddelete = AddProd.objects.get(pk=pk)
    proddelete.delete()
    return HttpResponseRedirect(reverse('showprod'))

def cartdelete(request,pk):
    print("*******************CartDelete View**********************")
    cartdata = ShopD.objects.get(pk=pk)
    cartdata.delete()
    return HttpResponseRedirect(reverse('checkout'))
    print("****************Bye*******************")


############################## PLAYER PANEL ##############################

def PlayerInfo(request):
    return render(request,"Admin/PlayerAdd.html")

def AddPlayerDetail(request):
  
    Playname = request.POST['Playname']
    PlayerPrice = request.POST['PlayerPr']
    PlayerPhone = request.POST['PlayerNo']
    PlayerRanks = request.POST['PlayerRank']
    PlayerDescrip = request.POST['Playerdescription']
    PlayerImg = request.FILES['Playerimg']
    PlayerPoint = AddPlayer.objects.create(PlayerName=Playname,PlayerPrice=PlayerPrice,PlayerMobile=PlayerPhone,PlayerRank=PlayerRanks,PlayerDescription=PlayerDescrip,PlayerImage=PlayerImg)
    return HttpResponseRedirect(reverse('ShowPlayer'))

def ShowPlayer(request):
    Players = AddPlayer.objects.all()
    return render(request,"Admin/showplayer.html",{'Players':Players})

def editPlayer(request,pk):

    editP =  AddPlayer.objects.get(pk=pk)
    return render(request,'Admin/EditPlayer.html',{'editP':editP})

def updatePlayer(request,pk):
    
    updatePlayers = AddPlayer.objects.get(pk=pk)
    updatePlayers.PlayerName = request.POST['PlayerNme']
    updatePlayers.PlayerPrice = request.POST['Pprice']
    updatePlayers.PlayerMobile = request.POST['PMob']
    updatePlayers.PlayerRank = request.POST['PlayerR']
    updatePlayers.PlayerDescription = request.POST['PlayerDescrip']
    updatePlayers.PlayerImage = request.FILES['PImage']
    updatePlayers.save()
    return HttpResponseRedirect(reverse('ShowPlayer'))

def deletePlayer(request,pk):

    PlayerDelete = AddPlayer.objects.get(pk=pk)
    PlayerDelete.delete()
    return HttpResponseRedirect(reverse('ShowPlayer'))

def cartdelete2(request,pk):
    print("*******************CartDelete View**********************")
    cartplayer = ShopP.objects.get(pk=pk)
    cartplayer.delete()
    return HttpResponseRedirect(reverse('checkoutPlayer'))
    print("****************Bye*******************")

####################### GROUND BOOKING ###################################
def Ground2(request):
    return render(request,"GroundBook/GroundBook2.html")

def Grounds2(request):
    return render(request,"GroundBook/Ground2.html")

def Grounds3(request):
    return render(request,"GroundBook/Ground3.html")

def Grounds4(request):
    return render(request,"GroundBook/Ground4.html")

def Grounds5(request):
    return render(request,"GroundBook/Ground5.html")

def Groundpayment(request):
    return render(request,"GroundBook/groundpayment.html")

def GroundHome(request):
    return render(request,"GroundBook/GroundMain.html")


def picker(request):
    return render(request,"GroundBook/picker.html")

def AddGDetail(request):
    print("G------------>:")
    Address_G1 = request.POST['address2']
    SS = request.POST['sport_option']
    SG = request.POST['ground_option']
    request.session['add'] = Address_G1
    new_Detail =  GroundDetails.objects.create(Address_G = Address_G1,S_Sports = SS,S_Ground = SG)
    return HttpResponseRedirect('paymentShow')
    return render(request,"GroundBook/groundpayment.html")
    
def paymentShow(request):
    print("\n\n=================================")

    all_D = GroundDetails.objects.all()
    print("\n\nALL D====",all_D)
    return render(request,"GroundBook/groundpayment.html", {'all_D':all_D[0]})


    


######################## EVENT INFO ########################

def EventInfo1(request):
    return render(request,"GroundBook/eventinfo.html")    




########################  ################





############################ Paytm Views #########################################
def initiate_payment(request):
    print("Inside View")
    if request.method == "GET":
        print("/n/n========================inside get===============/n/n")
        hr = ShopD.objects.all()
        total = 0.0
        for var in hr:
            total = total + var.total
        return render(request, 'paytm/pay.html',{'total':total})
    try:
        email = request.session['email']
        password = request.POST['password']
        amount = int(request.POST['amount'])
        user = Admin.objects.get(email=email)
        if user:
            transaction = Transaction.objects.create(made_by=user, amount=amount)
            transaction.save()
            merchant_key = settings.PAYTM_SECRET_KEY

            params = (
                ('MID', settings.PAYTM_MERCHANT_ID),
                ('ORDER_ID', str(transaction.order_id)),
                ('CUST_ID', str(transaction.made_by.email)),
                ('TXN_AMOUNT', str(transaction.amount)),
                ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
                ('WEBSITE', settings.PAYTM_WEBSITE),
                # ('EMAIL', request.user.email),
                # ('MOBILE_N0', '9911223388'),
                ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
                ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
                # ('PAYMENT_MODE_ONLY', 'NO'),
            )

            paytm_params = dict(params)
            checksum = generate_checksum(paytm_params, merchant_key)
            print("\n\n======== Checksum : ",checksum,len(checksum))
            transaction.checksum = checksum
            transaction.save()

            paytm_params['CHECKSUMHASH'] = checksum
            print('SENT: ', checksum)
            return render(request, 'paytm/redirect.html', context=paytm_params)


    except Exception as ee:
        print("Paytm Exception -------------------->",ee)
        return render(request, 'paytm/pay.html', context={'error': 'Wrong Accound Details or amount'})

    

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
        else:
            received_data['message'] = "Checksum Mismatched"
        return render(request, 'paytm/callback.html', context=received_data)

################################################ payment-Player ################################################

def initiate_payment2(request):
    print("Inside View")
    if request.method == "GET":
        print("/n/n========================inside get===============/n/n")
        hre = ShopP.objects.all()
        total1 = 0.0
        for var in hre:
            total1 = total1 + var.total1
        return render(request, 'paytm/pay2.html',{'total1':total1})
    try:
        email = request.session['email']
        password = request.POST['password']
        amount = int(request.POST['amount'])
        user = Admin.objects.get(email=email)
        if user:
            transaction = Transaction.objects.create(made_by=user, amount=amount)
            transaction.save()
            merchant_key = settings.PAYTM_SECRET_KEY

            params = (
                ('MID', settings.PAYTM_MERCHANT_ID),
                ('ORDER_ID', str(transaction.order_id)),
                ('CUST_ID', str(transaction.made_by.email)),
                ('TXN_AMOUNT', str(transaction.amount)),
                ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
                ('WEBSITE', settings.PAYTM_WEBSITE),
                # ('EMAIL', request.user.email),
                # ('MOBILE_N0', '9911223388'),
                ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
                ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
                # ('PAYMENT_MODE_ONLY', 'NO'),
            )

            paytm_params = dict(params)
            checksum = generate_checksum(paytm_params, merchant_key)
            print("\n\n======== Checksum : ",checksum,len(checksum))
            transaction.checksum = checksum
            transaction.save()

            paytm_params['CHECKSUMHASH'] = checksum
            print('SENT: ', checksum)
            return render(request, 'paytm/redirect2.html', context=paytm_params)


    except Exception as ee:
        print("Paytm Exception -------------------->",ee)
        return render(request, 'paytm/pay.html', context={'error': 'Wrong Accound Details or amount'})

    

@csrf_exempt
def callback2(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
        else:
            received_data['message'] = "Checksum Mismatched"
        return render(request, 'paytm/callback2.html', context=received_data)





################################################ E-MAIL #########################################################

def IndexPage(request):
    return render(request,"Email/Emailindex.html")



def SendData(request):
    email = request.POST['email']
    otp = randint(10000,99999)

    newuser = Admin.objects.create(email=email)
    email_Subject = "User Verifaction"
    email_msg = "Hello this mail is send by Admin"
    sendmail(email_Subject,"mail_template",email,{'otp':otp,'msg':email_msg})
    message = "Email Send successFully"
    return render(request,"Email/Emailindex.html",{'message':message})
