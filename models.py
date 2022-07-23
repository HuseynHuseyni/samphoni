from django.db import models

# Create your models here.

class PatientPersonalInfo(models.Model):
    name = models.CharField(max_length=64)
    father = models.CharField(max_length=64)
    sex = models.CharField(max_length=1, choices=(
        ("M", "Male"),
        ("F", "Female")
    ))
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=64)
    mobile = models.CharField(max_length=64)
    b_date = models.DateField()
    b_city = models.CharField(max_length=64)
    edu = models.CharField(max_length=64)
    job = models.CharField(max_length=64)
    marital = models.CharField(max_length=64)
    weight = models.IntegerField()
    height = models.IntegerField()
    income = models.IntegerField()
    start_menstruation_age = models.IntegerField()
    first_child_age = models.IntegerField()
    first_pregnancy_age = models.IntegerField()
    pregnant_now = models.BooleanField()
    stillbirth = models.IntegerField()
    num_pregnancy = models.IntegerField()
    num_births = models.IntegerField()
    num_abortions = models.IntegerField()
    abortions_age = models.IntegerField()
    num_children = models.IntegerField()
    num_breastfeeding = models.IntegerField()
    menopause = models.BooleanField()
    menopause_age = models.IntegerField()
    hysterectomy = models.IntegerField()
    infertility_drug = models.CharField(max_length=64)
    infertility_duration = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class PatientHistory(models.Model):
    patient = models.ForeignKey(
        "PatientPersonalInfo", on_delete=models.CASCADE)
    cancer_type = models.IntegerField()
    breast_cancer_type = models.IntegerField()
    breast_surgery = models.BooleanField()
    breast_surgery_year = models.IntegerField()
    radiotherapy = models.CharField(max_length=255)
    radiotherapy_tissue = models.CharField(max_length=255)
    breast_family = models.CharField(max_length=64)
    breast_family_relationship = models.CharField(max_length=64)
    cancer_family = models.CharField(max_length=64)
    cancer_family_type = models.IntegerField()
    cancer_family_relationship = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.patient}"


class PatientContraceptives(models.Model):
    patient = models.ForeignKey(
        "PatientPersonalInfo", on_delete=models.CASCADE)
    Contraceptives = models.CharField(max_length=255)
    prevention_pill = models.CharField(max_length=255)
    prevention_pill_duration = models.IntegerField()

    prevention_1m_ampule = models.BooleanField()
    prevention_1m_ampule_duration = models.IntegerField()

    prevention_3m_ampule = models.BooleanField()
    prevention_3m_ampule_duration = models.IntegerField()

    prevention_IUD = models.BooleanField()
    prevention_IUD_duration = models.IntegerField()

    prevention_TL = models.BooleanField()
    prevention_TL_duration = models.IntegerField()

    prevention_others = models.CharField(max_length=255)
    prevention_others_duration = models.IntegerField()

    def __str__(self):
        return f"{self.patient}"


class PatientVisitReason(models.Model):
    patient = models.ForeignKey(
        "PatientPersonalInfo", on_delete=models.CASCADE)
    pain = models.BooleanField()
    swelling = models.BooleanField()
    nipple_depression = models.BooleanField()
    sagging_skin = models.BooleanField()
    sores = models.BooleanField()
    redness = models.BooleanField()
    lumps = models.BooleanField()
    discharge = models.BooleanField()
    itching = models.BooleanField()
    burning_bulging = models.BooleanField()
    asymptomatic = models.BooleanField()

    def __str__(self):
        return f"{self.patient}"


class PatientActivity(models.Model):
    patient = models.ForeignKey(
        "PatientPersonalInfo", on_delete=models.CASCADE)

    smoking = models.BooleanField()
    cigarette = models.CharField(max_length=255)

    cigarette_start_age = models.IntegerField()
    cigarette_duration = models.IntegerField()

    hookahs = models.BooleanField()
    hookahs_start_age = models.IntegerField()
    hookahs_duration = models.IntegerField()

    # Type ?
    drugs = models.BooleanField()
    drugs_start_age = models.IntegerField()
    drugs_duration = models.IntegerField()

    alcohol = models.BooleanField()
    alcohol_start_age = models.IntegerField()
    alcohol_duration = models.IntegerField()

    sports_type = models.CharField(max_length=255)
    sports_level = models.CharField(max_length=64)

    #  weekly
    weekly_vegetables = models.IntegerField()
    weekly_tea = models.IntegerField()
    weekly_coffee = models.IntegerField()
    weekly_fastfood = models.IntegerField()
    weekly_W_meat = models.IntegerField()
    weekly_R_meat = models.IntegerField()
    weekly_chocolate_sweets = models.IntegerField()
    weekly_frying = models.IntegerField()
    weekly_softdrink = models.IntegerField()
    weekly_milk = models.IntegerField()
    weekly_buttermilk = models.IntegerField()
    weekly_yogurt = models.IntegerField()
    weekly_cheese = models.IntegerField()
    weekly_curd = models.IntegerField()
    weekly_icecream = models.IntegerField()

    solid_veg_oil = models.IntegerField()
    liquid_veg_oil = models.IntegerField()
    animal_oil = models.IntegerField()
    tallow = models.IntegerField()
    margarine = models.IntegerField()

    salt_no = models.BooleanField()
    salt_low = models.BooleanField()
    salt_medium = models.BooleanField()
    salt_high = models.BooleanField()

    def __str__(self):
        return f"{self.name}"


