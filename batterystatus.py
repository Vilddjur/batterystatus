#!/usr/bin/python
import datetime
from time import time
import json

class Py3status:

    color_good="#00FF00"
    color_bad="#FF0000"

    def check_battery(self, i3s_output_list, i3s_config):
        #Open files
        maxEnergyFile = open("/sys/class/power_supply/BAT1/energy_full", 'r')
        currentEnergyFile = open("/sys/class/power_supply/BAT1/energy_now", 'r')
        chargingFile = open("/sys/class/power_supply/BAT1/status", 'r')
        #Read files
        maxEnergy = float(maxEnergyFile.read())
        currentEnergy = float(currentEnergyFile.read())
        chargingStatus = chargingFile.read()
        #Close files
        maxEnergyFile.close()
        currentEnergyFile.close()
        chargingFile.close()

        batteryPercentage = 100.0 * currentEnergy / maxEnergy

        if(batteryPercentage < 20):
            #low
            response = {
                    'full_text':    "",
                    'color':         self.color_bad
                    }
        elif(batteryPercentage >= 85):
            #high
            response = {
            'full_text':    "",
            'color':         self.color_good
            }
        elif(batteryPercentage >= 60):
            #mid-high
            response = {
            'full_text':    "",
            'color':         self.color_good
            }
        elif(batteryPercentage >= 40):
            #mid
            response = {
                    'full_text':    "",
                    'color':         self.color_good
                    }
        elif(batteryPercentage >= 20):
            #mid-low
            response = {
            'full_text':    "",
            'color':         self.color_good
            }

        if chargingStatus != "Discharging\n":
            response['full_text'] += " "
            response['color'] = self.color_good

        response['full_text'] += " %.0f" % batteryPercentage + "%"
        return response


if __name__ == "__main__":
    from time import sleep
    x = Py3status()
    config = {
        'color_good': '#00FF00',
        'color_bad': '#FF0000',
    }
    while True:
        print(x.check_battery([], config))
        sleep(1)
