import json
import pandas as pd

res = []

options = ["Gaze direction","Gaze behavior", "Body orientation", "Body posture", "Head orientation", "Head movement",
           "Gestures", "Emotions", "Expressions"]
turn_options = ["Point at", "Look for approval of", "Show something to participant", "No action at current turn", "Additional input"]

for exp_num in range(1,12):

    if exp_num == 6:
        continue

    for round in [0,1]:
        j_file_path = "../Julia"+ "_" + str(exp_num) + "_" + str(round)+ "ACD.json"

        j_data = json.load( open(j_file_path))


        for participant in ['A', 'C', 'D']:

            for key, item in j_data[participant].iteritems():

                item["exp_num"] = exp_num
                item["round"] = round
                item["participant"] = participant


                res.append(item)

res_df= pd.DataFrame.from_dict(res)
writer = pd.ExcelWriter('output.xlsx')
res_df.to_excel(writer,'Sheet1')
writer.save()
