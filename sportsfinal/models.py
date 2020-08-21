from django.db import models

# Create your models here.
class Admin(models.Model):
    email = models.EmailField(unique= True)
    password = models.CharField(max_length = 20)
    otp = models.IntegerField(default = 459)
    is_active = models.BooleanField(default=True)
    is_verfied = models.BooleanField(default=False)
    role = models.CharField(max_length = 50)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)

class User(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length= 500, blank= True)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50, blank= True)
    gender = models.CharField(max_length= 10)
    birthdate = models.DateField(blank=True)
    location = models.CharField(max_length= 30, blank= True)
    

class vendor(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    vendor_address = models.CharField(max_length=500, blank= True) 
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank= True)
    gender = models.CharField(max_length=10)
    birthdate = models.DateField(blank = True)
    location = models.CharField(max_length=30, blank= True)
    Address = models.CharField(max_length=100, blank= True)
   
class SportsEventMembership(models.Model):
    EO_name = models.CharField(max_length=50)
    EO_email = models.EmailField(unique= True, default='8')
    EO_mobile = models.BigIntegerField(default='9')
    EO_address = models.CharField(max_length=200, blank = True)
    EO_city = models.CharField(max_length=200)
    EO_country = models.CharField(max_length=50)
    EO_state = models.CharField(max_length=50)
    EO_TeamCount = models.CharField(max_length=6, blank = True)
    EO_Zip_code = models.CharField(max_length=50, blank = True)
    Select_1 = models.CharField(max_length=50,blank = True)
    

class EventParticipants(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete = models.CASCADE)
    EP_game = models.CharField(max_length=20, blank = True)
    EP_fee = models.CharField(max_length=6, blank = True)

class EventParticipantsInfo(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete  = models.CASCADE)
    EP_name = models.CharField(max_length=100, blank = True)
    EP_mob = models.CharField(max_length=10)
    EP_occupation = models.CharField(max_length=50)
    EP_age = models.CharField(max_length=3)
    EP_email = models.EmailField(max_length=50)

class CoachingInstitute(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete = models.CASCADE)
    CI_name = models.CharField(max_length=50, blank = True)
    CI_address = models.CharField(max_length=200, blank = True)
    CI_contact = models.CharField(max_length=10)
    CI_descriptions = models.CharField(max_length=4000)
    CI_ratings = models.CharField(max_length=5)

class CoachingInstituteGuestPlayer(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete = models.CASCADE)
    User_id = models.ForeignKey(User, on_delete = models.CASCADE,default="1")
    GP_id = models.CharField(max_length=10, blank = True)
    GP_contact = models.CharField(max_length=10, blank = True)
    GP_name = models.CharField(max_length=50, blank = True)
    GP_age = models.CharField(max_length=3, blank = True)
    GP_achievements = models.CharField(max_length=200, blank = True)
    GP_experiece = models.CharField(max_length=3, blank = True)
    GP_ratings = models.CharField(max_length=5)

class Catering(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete = models.CASCADE)
    CAT_name = models.CharField(max_length=50)
    CAT_speciality = models.CharField(max_length=30, blank = True)
    CAT_contact = models.CharField(max_length=10, blank = True)
    CAT_add = models.CharField(max_length=20, blank = True)

class CateringSnacksInfo(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete = models.CASCADE)
    CAT_snackname = models.CharField(max_length=20, blank = True)
    CAT_quantity = models.CharField(max_length=5, blank = True)
    CAT_price = models.CharField(max_length=5, blank = True)

class SportsEducation(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete = models.CASCADE)
    SE_description = models.CharField(max_length=4000, blank = True)
    SE_name = models.CharField(max_length=20, blank = True)
    CI_id = models.ForeignKey(CoachingInstitute, on_delete = models.CASCADE)

class SportsEducationRedirectsToCoachingInstitute(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete = models.CASCADE)
    SE_id = models.ForeignKey(SportsEducation, on_delete = models.CASCADE)
    CI_id = models.ForeignKey(CoachingInstitute, on_delete = models.CASCADE)

class Offer(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete = models.CASCADE)
    OF_discountprice = models.CharField(max_length=6, blank = True)

################################## ADD TO CART/ PRODUCT ##########################################
# class ProductTbl(models.Model):
#    pname = models.CharField(max_length = 50)
#    pprice = models.IntegerField()
#    qty = models.IntegerField()

# class CartTbl(models.Model):
#     FkPID = models.ForeignKey(ProductTbl, on_delete = models.CASCADE)
#     FkUID= models.IntegerField(default="15")
#     total = models.IntegerField()
#     qty = models.IntegerField()

################################  PRODUCT ################################################

class AddProd(models.Model):
    nameprod = models.CharField(max_length = 100,blank = True)
    nameprice = models.IntegerField()
    namedescrip = models.CharField(max_length = 100,blank = True)
    nameimg = models.ImageField(upload_to='image/', default='')
    quantity9 = models.IntegerField( default = "15")


class ShopD(models.Model):
    Admin4 = models.ForeignKey(Admin, on_delete = models.CASCADE, null = True)
    productP5 = models.ForeignKey(AddProd, on_delete = models.CASCADE)
    Quantity4 = models.IntegerField(default = 1)
    size = models.IntegerField(default = 1)
    total = models.BigIntegerField(default = 0)



