import csv
import os
from Models.AirplaineModel import Airplaine



class AirplaineData:
    def __init__(self):
        self.file_name = "Datalayer/Respository/airplaines.csv"
    def get_all_airplaines(self):
        ret_lis = []
        with open('airplaines.csv', newline='', endcoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_lis.append((row["name"], row["CurrentLocation"], row["Type"], row["Manufacturer"], row["Capacity"]))
            return ret_lis
        
        """Initialize the AirplaineData with the path to CSV file with airplaine data"""
        self.filename = filename
        self.EnsureFileExists()

    def EnsureFileExists(self):
        self.CreateFileIfNotExists(self.AirplaineFilename, ['NameOfPlane', 'CurrentLocation', 'Type','Manufacturer', 'Capacity',])

    def CreateFileIfNotExists(self, filename, fieldnames):
        if not os.path.exists(filename):
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

    def ReadAllAirplaines(self):
        """
        Read all Airplaines from the Airplaine CSV file and return them as a list of Airplaine objects.
        :return: List of Airplaine objects.
        """
        Airplaines = []
        try:
            with open(self.AirPlaineFilename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    Airplaines.append(Airplaine(**row))
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The file {self.AirplaineFilename} does not exist.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {e}")
        return Airplaines

    def AddAirplaine(self, airplaine):
        """
        Add a new airplaine to the CSV file.
        :param airplaine: Airplaine object to be added.
        """

        try:
            with open(self.AirplaineFilename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file, fieldnames=airplaine.__dict__.keys())
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(airplaine.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")

    def ModifyAirplaineData(self, UpdatedAirplaines):
        """
        Write the updated list of airplaines to the CSV file.
        :param UpdatedAirplaines: List of airplaine objects with updated information.
        """
        try:
            with open(self.airplaine_filename, mode='w', newline='', encoding='utf-8') as file:
                if UpdatedAirplaines:
                    writer = csv.DictWriter(
                        file, fieldnames=UpdatedAirplaines[0].__dict__.keys())
                    writer.writeheader()
                    for emp in UpdatedAirplaines:
                        writer.writerow(emp.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")

    