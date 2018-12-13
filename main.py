import pandas as pd

#load data
original_data = pd.read_csv('data.tsv', sep ="\t")



############################## AQ
score_dict={}

#parametres:
# 1 on agree
questions_high=[1, 2, 4, 5, 6, 7,9, 12, 13, 16, 18, 19, 20, 21, 22, 23, 26, 33, 35, 39, 41,42, 43, 45, 46]
# 1 on disagree
questions_low=[3, 8, 10, 11, 14, 15, 17, 24, 25, 27, 28, 29, 30, 31, 32,34, 36, 37, 38, 40, 44, 47, 48, 49, 50]

social_skill=[1,11,13,15,22,36,44,45,47,48]
attention_switching=[2,4,10,16,25,32,34,37,43,46]
attention_to_detail=[5,6,9,12,19,23,28,29,30,49]
communication=[7,17,18,26,27,31,33,35,38,39]
imagination=[3,8,14,20,21,24,40,41,42,50]

#go over every subject:
for index, row in original_data.iterrows():
    score_dict[index]={}
    total_score=0
    social_skill_score=0
    attention_switching_score=0
    attention_to_detail_score=0
    communication_score=0
    imagination_score=0


    #go over every question:
    for question in range(1,51):
        #calculate the score:

        if question in questions_high:
            #agree
            if "dis" not in row["AQ_"+str(question)].lower():
                total_score+=1

                if question in social_skill:
                    social_skill_score+=1

                elif question in attention_switching:
                    attention_switching_score+=1

                elif question in attention_to_detail:
                    attention_to_detail_score += 1

                elif question in communication:
                    communication_score += 1

                elif question in imagination:
                    imagination_score += 1

        elif question in questions_low:
            if "dis" in row["AQ_" + str(question)].lower():
                total_score+=1

                if question in social_skill:
                    social_skill_score += 1

                elif question in attention_switching:
                    attention_switching_score += 1

                elif question in attention_to_detail:
                    attention_to_detail_score += 1

                elif question in communication:
                    communication_score += 1

                elif question in imagination:
                    imagination_score += 1



    score_dict[index]['AQ_total_score']=total_score
    score_dict[index]['social_skill'] = social_skill_score
    score_dict[index]['attention_switching'] = attention_switching_score
    score_dict[index]['attention_to_detail'] = attention_to_detail_score
    score_dict[index]['communication'] = communication_score
    score_dict[index]['imagination'] = imagination_score



# crate df:
aq_score_df= pd.DataFrame.from_dict(score_dict, orient='index')

aq_score_df=aq_score_df[['social_skill','attention_switching','attention_to_detail','communication','imagination','AQ_total_score']]


############################## NARS
# Sub-scale 1: Negative Attitudes toward Situations and Interactions with Robots. Items - 4,7,8,9,10,12
# Sub-scale 2: Negative Attitudes toward Social Influence of Robots. Items - 1,2,11,13,14
# Sub-scale 3: Negative Attitudes toward Emotions in Interaction with Robots. Items - 3r,5r,6r

NARS_titles = []
for i in range(1, 15):
    strNARS_i = 'NARS_' + str(i)
    NARS_titles.append(strNARS_i)

df_NARS = original_data[NARS_titles]
df_NARS= df_NARS.replace("Strongly disagree", "1")
df_NARS= df_NARS.replace("Disagree", "2")
df_NARS= df_NARS.replace("Neither agree nor disagree", "3")
df_NARS= df_NARS.replace("Agree", "4")
df_NARS= df_NARS.replace("Strongly agree", "5")
NARS_sub1_mean = df_NARS[["NARS_4", "NARS_7", "NARS_8", "NARS_9", "NARS_10", "NARS_12"]].astype(int).mean(axis=1).to_frame("NARS_sub1_mean")
NARS_sub2_mean = df_NARS[["NARS_1", "NARS_2", "NARS_11", "NARS_13", "NARS_14"]].astype(int).mean(axis=1).to_frame("NARS_sub2_mean")
NARS_sub3_mean = (6 - df_NARS[["NARS_3", "NARS_5", "NARS_6"]].astype(int).mean(axis=1)).to_frame("NARS_sub3_mean")
NARS_sub1_sum = df_NARS[["NARS_4", "NARS_7", "NARS_8", "NARS_9", "NARS_10", "NARS_12"]].astype(int).sum(axis=1).to_frame("NARS_sub1_sum")
NARS_sub2_sum = df_NARS[["NARS_1", "NARS_2", "NARS_11", "NARS_13", "NARS_14"]].astype(int).sum(axis=1).to_frame("NARS_sub2_sum")
NARS_sub3_sum = (18 - df_NARS[["NARS_3", "NARS_5", "NARS_6"]].astype(int).sum(axis=1)).to_frame("NARS_sub3_sum")