################################ PLAYER ###################################################

class AddPlayer(models.Model): 
    PlayerName = models.CharField(max_length = 100,blank = True)
    PlayerPrice = models.IntegerField()
    PlayerMobile = models.BigIntegerField(default="18")
    PlayerRank = models.IntegerField()
    PlayerDescription = models.CharField(max_length = 800,blank = True)
    PlayerImage = models.ImageField(upload_to='image/', default='')

class ShopP(models.Model):
    Admin5 = models.ForeignKey(Admin, on_delete = models.CASCADE, null = True)
    palyerP6 = models.ForeignKey(AddPlayer, on_delete = models.CASCADE)
    total1 = models.BigIntegerField(default = 0)



class RepairingZone(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete = models.CASCADE)
    User_id = models.ForeignKey(User, on_delete = models.CASCADE, default="4")
    RZ_item = models.CharField(max_length=50, blank = True)
    RZ_qty = models.CharField(max_length=6, blank = True)
    RZ_date = models.CharField(max_length=12, blank = True)
    RZ_description = models.CharField(max_length=200, blank = True)


# class Reports(models.Model):
#     admin_id = models.ForeignKey(Admin, on_delete = models.CASCADE)
#     vendor_id = models.ForeignKey(vendor, on_delete = models.CASCADE)
#     PD_id = models.ForeignKey(Product, on_delete = models.CASCADE)

class Feedback(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete = models.CASCADE)
    User_id = models.ForeignKey(User, on_delete = models.CASCADE, default="3")
    FD_comments = models.CharField(max_length=200, blank = True)
    FD_ratings = models.CharField(max_length=5)

class vendorRegistration(models.Model):
    
    Name_of_firm = models.CharField(max_length=30, blank= True)
    Type_of_firm = models.CharField(max_length=30, blank = True)
    Country = models.CharField(max_length=50, blank = True)
    Status_of_company = models.CharField(max_length=50, blank = True)
    GST_no = models.CharField(max_length=50, blank = True)
    PAN_no = models.CharField(max_length=50, blank = True)
    PIN_no = models.CharField(max_length=50, blank = True)
    STDCODE_with_Phone_no = models.CharField(max_length=50, blank = True)
    Fax = models.CharField(max_length=50, blank = True)
    Website = models.CharField(max_length=50, blank=True)
    Name_of_contactperson = models.CharField(max_length=30, blank = True)
    Designation_of_contactperson = models.CharField(max_length=50, blank = True)
    Is_your_firm_MSME = models.CharField(max_length=30, blank = True)
    Brief_discription_of_company = models.CharField(max_length=800, blank = True)
    Types_of_items_intrested_for_supply = models.CharField(max_length=50, blank = True)
    address = models. CharField(max_length=200, blank = True)
    city = models.CharField(max_length=50,blank=True)
    state = models.CharField(max_length=50,blank=True)

class AddEvent(models.Model):

    role = models.CharField(max_length = 50, default='7')
    Sports_Event_Categories = models.CharField(max_length=30, blank = True)
    Country = models.CharField(max_length=50, blank = True)
    Games = models.CharField(max_length=50, blank = True)
    GST_no = models.CharField(max_length=50, blank = True)
    PAN_no = models.CharField(max_length=50, blank = True)
    PIN_no = models.CharField(max_length=50, blank = True)
    STDCODE_with_Phone_no = models.CharField(max_length=50, blank = True)
    Website = models.CharField(max_length=50, blank=True)
    Name_of_contactperson = models.CharField(max_length=30, blank = True)
    Designation_of_contactperson = models.CharField(max_length=50, blank = True)
    Brief_discription_of_Event = models.CharField(max_length=800, blank = True)
    Types_of_items_intrested_for_supply = models.CharField(max_length=50, blank = True)
    address = models.CharField(max_length=200, blank = True)
    city = models.CharField(max_length=50,blank=True)
    state = models.CharField(max_length=50,blank=True)
    email = models.EmailField(unique= True, default='8')
    mobile = models.BigIntegerField(default='9')

class TournamentParticipationForm(models.Model):

    Team_Name = models.CharField(max_length= 100, blank = True)
    Manager_Name = models.CharField(max_length= 50, blank = True)
    Manager_Email = models.EmailField(unique= True)
    Manager_Mob_Work = models.BigIntegerField(default='10')
    Manager_Mob_Other = models.BigIntegerField(default='11')
    Captain_Name = models.CharField(max_length= 100, blank = True)
    Captain_Email = models.EmailField(unique= True)
    Captain_Mob_Home = models.BigIntegerField(default='12')
    Captain_Mob_Work = models.BigIntegerField(default='13')
    Captain_Mob_Other = models.BigIntegerField(default='14')
    Final_Payment = models.CharField(max_length= 100, blank = True)
    Team_manager_Sign_Date = models.CharField(max_length= 100,blank = True)
    Team_N = models.CharField(max_length=100,blank = True)

class GroundDetails(models.Model):

    Address_G = models.CharField(max_length= 200, blank = True)
    S_Sports = models.CharField(max_length= 50, blank = True)
    S_Ground = models.CharField(max_length= 50, blank = True)


################## Paytm ###########################

class Transaction(models.Model):
    made_by = models.ForeignKey(Admin, related_name='transactions', on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=250, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

    