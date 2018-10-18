## first 2 lines for mac only
import matplotlib
matplotlib.use('TkAgg')

import pandas as pd


#### load data
qualtrics_data = pd.read_excel("../qualtrics_data_w_questionnaire_scores_16_10.xlsx", "Qualtrics", index_col="ResponseId")

statistic_data =qualtrics_data.loc[:,['age','sex', 'study','social_skill', 'attention_switching', 'attention_to_detail',
                                      'communication', 'imagination', 'AQ_total_score']]

#### plot
statistic_data.hist(grid=True, bins=5, rwidth=0.95, color='#607c8e')
statistic_data.loc[:,['age']].boxplot()
statistic_data.loc[:,['AQ_total_score']].boxplot()
statistic_data['sex'].value_counts().plot.bar(x= 'sex',rot=0)
statistic_data['study'].value_counts().plot.bar(x= 'study',rot=0)



#### get statistic
statistic_des = statistic_data.describe()

writer = pd.ExcelWriter('../results/out.xlsx')

# Write each dataframe to a different worksheet.
statistic_des.to_excel(writer, "statistic")

# Close the Pandas Excel writer and output the Excel file.
writer.save()
