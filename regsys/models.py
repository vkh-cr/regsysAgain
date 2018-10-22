from django.db import models


class Sleeping:
    BED = 'Postel'
    BAG = 'Spacak'
    NON = 'Sirak'

    choices = (
        (BED, 'Ubytování s příslušenstvím - postel'),
        (BAG, 'Ubytování spacák a karimatka'),
        (NON, 'Bez ubytovani'),
    )

    def maxLen(self):
        max(list(map(lambda p: len(p[0]), Sleeping.choices)))


class RegStatus:
    WAITING_PAYMENT = 'WAITING_PAYMENT'
    PAID = 'PAID'
    EXPIRED = 'EXPIRED'
    CANCELLED = 'CANCELLED'

    choices = (
        (WAITING_PAYMENT, 'Ceka na zaplaceni'),
        (PAID, 'Zaplaceno'),
        (EXPIRED, 'Platba vyprsela'),
        (CANCELLED, 'Zruseno'),
    )

    def maxLen(self):
        max(list(map(lambda p: len(p[0]), RegStatus.choices)))


class RegType:
    ATTANDEE = 'Ucastnik'
    VOLUNTEER = 'Dobrovolnik'
    GUEST = 'Host'
    PRIEST = 'Duchovni'
    TEAM = 'Tym'

    choices = (
        (ATTANDEE, 'Ucastnik'),
        (VOLUNTEER, 'Dobrovolnik'),
        (GUEST, 'Host'),
        (PRIEST, 'Duchovni'),
        (TEAM, 'Tym'),
    )
    
    def maxLen(self):
        max(list(map(lambda p: len(p[0]), RegType.choices)))
    

class DetailRegistration(models.Model):
    first_name = models.CharField(max_length=30, default='lol')
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    birth_year = models.IntegerField()
    address = models.CharField(max_length=100)
    tip = models.IntegerField(default=10)
    message = models.TextField(default='None')

    fri_breakfast = models.BooleanField(default=True)
    fri_lunch = models.BooleanField(default=True)
    fri_dinner = models.BooleanField(default=True)
    sat_breakfast = models.BooleanField(default=True)
    sat_lunch = models.BooleanField(default=True)
    sat_dinner = models.BooleanField(default=True)
    sun_breakfast = models.BooleanField(default=True)
    sun_lunch = models.BooleanField(default=True)
    
    fri_night = models.CharField(max_length=10, choices=Sleeping.choices, default=Sleeping.BED)
    sat_night = models.CharField(max_length=10, choices=Sleeping.choices, default=Sleeping.BED)

    status = models.CharField(max_length=30, choices=RegStatus.choices, default=RegStatus.WAITING_PAYMENT)

    internal_message = models.TextField(default='Nothing specific')
    price = models.IntegerField(default=200)
    date_created = models.DateField(auto_now=True, editable=False)
    var_symbol = models.IntegerField(primary_key=True)
    reg_type = models.CharField(max_length=10, choices=RegType.choices, default=RegType.ATTANDEE)

    def __str__(self):
        return "DetailRegistration, {} {}, status {}".format(self.first_name, self.last_name, self.status)


class Payment(models.Model):
    pay_date = models.DateField(auto_now=False, editable=False)
    amount = models.IntegerField()
    account_num = models.CharField(max_length=30)
    account_bank = models.CharField(max_length=30)
    account_name = models.CharField(max_length=30)
    var_symbol = models.IntegerField()
    spec_symbol = models.IntegerField()
    json = models.CharField(max_length=300)

    def __str__(self):
        return "Payment acc: %s - %s/%s - %s" % (self.account_name, self.account_num, self.account_bank, self.amount)
