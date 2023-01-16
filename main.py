import os
import json
import pandas as pd
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

class Temperature(ABC):

    def template_method(self):
 
        self.ExtractData()
        self.Procces()
    
    @abstractmethod
    def ExtractData(self):
        pass

    @abstractmethod
    def Procces(list):
        pass

class TemperatureXML(Temperature):

    def ExtractData(self):
        mytree = ET.parse("sample-files/data.xml")
        myroot = mytree.getroot()
        listdata = []
        total = 0
        for data in myroot.findall('row'):
            meassure = data.findtext('meassure')
            meassure = float(meassure)
            total += meassure
            listdata.append(meassure)
        return listdata, total

    def Procces(self):
        listdata, total = self.ExtractData()
        vMin = min(listdata)
        vMax = max(listdata)
        aveg = total/len(listdata)
        print("data: ", listdata, "\nmin: ", vMin, "\nmax: ", vMax, "\naveg: ", round(aveg, 2))
        sendDataOut(vMin, vMax, aveg)

class TemperatureJson(Temperature):

    def ExtractData(self):
        with open("sample-files/data.json", "r") as jsonFile:
            jsonData = json.load(jsonFile)
            listdata = []
            for data in jsonData:
                listdata.append(data.get("meassure"))
        return listdata

    def Procces(self):
        listdata = self.ExtractData()
        vMin = min(listdata)
        vMax = max(listdata)
        aveg = sum(listdata)/len(listdata)
        print("data: ", listdata, "\nmin: ", vMin, "\nmax: ", vMax, "\naveg: ", round(aveg, 2))
        sendDataOut(vMin, vMax, aveg)

class TemperatureFlatFile(Temperature):

    def ExtractData(self):
        flatData = pd.read_csv("sample-files/data.csv", sep="|", usecols=["Meassure"])
        listdata = []
        data = flatData.iloc[:].values
        for row in data:
            listdata.append(row[0])
        return listdata

    def Procces(self):
        listdata = self.ExtractData()
        vMin = min(listdata)
        vMax = max(listdata)
        aveg = sum(listdata)/len(listdata)
        print("data: ", listdata, "\nmin: ", vMin, "\nmax: ", vMax, "\naveg: ", round(aveg, 2))
        sendDataOut(vMin, vMax, aveg)

def sendDataOut(vMin, vMax, aveg):
    dataOut = { "min": vMin, "max": vMax, "aveg": round(aveg, 2) }
    with open("sample-files/data.out.json", "w") as jsonOutFile:
        json.dump(dataOut, jsonOutFile)

def client_code(Temperature: Temperature):

    Temperature.template_method()

if __name__ == "__main__":
    
    notValid = True
    while(notValid):
        
        print("What type of file you want to examinate\ntype: flatfile | xmlfile | jsonfile")
        option = input("option: ")

        if option == "flatfile":
            os.system("cls")
            print("Extract Flat file result:")
            client_code(TemperatureFlatFile())
            input("\nPress Enter to close program")
            notValid = False
        elif option == "xmlfile":
            os.system("cls")
            print("Extract XML file result:")
            client_code(TemperatureXML())
            input("\nPress Enter to close program")
            notValid = False
        elif option == "jsonfile":
            os.system("cls")
            print("Extract JSON file result:")
            client_code(TemperatureJson())
            input("\nPress Enter to close program")
            notValid = False
        else:
            os.system("cls")
            print("Put a valid type of file")
