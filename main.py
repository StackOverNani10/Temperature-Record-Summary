import json
from abc import ABC, abstractmethod
from xml.dom import minidom


jsonFile = open("sample-files/data.json", "r") 
jsonData = json.loads(jsonFile.read())


xmlFile = minidom.parse("sample-files/data.xml")



"""
class Temperature(ABC):

    def template_method(self) -> None:
 
        self.openFile()
        self.extractData()
        self.convertData()
        self.closeFile()
        self.minData()
        self.maxData()
        self.averageData()

    def openFile(self) -> None:
        print("Temperature says: openFile")

    def readFile(self) -> None:
        print("Temperature says: readFile")

    def extractData(self) -> None:
        print("Temperature says: extractData")

    def convertData(self) -> None:
        print("Temperature says: convertData")

    def closeFile(self) -> None:
        print("Temperature says: closeFile")

    def minData(self) -> None:
        print("Temperature says: minData")

    def maxData(self) -> None:
        print("Temperature says: maxData")
    
    def averageData(self) -> None:
        print("Temperature says: averageData")

    @abstractmethod
    def readFile(self) -> None:
        pass

    @abstractmethod
    def extractData(self) -> None:
        pass


class TemperatureXML(Temperature):

    def readFile(self) -> None:
        print("TemperatureXML says: Implemented readFile")

    def extractData(self) -> None:
        print("TemperatureXML says: Implemented extractData")


class TemperatureJson(Temperature):

    def readFile(self) -> None:
        print("TemperatureJson says: Implemented readFile")

    def extractData(self) -> None:
        print("TemperatureJson says: Implemented extractData")

class TemperatureFlatFile(Temperature):

    def readFile(self) -> None:
        print("TemperatureFlatFile says: Implemented readFile")

    def extractData(self) -> None:
        print("TemperatureFlatFile says: Implemented extractData")

def client_code(Temperature: Temperature) -> None:

    Temperature.template_method()

if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(TemperatureXML())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(TemperatureJson())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(TemperatureFlatFile())
"""