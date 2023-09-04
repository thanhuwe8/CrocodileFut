from MyCrocodile.CrocoUtils.Packages import *
from tkinter import filedialog

'''
name	quality	rarity	position	chemistry	nationality	league	club	BuyPrice

'''

snipe_filter = ['name', 'quality', 'rarity', 'position', 'chemistry', 'nationality', 'league', 'club', 'BuyPrice']


def GenerateBuySnipe():
    example_dict = {
        'name': ['Declan Rice'], 
        'quality':['Gold'],
        'rarity':['Rare'], 
        'position':['Midfielders'],
        'chemistry':['BASIC'],
        'nationality':['England'],
        'league':['Premier League (ENG 1)'], 
        'club':['West Ham'],
        'BuyPrice':[3500]
        
    }
    result = pd.DataFrame.from_dict(example_dict)
    return(result)


def SaveBuySnipeTemplate():
    template_data = GenerateBuySnipe()
    file_path = filedialog.asksaveasfile(mode='w', defaultextension=".csv")
    template_data.to_csv(file_path)