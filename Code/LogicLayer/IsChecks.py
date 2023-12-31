from datetime import datetime, timedelta


class IsChecks:
    def __init__(self):
        self.punc = '-_'
        self.all_punc = '''!"#$%&\'(')*+,-./:;<=>?@[\\]^_`{|}~¨°'''

    def is_city(self, City):
        '''
        Checks if the city is valid, raises ValueError if not.
        The city must be a non-empty string of alphabetic characters and no longher than 70 characters.
        '''
        if not City or not City.replace(" ", "").isalpha():
            raise ValueError(
                "City must be a non-empty string of alphabetic characters")
        if "  " in City:
            raise ValueError("City cannot contain two or more spaces")
        if not len(City) <= 70:
            raise ValueError("City name cannot be longer than 70 characters")

    def is_airport(self, Airport):
        '''
        Checks if the airport is valid, raises ValueError if not.
        The airport must be a non-empty string of 3 alphabetic characters.
        '''
        if not Airport or not Airport.replace(" ", "").isalpha():
            raise ValueError(
                "Airport must be a non-empty string of alphabetic characters")
        if not len(Airport) == 3:
            raise ValueError(
                "Airport name must be input as the 3 letter abbreviation (ex. LAX, KEF)")
        if "  " in Airport:
            raise ValueError("Airport cannot contain two or more spaces")

    def is_country(self, Country):
        '''
        Checks if the country is valid, raises ValueError if not.
        The country must be a non-empty string of alphabetic characters and no longher than 70 characters.
        '''
        if not Country or not Country.replace(" ", "").isalpha():
            raise ValueError(
                "Country must be a non-empty string of alphabetic characters")
        if "  " in Country:
            raise ValueError("Country cannot contain two or more spaces")
        if not len(Country) <= 70:
            raise ValueError("Country name cannot be longer than 70 characters")

    def is_distance(self, Distance):
        '''
        Checks if the distance is valid, raises ValueError if not.
        The distance must be a positive integer, less than 20000 and no longer than 6 digits.
        '''
        if not Distance.isdigit():
            raise ValueError("Distance must be a positive integer")
        if not len(Distance) < 6: 
            raise ValueError("Distance cannot be longer than 6 digits")
        try:
            Distance = int(Distance)
        except ValueError:
            raise ValueError("Distance must be numeric")
        if Distance > 20000:
            raise ValueError(
                "Distance must be less than 20,000km (half the circumference of the Earth)")

    def is_travel_time(self, Travel_Time):
        '''
        Checks if the travel time is valid, raises ValueError if not.
        The travel time must be a positive integer, less than 1120 and no longer than 4 digits.
        '''
        if not Travel_Time.isdigit():
            raise ValueError("Travel Time must be a positive integer")
        if not len(Travel_Time) < 5:
            raise ValueError("Travel time cannot be longer than 4 digits")
        try:
            Travel_Time = int(Travel_Time)
        except:
            raise ValueError("Travel Time and must be numeric")
        travel_time = int(Travel_Time)
        if travel_time > 1120:
            raise ValueError(
                "Longest Commercial Flight in the world is/was 1120min, be realistic")

    def is_contact_name(self, Contact_Name):
        '''
        Checks if the contact name is valid, raises ValueError if not.
        The contact name must be a non-empty string of alphabetic characters and no longher than 70 characters.
        '''
        if not Contact_Name or not Contact_Name.replace(" ", "").isalpha():
            raise ValueError(
                "Contact Name must be a non-empty string of alphabetic characters")
        if "  " in Contact_Name:
            raise ValueError("Contact Name cannot contain two or more spaces")
        if not len(Contact_Name) <= 70:
            raise ValueError("Contact Name cannot be longer than 70 characters")

    def is_contact_phone_number(self, Contact_Phone_Number):
        '''
        Checks if the contact phone number is valid, raises ValueError if not.
        strips away "+" only from the first character if that is the case.
        The contact phone number must be a positive integer, 10 digits maximum and 3 digits minimum.
        '''
        # strip "+"" only from the first character if that is the case
        if "  " in Contact_Phone_Number:
            raise ValueError(
                "Contact Phone Number cannot contain two or more spaces")
        Contact_Phone_Number = Contact_Phone_Number.replace(" ", "")
        if Contact_Phone_Number[0:1] == "+":
            Contact_Phone_Number = Contact_Phone_Number[1:] # strips away "+" only from the first character if that is the case
        if not Contact_Phone_Number.replace(" ", "").isdigit():
            raise ValueError("Phone Number must be a positive integer")
        # checks if the number has 10 digits maximum
        if not int(Contact_Phone_Number) <= 9999999999:
            raise ValueError("Phone Number must be 10 digits maximum")
        if not int(Contact_Phone_Number) >= 100:
            raise ValueError("Phone Number must be 3 digits minimum")

        try:
            Contact_Phone_Number = int(Contact_Phone_Number.replace(" ", ""))
        except:
            raise ValueError("Phone Number must be numeric")

    def is_home_phone(self, home_phone):
        '''
        Checks if the home phone number is valid, raises ValueError if not.
        calls is_contact_phone_number() function, to check if the number is valid.
        '''
        if not home_phone:
            pass
        else:
            home_phone = self.is_contact_phone_number(home_phone)

    def is_name(self, Name):
        '''
        Checks if the name is valid, raises ValueError if not.
        The name must be a non-empty string of alphabetic characters and no longher than 70 characters.
        '''
        if not Name:
            raise ValueError("Name must be a non-empty string")
        if not Name.replace(" ", "").isalpha():
            raise ValueError(
                "Get out of here 'X Æ A-12' We dont allow numbers or symbols in our names")
        if "  " in Name:
            raise ValueError("Name cannot contain two or more spaces")
        if not len(Name) <= 70:
            raise ValueError("Name cannot be longer than 70 characters")

    def is_current_location(self, Current_Location):
        '''
        Checks if the current location is valid, raises ValueError if not.
        The current location must be a non-empty string of alphabetic characters and less than 20 characters.
        '''
        if not Current_Location or not Current_Location.replace(" ", "").isalpha():
            raise ValueError(
                "Current Location must be a non-empty string of alphabetic characters")
        if not len(Current_Location) < 20:
            raise ValueError("Manufacturer must be less than 20 characters")
        if "  " in Current_Location:
            raise ValueError(
                "Current location cannot contain two or more spaces")

    def is_social_security_number(self, social_security_number):
        '''
        Checks if the social security number is valid, raises ValueError if not.
        The social security number must be a positive integer, 10 digits long and end in either '0' or '9'.
        The social security number must also be a valid date, not in the future and not too old, 
        this function checks for example if the person is older than 130 years old or younger than 13 years old.
        The function uses datetime to check if the date is valid.
        '''
        if not social_security_number.replace("-", "").replace(" ", "").isdigit():
            raise ValueError(
                "social_security_number must be a positive integer")
        if "  " in social_security_number:
            raise ValueError("Social security number cannot contain two or more spaces")
        social_security_number = social_security_number.replace(" ", "").replace("-", "")
        try:
            social_security_number_int = int(social_security_number)
        except:
            raise ValueError("Social security number must be numeric")
        if len(social_security_number) != 10:
            raise ValueError("Social security number must be 10 digits")
        
        day = social_security_number[0:2]
        month = social_security_number[2:4]
        year = social_security_number[4:6]
        last_digit = social_security_number[-1]
        if last_digit == '0':
            year = f"20{year}"
        elif last_digit == '9':
            year = f"19{year}"
        else:
            raise ValueError("Social security number must end in either '0' or '9'")
        datetime_ssn = datetime(int(year), int(month), int(day), 0,0)
        now = datetime.now()
        now_date = now.date()
        datetime_ssn = datetime_ssn.date()
        if datetime_ssn > now_date:
            raise ValueError("Birth date in social_security_number is in the future")
        if datetime_ssn + timedelta(4749) > now_date:
            raise ValueError("Birth date in social_security_number is too young")
        if datetime_ssn + timedelta(36525) < now_date:
            raise ValueError("Birth date in social_security_number is way too old. ")

    def is_type(self, Type):
        '''
        Checks if the type is valid, raises ValueError if not.
        The type must be a non-empty string of alphabetic characters and less than 15 characters.
        '''
        if not Type:
            raise ValueError("Type must be a non-empty string")
        if "  " in Type:
            raise ValueError("Type cannot contain two or more spaces")
        if len(Type) > 15:
            raise ValueError("Type_str cannot be longer than 15 characters")

    def is_manufacturer(self, Manufacturer):
        '''
        Checks if the manufacturer is valid, raises ValueError if not.
        The manufacturer must be a non-empty string of alphabetic characters and less than 20 characters.
        This function also checks if the manufacturer is only punctuation.
        '''
        if not Manufacturer:
            raise ValueError("Manufacturer must be a non-empty string")
        if "  " in Manufacturer:
            raise ValueError("Manufacturer cannot contain two or more spaces")
        if not Manufacturer.strip(self.punc):
            raise ValueError("Manufacturer cannot be only punctuation")
        if len(Manufacturer) > 20:
            raise ValueError(
                "Manufacturer name cannot be longer than 20 characters")

    def is_capacity(self, Capacity):
        '''
        Checks if the capacity is valid, raises ValueError if not.
        The capacity must be a positive integer, less than 853 and less than 4 digits.
        '''
        if not Capacity.isdigit():
            raise ValueError("Capacity must be a positive integer")
        if len(Capacity) > 4: 
            raise ValueError("Capacity must be maximum 3 digits")
        try:
            Capacity = int(Capacity)
        except ValueError:
            raise ValueError("Capacity must be numeric")
        if Capacity > 853:
            raise ValueError("No plane in the world has a seat capacity of more than 853")


    def is_address(self, address):
        '''
        Checks if the address is valid, raises ValueError if not.
        The address must be a non-empty string and less than 20 characters.
        '''
        if not address:
            raise ValueError("Address must be a non-empty string")
        if "  " in address:
            raise ValueError("Address cannot contain two or more spaces")
        if len(address) > 20:
            raise ValueError("Address too long")

    def is_email(self, Email):
        '''
        Checks if the email is valid, raises ValueError if not.
        The email must be a non-empty string and less than 20 characters.
        The email must also contain "." and "@".
        '''
        if not Email:
            raise ValueError("Email must be a non-empty string")
        if " " in Email:
            raise ValueError("Email cannot contain spaces")
        if not "@" in Email:
            raise ValueError('Email must contain "@"')
        if not "." in Email:
            raise ValueError('Email must contain "."')
        if self.all_punc in Email.strip("@."):
            if len(Email) > 20:
                raise ValueError("Email is too long")

    def departure_date_past(self, departure_date):
        '''
        Checks if the departure date is valid, raises ValueError if not.
        The departure date must be a valid date, not in the past.
        The function uses datetime to check if the date is valid.
        '''
        given_datetime = datetime.strptime(departure_date, "%Y-%m-%d")
        now = datetime.now()
        now_date = now.date()
        given_datetime = given_datetime.date()
        if given_datetime < now_date:
            raise ValueError("Date cannot be in the past")

    def departure_datetime_past(self, departure_datetime):
        '''
        Checks if the departure datetime is valid, raises ValueError if not.
        The departure datetime must be a valid datetime, not in the past.
        The function uses datetime to check if the datetime is valid.
        '''
        given_datetime = datetime.strptime(
            departure_datetime, "%Y-%m-%d %H:%M")
        now = datetime.now()
        if given_datetime < now:
            raise ValueError("Date cannot be in the past")

    def is_return_time_dd_rd(self, input_departure_day, input_return_day):
        '''
        Checks if the return datetime is valid, raises ValueError if not.
        The return datetime must be a valid datetime, not in the past.
        The return datetime must also be after the departure datetime.
        The function uses the datetime function to check if the datetime is valid.
        '''
        given_datetime = datetime.strptime(
            input_departure_day, "%Y-%m-%d %H:%M")
        given_returntime = datetime.strptime(
            input_return_day, "%Y-%m-%d %H:%M")
        if not given_datetime < given_returntime:
            raise ValueError("Return time has to be after departure time")

    def is_date(self, date):
        '''
        Checks if the date is valid, raises ValueError if not.
        The date must be a valid date.
        The function uses datetime to check if the date is valid.
        '''
        date = date.split('-')
        if not len(date) == 3:
            raise ValueError('Date has to be writen in the correct format (YYYY-MM-DD)')
        if not date[0].isdigit or not date[1].isdigit or not date[2].isdigit:
            raise ValueError('Date has to be (YYYY-MM-DD) with valid integers between the dashes ("-")')

    def flight_sched_destination_validation(self, departure_datetime, return_datetime, destination_obj):
        '''
        Checks if the destination is valid, raises ValueError if not.
        The function uses datetime to check if the destination is valid.
        The function also checks if the time between flights is too short and checks if the destination is the HQ.
        '''
        if int(destination_obj.id) == 1:
            raise ValueError("Cannot fly to HQ")

        if not destination_obj:
            raise ValueError("Destination does not exist")
        difference = datetime.strptime(
            return_datetime, "%Y-%m-%d %H:%M") - datetime.strptime(departure_datetime, "%Y-%m-%d %H:%M")
        destination_travel_time = destination_obj.travel_time
        if difference < (timedelta(minutes=int(destination_travel_time)*1) + timedelta(hours=0.99)):
            raise ValueError(
                "Time between flights is too short, allow 1 hr overhead to refuel plane abroad.")
