# This section deals with the wrangle function that pulls data from the excel file, cleans it and returns the data frame
import pandas as pd
import numpy as np

kenya_county_coords = [
    ("Mombasa", -4.0435, 39.6682), ("Kwale", -4.1737, 39.4521), ("Kilifi", -3.6305, 39.8499), ("Tana River", -1.5575, 40.0687), ("Lamu", -2.2717, 40.9020),   ("Taita-Taveta", -3.3167, 38.3167), ("Garissa", -0.4536, 39.6401), ("Wajir", 1.7471, 40.0573), ("Mandera", 3.9366, 41.8670), ("Marsabit", 2.3347, 37.9909),
    ("Isiolo", 0.3556, 37.5833), ("Meru", 0.0470, 37.6496), ("Tharaka-Nithi", -0.2966, 37.7233), ("Embu", -0.5388, 37.4574), ("Kitui", -1.3667, 38.0167),
    ("Machakos", -1.5177, 37.2634), ("Makueni", -1.8031, 37.6203), ("Nyandarua", -0.1807, 36.5220), ("Nyeri", -0.4201, 36.9476), ("Kirinyaga", -0.6591, 37.3827), ("Murang'a", -0.7210, 37.1526), ("Kiambu", -1.1714, 36.8356), ("Turkana", 3.1167, 35.6000), ("West Pokot", 1.2389, 35.1119), ("Samburu", 0.5526, 37.5342), ("Trans-Nzoia", 1.0567, 34.9507), ("Uasin Gishu", 0.5143, 35.2698), ("Elgeyo-Marakwet", 0.8022, 35.5360), ("Nandi", 0.1833, 35.1261), ("Baringo", 0.4667, 35.9667), ("Laikipia", 0.3606, 36.7819), ("Nakuru", -0.3031, 36.0800), ("Narok", -1.0783, 35.8617), ("Kajiado", -1.8523, 36.7768), ("Kericho", -0.3670, 35.2863), ("Bomet", -0.7813, 35.3416), ("Kakamega", 0.2827, 34.7519), ("Vihiga", 0.0762, 34.7222), ("Bungoma", 0.5635, 34.5606), ("Busia", 0.4600, 34.1110),
    ("Siaya", 0.0612, 34.2881), ("Kisumu", -0.0917, 34.7680), ("Homa Bay", -0.5273, 34.4571), ("Migori", -1.0634, 34.4731), ("Kisii", -0.6773, 34.7796),
("Nyamira", -0.5633, 34.9351), ("Nairobi", -1.2921, 36.8219)
]