############################## GODSPEED

df_godspeed_1 = original_data[["Godspeed_" + str(i) for i in range(1, 6)]].astype(int).mean(axis=1).to_frame("GODSPEED 1: ANTHROPOMORPHISM")
df_godspeed_2 = original_data[["Godspeed_" + str(i) for i in range(6, 12)]].astype(int).mean(axis=1).to_frame("GODSPEED 2: ANIMACY")
df_godspeed_3 = original_data[["Godspeed_" + str(i) for i in range(12, 17)]].astype(int).mean(axis=1).to_frame("GODSPEED 3: LIKEABILITY")

df_godspeed = original_data[["Godspeed_" + str(i) for i in range(17, 25)]]
df_godspeed["Godspeed_21"] = 6 - df_godspeed["Godspeed_21"].astype(int)
df_godspeed["Godspeed_23"] = 6 - df_godspeed["Godspeed_23"].astype(int)

df_godspeed_4 = df_godspeed[["Godspeed_" + str(i) for i in range(17, 22)]].astype(int).mean(axis=1).to_frame("GODSPEED 4: PERCEIVED INTELLIGENCE")
df_godspeed_5 = df_godspeed[["Godspeed_" + str(i) for i in range(22, 25)]].astype(int).mean(axis=1).to_frame("GODSPEED 5: PERCEIVED SAFETY")

############################## SCS
SCS_titles = []
for i in range(1, 15):
    strSCS_i = 'SCS_' + str(i)
    SCS_titles.append(strSCS_i)

df_CSC = original_data[SCS_titles]
df_CSC= df_CSC.replace("Strongly disagree", "1")
df_CSC= df_CSC.replace("Disagree", "2")
df_CSC= df_CSC.replace("Agree", "3")
df_CSC= df_CSC.replace("Strongly agree", "4")

SCS_mean = df_CSC.astype(int).mean(axis=1).to_frame("SCS_mean")
SCS_G_mean = df_CSC[["SCS_" + str(i) for i in range(1, 6)]].astype(int).mean(axis=1).to_frame("SCS_G_mean")
SCS_C_mean = df_CSC[["SCS_" + str(i) for i in range(8, 13)]].astype(int).mean(axis=1).to_frame("SCS_C_mean")
SCS_sum = df_CSC.astype(int).sum(axis=1).to_frame("SCS_sum")
SCS_G_sum = df_CSC[["SCS_" + str(i) for i in range(1, 6)]].astype(int).sum(axis=1).to_frame("SCS_G_sum")
SCS_C_sum = df_CSC[["SCS_" + str(i) for i in range(8, 13)]].astype(int).sum(axis=1).to_frame("SCS_C_sum")



############################## export to excel
data_fm = pd.concat([original_data[["ResponseId", "exp number", "participant number", "participant letter", "age", "sex"]],
                     aq_score_df,
                     NARS_sub1_mean, NARS_sub2_mean, NARS_sub3_mean, NARS_sub1_sum, NARS_sub2_sum, NARS_sub3_sum,
                     df_godspeed_1, df_godspeed_2, df_godspeed_3,df_godspeed_4, df_godspeed_5,
                     SCS_mean, SCS_G_mean, SCS_C_mean, SCS_sum, SCS_G_sum, SCS_C_sum], axis=1)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('questionnaires.xlsx')

# Write each dataframe to a different worksheet.
data_fm.to_excel(writer)


# Close the Pandas Excel writer and output the Excel file.
writer.save()
