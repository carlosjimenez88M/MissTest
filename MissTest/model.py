#=============================#
#        MissTest             #
#     Daniel Jiménez M.       #
#       2023-04-02            #
#=============================#



from utils import *





## models

def check_mcar(data):
    columns = data.columns
    p_values = []
    for col1 in columns:
        for col2 in columns:
            if col1 != col2:
                cross_tab = pd.crosstab(data[col1].isna(), data[col2].isna())
                _, p_value, _, _ = chi2_contingency(cross_tab)
                p_values.append(p_value)
    
    avg_p_value = np.mean(p_values)
    if avg_p_value > 0.05:
        return "MCAR"
    else:
        return "MAR or MNAR"



def missing_values_description(data):
    try:
        miss_values = data.isna()\
            .sum()\
                .reset_index(name='Total')\
                    .sort_values(by='Total', ascending=False)\
                        .merge((data.isna().mean()*100)\
            .reset_index(name='%')\
                    .sort_values(by='%', ascending=False))
        
        missing_type = check_mcar(data)
        print(f"Missing data type: {missing_type}")

        if missing_type == "MCAR":
            miss_values_filtered = miss_values[miss_values['%'] < 3]
            for index, row in miss_values_filtered.iterrows():
                data.dropna(subset=[row['index']], inplace=True)
        return miss_values
    except:
        pass