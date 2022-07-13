from django.db import models

# Create your models here.

# class PatientHistory(models.Model):
# class PatientContraceptives(models.Model):
# class PatientVisitReason(models.Model):
  
class PatientActivity(models.Model):
    
    smoking = models.BooleanField()
    cigarette = models.CharField(max_length=255)
    
    cigarette_start_age = models.IntegerField()
    cigarette_duration  = models.IntegerField()
    
    hookahs = models.BooleanField()
    hookahs_start_age  = models.IntegerField()
    hookahs_duration  = models.IntegerField()

    # Type ? 
    drugs  = models.BooleanField()
    drugs_start_age =  models.IntegerField()
    drugs_duration  = models.IntegerField()

    alcohol = models.BooleanField()
    alcohol_start_age =  models.IntegerField()
    alcohol_duration =  models.IntegerField()

    sports_type = models.CharField(max_length=255)
    sports_level = models.CharField(max_length=64)

    #  weekly
    weekly_vegetables =  models.IntegerField()
    weekly_tea =  models.IntegerField()
    weekly_coffee =  models.IntegerField()
    weekly_fastfood =  models.IntegerField()
    weekly_W_meat =  models.IntegerField()
    weekly_R_meat =  models.IntegerField()
    weekly_chocolate_sweets  =  models.IntegerField()
    weekly_frying  =  models.IntegerField()
    weekly_softdrink  =  models.IntegerField()
    weekly_milk =  models.IntegerField()
    weekly_buttermilk  =  models.IntegerField()
    weekly_yogurt  =  models.IntegerField()
    weekly_cheese  =  models.IntegerField()
    weekly_curd =  models.IntegerField()
    weekly_icecream =  models.IntegerField()
    
    solid_veg_oil = models.IntegerField()
    liquid_veg_oil = models.IntegerField()
    animal_oil =models.IntegerField()
    tallow = models.IntegerField()
    margarine = models.IntegerField()

    salt_no = models.BooleanField()
    salt_low = models.BooleanField()
    salt_medium = models.BooleanField()
    salt_high = models.BooleanField()

    
    
    def __str__(self):
        return f"{self.name}"


class PatientDisease(models.Model):
    
    diabete = models.BooleanField()
    diabete_month  = models.IntegerField()
    diabete_age  = models.IntegerField()
    diabete_treatment  = models.CharField(max_length=255)

    hypertension = models.BooleanField()
    hypertension_month = models.IntegerField()
    hypertension_age = models.IntegerField()
    hypertension_treatment  = models.CharField(max_length=255)

    heart = models.BooleanField()
    heart_month  = models.IntegerField()
    heart_age  = models.IntegerField()
    heart_treatment  = models.CharField(max_length=255)

    cholestrol = models.BooleanField()
    cholestrol_month  = models.IntegerField()
    cholestrol_age  = models.IntegerField()
    cholestrol_treatment  = models.CharField(max_length=255)


    hypothyroidism = models.BooleanField()
    hypothyroidism_month  = models.IntegerField()
    hypothyroidism_age  = models.IntegerField()
    hypothyroidism_treatment  = models.CharField(max_length=255)

    hyperthyroidism = models.BooleanField()
    hyperthyroidism_month  = models.IntegerField()
    hyperthyroidism_age  = models.IntegerField()
    hyperthyroidism_treatment  = models.CharField(max_length=255)


    MS = models.BooleanField()
    MS_month  = models.IntegerField()
    MS_age  = models.IntegerField()
    MS_treatment  = models.CharField(max_length=255)


    meningioma = models.BooleanField()
    meningioma_month  = models.IntegerField()
    meningioma_age  = models.IntegerField()
    meningioma_treatment  = models.CharField(max_length=255)

    rheumatic = models.BooleanField()
    rheumatic_month  = models.IntegerField()
    rheumatic_age  = models.IntegerField()
    rheumatic_treatment  = models.CharField(max_length=255)
    rheumatic_type  = models.CharField(max_length=255)

    TB = models.BooleanField()
    TB_month  = models.IntegerField()
    TB_age  = models.IntegerField()
    TB_treatment  = models.CharField(max_length=255)
    TB_tissue   = models.CharField(max_length=255)

    other   = models.CharField(max_length=255)
    other_month  = models.IntegerField()
    other_age  = models.IntegerField()
    other_treatment  = models.CharField(max_length=255)

    
    def __str__(self):
        return f"{self.name}"

