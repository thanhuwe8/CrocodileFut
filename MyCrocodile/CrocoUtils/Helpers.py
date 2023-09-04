import configparser
import datetime
from datetime import datetime



def GUIClearStats(config):
    #* Read the config
    
    #? set Date stats to today
    today = datetime.today().strftime('%Y-%m-%d')
    today_str = str(today)
    config.set("Date","app_today",today_str)
    with open("./MyCrocodile/Resources/settings.ini", 'w') as configfile:
        config.write(configfile)
    
    #? set GUI stats to 0
    default_value = '0'
    options = config.options("Statistics")
    for stat_key in options:
        options = config.set("Statistics", stat_key, default_value)
    
    with open("./MyCrocodile/Resources/settings.ini", 'w') as configfile:
        config.write(configfile)