class Repository:
    def __init__(self, filepath):
        self.filepath = filepath
        
    def wrangle(self):
        # synthetic data was used
        df = pd.read_excel(self.filepath)
        coords_df = pd.DataFrame(kenya_county_coords, columns=["County", "Latitude", "Longitude"])
        df = df.merge(coords_df, on="County", how="left")
        ## Drop high and low cardinatlity columns
        drop_cols = ["TS", "ConsentStudy", "ConsentProceed", "AccCount", "VehCondition",
                     "Preventable", "LicenseType", "SeatBelt", "AccCause", "RiskSelf", "VehAge", 
                     "TiredMonth","MedsAlert", "RushHours", "LastService",  "Accident5y", "TrainingType"]
    
        # Creating a binary classification for the target
        acc_involve = {
        "Yes" : 1,
        "No" : 0
        }
        
        df["AccOccur"] = df["Accident5y"].map(acc_involve)
        df["AccOccur"].head()
    
        # dropping the "Accident5y"
        #drop_cols.append("Accident5y")
    
        # Only fill the missing (NaN) values - very safe & common approach
    
        proportions = df['OVC'].value_counts(normalize=True)
        
        # Where is NaN → we fill
        mask_missing = df['OVC'].isna()
        
        df.loc[mask_missing, 'OVC'] = np.random.choice(
            proportions.index,
            size=mask_missing.sum(),
            p=proportions.values
        )
        # create a function to populate the agegrp column
        import random
        random.seed(42)
        groupA_num = int(1014 * 0.15)
        groupB_num = int(1014 * 0.61)
        groupC_num = int(1014 * 0.20) + 1
        groupD_num = int(1014 * 0.04) + 1
        
        groupA = (18, 25)
        groupB = (26, 35)
        groupC = (36, 45)
        groupD = (46, 55)
        AgeGrp = []
        def generate_age_group(group_size, age_range):
            min_age, max_age = age_range
            return[random.randint(min_age, max_age) for _ in range(group_size)]
        
        AgeGrp = []
        AgeGrp.extend(generate_age_group(groupA_num, groupA))
        AgeGrp.extend(generate_age_group(groupB_num, groupB))
        AgeGrp.extend(generate_age_group(groupC_num, groupC))
        AgeGrp.extend(generate_age_group(groupD_num, groupD))
        
          
        df["AgeGrp"] = AgeGrp
    
        # Yrs driven should be a number since you can get the number of years you had a license ecitizen
        set_age = 18
        mask = df["AgeGrp"] - set_age
        mask.head()
        df["YrsDrive"] = mask
        df.head()
    
        # DriveFrequency should also be a scale where barely is 1 and occasionally 5
        DriveFreq = {
            "Daily" : 5,
            "Several Times a week" : 3,
            "Occasionally" : 2,
            " Rarely" : 1
        }
        
        df["DriveFreq"] = df["DriveFreq"].map(DriveFreq)
    
        # vehicle age should be a number since the log book has the manufacturing date
        vehicleAge = {
            "Less than 5 years": 3,
            "5-10 years": 7,
            "More than 10 years": 12
        }
        df["VehAge"] = df["VehAge"].map(vehicleAge)
    
        # overall vehicle condition should be converted to a scale where 1 is fair, 2 is good and 3 is excellent
        OverallVehicle = {
            "Poor" : 1,
            "Fair" : 2,
            "Good" : 3,
            "Excellent" : 4
        }
        
        df["OVC"] = df["OVC"].map(OverallVehicle)
    
        # hesl speed limit & hphone exceeding should also be a range from 1 to 5
        speed_phone = {
            "Never" : 1,
            "Rarely" : 2,
            "Sometimes": 3,
            "Often" : 4
        }
        
        df["HESL"] = df["HESL"].map(speed_phone)
        df["HPhone"] = df["HPhone"].map(speed_phone)
    
        # sleephrs should be a number between 4 and 8 hours
        sleephrs = {
            "less than 4 hours" : 3,
            "4-6 hours" : 5,
            "6-8 hours" : 7,
            "More than 8 hours" : 9
        }
        df["SleepHrs"] = df["SleepHrs"].map(sleephrs)
    
        # convert tired month from yes & no to 1 or 0, 1 for yes and 0 for no
        tiredMonth = {
            "yes" : 1,
            "no" : 0
        }
        
        df["TiredMonth"] = df["TiredMonth"].map(tiredMonth)
        # have you ever drunk driven no to be 0 and prefer not to say or yes to be 1
        drunkdriven = {
            "yes" : 1,
            "no" : 0,
            "Prefer not to say" : 1
        }
        df["Alcohol6h"] = df["Alcohol6h"].map(drunkdriven)
    
        # medicalert no to be 0 and 1 to be yes
        medication = {
            "yes" : 1,
            "no" : 0,
            "Not sure" : 1
        }
        
        df["MedsAlert"] = df["MedsAlert"].map(medication)
    
        # Typical road condition bad to be 1, fair to be 2, good to be 3, excellent to be 4
        # roadCon = {
        #     "Poor": 1,
        #     "Fair" : 2,
        #     "Good" : 3
            
        # }
        
        # df["RoadCond"] = df["RoadCond"].map(roadCon)
    
        # road lighting quality poor to be 1, fair to be 2, good to be 3, excellent to be 4
        roadLight = {
            "Poor": 1,
            "None" : 0,
            "Good" : 2
            
        }
        
        df["Lighting"] = df["Lighting"].map(roadLight)
    
        # typical traffic level heavy is a 3, moderate is a 2, low is a 1
        # weather = {
        #     "Clear" : 1,
        #     "Rainy" : 2,
        #     "Foggy" : 3,
        #     "Dusty" :4
        # }
        # df["Weather"] = df["Weather"].map(weather)
        # # how would you rate visibility and clarity very poor 1, poor 2, adequate 3, good 4, very good 5
        # visibility = {
        #     "Very poor (signs are missing or unclear)" : 1,
        #     "Poor" : 2,
        #     "Adequate" : 3,
        #     "Good" : 4,
        #     "Very good (clear and easy to follow)" : 5 
        # }
        # df["SignVis"] = df["SignVis"].map(visibility)
    
        total_rows = len(df)
        male_count = int(total_rows * 0.8)
        female_count = total_rows - male_count
        
        genders = ["Male"] * male_count + ["Female"] * female_count
        random.shuffle(genders)
        df["Gender"] = genders
                
        df.drop(columns=drop_cols, inplace=True)
        return df