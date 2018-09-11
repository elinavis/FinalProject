import json
import pandas as pd

res = []

options = ["Gaze direction","Gaze behavior", "Body orientation", "Body posture", "Head orientation", "Head movement",
           "Gestures", "Emotions", "Expressions"]
turn_options = ["Point at", "Look for approval of", "Show something to participant", "No action at current turn", "Additional input"]

for exp_num in range(1,2): #todo 12

    for round in [0,1]:
        e_file_path = "Elina"+ "_" + str(exp_num) + "_" + str(round)+ ".json"
        j_file_path = "Julia"+ "_" + str(exp_num) + "_" + str(round)+ ".json"

        e_data = json.load( open(e_file_path))
        j_data = json.load( open(j_file_path))


        for participant in ['A', 'C']: #todo , 'D'

            for t in range(0, 20, 5): #todo 120

                current_res = {"Exp_num": exp_num,
                               "Round": round,
                               "Participant": participant,
                               "Time": t,
                               "Turn of": e_data[participant][str(t)]["turn of"]}

                for op in options:
                    if e_data[participant][str(t)][op] == j_data[participant][str(t)][op]:
                        current_res[op] = e_data[participant][str(t)][op]
                    else:
                        current_res[op] = e_data[participant][str(t)][op] + "," + j_data[participant][str(t)][op]

                for op in turn_options:
                    val = ""
                    if op in e_data[participant][str(t)]:
                        val =  str(e_data[participant][str(t)][op])
                    if op in j_data[participant][str(t)] and val != str(j_data[participant][str(t)][op]) :
                        val += "," + str(j_data[participant][str(t)][op])

                    current_res[op] = val

                res.append(current_res)

res_df= pd.DataFrame.from_dict(res)
writer = pd.ExcelWriter('output.xlsx')
res_df.to_excel(writer,'Sheet1')
writer.save()
