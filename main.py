import json

res = {}

options = ["Gaze direction","Gaze behavior", "Body orientation", "Body posture", "Head orientation", "Head movement",
           "Gestures", "Emotions", "Expressions"]
turn_options = ["Point at", "Look for approval of", "Show something to participant", "No action at current turn", "Additional input"]

for exp_num in range(1,2): #todo 12
    res[exp_num] = {}
    for round in [0,1]:
        e_file_path = "Elina"+ "_" + str(exp_num) + "_" + str(round)+ ".json"
        j_file_path = "Julia"+ "_" + str(exp_num) + "_" + str(round)+ ".json"

        e_data = json.load( open(e_file_path))
        j_data = json.load( open(j_file_path))

        res[exp_num][round] = {}

        for participant in ['A', 'C']: #todo , 'D'
            res[exp_num][round][participant] = {}

            for t in range(0,20, 5): #todo 120
                res[exp_num][round][participant][t] = {}
                res[exp_num][round][participant][t]["turn of"] = e_data[participant][str(t)]["turn of"]


                for op in options:

                    if e_data[participant][str(t)][op] == j_data[participant][str(t)][op]:
                        res[exp_num][round][participant][t][op] = e_data[participant][str(t)][op]
                    else:
                        res[exp_num][round][participant][t][op] = e_data[participant][str(t)][op] + "," +\
                                                                  j_data[participant][str(t)][op]

                for op in turn_options:
                    val = ""
                    if op in e_data[participant][str(t)]:
                        val =  str(e_data[participant][str(t)][op])
                    if op in j_data[participant][str(t)] and val != j_data[participant][str(t)][op] :
                        val += "," + str(j_data[participant][str(t)][op])

                    res[exp_num][round][participant][t][op] = val

print res