class PatientDisease(models.Model):
    patient = models.ForeignKey(
        "PatientPersonalInfo", on_delete=models.CASCADE)

    diabete = models.BooleanField()
    diabete_month = models.IntegerField()
    diabete_age = models.IntegerField()
    diabete_treatment = models.CharField(max_length=255)

    hypertension = models.BooleanField()
    hypertension_month = models.IntegerField()
    hypertension_age = models.IntegerField()
    hypertension_treatment = models.CharField(max_length=255)

    heart = models.BooleanField()
    heart_month = models.IntegerField()
    heart_age = models.IntegerField()
    heart_treatment = models.CharField(max_length=255)

    cholestrol = models.BooleanField()
    cholestrol_month = models.IntegerField()
    cholestrol_age = models.IntegerField()
    cholestrol_treatment = models.CharField(max_length=255)

    hypothyroidism = models.BooleanField()
    hypothyroidism_month = models.IntegerField()
    hypothyroidism_age = models.IntegerField()
    hypothyroidism_treatment = models.CharField(max_length=255)

    hyperthyroidism = models.BooleanField()
    hyperthyroidism_month = models.IntegerField()
    hyperthyroidism_age = models.IntegerField()
    hyperthyroidism_treatment = models.CharField(max_length=255)

    MS = models.BooleanField()
    MS_month = models.IntegerField()
    MS_age = models.IntegerField()
    MS_treatment = models.CharField(max_length=255)

    meningioma = models.BooleanField()
    meningioma_month = models.IntegerField()
    meningioma_age = models.IntegerField()
    meningioma_treatment = models.CharField(max_length=255)

    rheumatic = models.BooleanField()
    rheumatic_month = models.IntegerField()
    rheumatic_age = models.IntegerField()
    rheumatic_treatment = models.CharField(max_length=255)
    rheumatic_type = models.CharField(max_length=255)

    TB = models.BooleanField()
    TB_month = models.IntegerField()
    TB_age = models.IntegerField()
    TB_treatment = models.CharField(max_length=255)
    TB_tissue = models.CharField(max_length=255)

    other = models.CharField(max_length=255)
    other_month = models.IntegerField()
    other_age = models.IntegerField()
    other_treatment = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.patient}"


class PatientDrugs(models.Model):
    patient = models.ForeignKey(
        "PatientPersonalInfo", on_delete=models.CASCADE)

    group1 = models.CharField(max_length=255)
    g1_drug_names = models.CharField(max_length=255)
    g1_duration = models.CharField(max_length=255)
    group2 = models.CharField(max_length=255)
    g2_drug_names = models.CharField(max_length=255)
    g2_duration = models.CharField(max_length=255)
    group3 = models.CharField(max_length=255)
    g3_drug_names = models.CharField(max_length=255)
    g3_duration = models.CharField(max_length=255)
    group4 = models.CharField(max_length=255)
    g4_drug_names = models.CharField(max_length=255)
    g4_duration = models.CharField(max_length=255)
    group5 = models.CharField(max_length=255)
    g5_drug_names = models.CharField(max_length=255)
    g5_duration = models.CharField(max_length=255)
    group6 = models.CharField(max_length=255)
    g6_drug_names = models.CharField(max_length=255)
    g6_duration = models.CharField(max_length=255)
    group7 = models.CharField(max_length=255)
    g7_drug_names = models.CharField(max_length=255)
    g7_duration = models.CharField(max_length=255)
    group8 = models.CharField(max_length=255)
    g8_drug_names = models.CharField(max_length=255)
    g8_duration = models.CharField(max_length=255)
    group9 = models.CharField(max_length=255)
    g9_drug_names = models.CharField(max_length=255)
    g9_duration = models.CharField(max_length=255)
    group10 = models.CharField(max_length=255)
    g10_drug_names = models.CharField(max_length=255)
    g10_duration = models.CharField(max_length=255)
    group11 = models.CharField(max_length=255)
    g11_drug_names = models.CharField(max_length=255)
    g11_duration = models.CharField(max_length=255)
    group12 = models.CharField(max_length=255)
    g12_drug_names = models.CharField(max_length=255)
    g12_duration = models.CharField(max_length=255)
    group13 = models.CharField(max_length=255)
    g13_drug_names = models.CharField(max_length=255)
    g13_duration = models.CharField(max_length=255)
    group14 = models.CharField(max_length=255)
    g14_drug_names = models.CharField(max_length=255)
    g14_duration = models.CharField(max_length=255)
    group15 = models.CharField(max_length=255)
    g15_drug_names = models.CharField(max_length=255)
    g15_duration = models.CharField(max_length=255)
    group16 = models.CharField(max_length=255)
    g16_drug_names = models.CharField(max_length=255)
    g16_duration = models.CharField(max_length=255)
    group17 = models.CharField(max_length=255)
    g17_drug_names = models.CharField(max_length=255)
    g17_duration = models.CharField(max_length=255)
    group18 = models.CharField(max_length=255)
    g18_drug_names = models.CharField(max_length=255)
    g18_duration = models.CharField(max_length=255)
    group19 = models.CharField(max_length=255)
    g19_drug_names = models.CharField(max_length=255)
    g19_duration = models.CharField(max_length=255)
    group20 = models.CharField(max_length=255)
    g20_drug_names = models.CharField(max_length=255)
    g20_duration = models.CharField(max_length=255)
    hormone_replacement_drugs = models.CharField(max_length=255)
    hormone_repl_duration = models.CharField(max_length=255)
    breast_self_exam = models.CharField(max_length=255)
    breast_self_exam_resourse = models.CharField(max_length=255)
    breast_screening = models.CharField(max_length=255)
    breast_screening_doctor = models.CharField(max_length=255)
    breast_screening_doctor_period = models.CharField(max_length=255)
    breast_screening_mamography = models.CharField(max_length=255)
    breast_screening_mamo_period = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.patient}"