import pandas as pd
df = pd.read_csv("initial-purpose-of-traffic-stop-by-drivers-sex-race-and-ethnicity.csv", sep=";")
df_race = pd.DataFrame({"Year":[], "Purpose":[], "Gender":[], "Race":[], "Count":[]})
race_list = ["White", "Black", "Native American", "Asian", "Other"]
for index, i in df.iterrows():
    for j in race_list:
        temp = pd.DataFrame({"Year":[i["Year"]], "Purpose":[i["Purpose"]], "Gender":[i["Gender"]], "Race":[j], "Count":[i[j]]})
        df_race = pd.concat([df_race, temp], ignore_index=True)

df_race = df_race.convert_dtypes()
df_race.to_csv("traffic_purpose_race.csv", sep=";")
df_race

import pandas as pd
df = pd.read_csv("initial-purpose-of-traffic-stop-by-drivers-sex-race-and-ethnicity.csv", sep=";")
df_race = pd.DataFrame({"Year":[], "Purpose":[], "Gender":[], "Ethnicity":[], "Count":[]})
race_list = ["Hispanic", "Non Hispanic"]
for index, i in df.iterrows():
    for j in race_list:
        temp = pd.DataFrame({"Year":[i["Year"]], "Purpose":[i["Purpose"]], "Gender":[i["Gender"]], "Ethnicity":[j], "Count":[i[j]]})
        df_race = pd.concat([df_race, temp], ignore_index=True)

df_race = df_race.convert_dtypes()
df_race.to_csv("traffic_purpose_ethnicity.csv", sep=";")
df_race