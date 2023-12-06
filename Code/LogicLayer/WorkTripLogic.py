from DataLayer.DataLayerAPI import DataLayerAPI
from LogicLayer.EmployeeManagerLogic import EmployeeManagerLogic
from Models.WorkTrip import WorkTrip
from datetime import datetime, timedelta

# for testing
from random import randint


class WorkTripLogic:
    def __init__(self):
        self.work_trip_data = DataLayerAPI()
        self.employee_manager = EmployeeManagerLogic()

    def generate_unique_work_trip_id(self):
        """
        Generates a unique work trip ID.
        If no work trips exist, starts from '001'.
        Otherwise, increments the maximum existing ID by 1.
        :return: A string representing the unique ID.
        """
        work_trips = self.work_trip_data.read_all_work_trips()
        if not work_trips:
            return "001"

        max_id = max(int(trip.id) for trip in work_trips)
        new_id = max_id + 1
        return str(new_id).zfill(3)

    def add_work_trip(self, destination, departure_datetime, return_datetime, crew_members=None):
        """
        Adds a new work trip to the system.
        Validates required fields before adding.

        :param destination: Destination object of the work trip.
        :param departure_datetime: Departure date and time. In string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13"
        :param return_datetime: Return date and time. In string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13"
        :param crew_members: String comma seperated list of crew member IDs (optional). f.x. "001,002,003"
        :raises ValueError: If required fields are missing or empty.
        """

        # date cannot be in the past, return_datetime cannot be less than departure_datetime
        if not destination or not departure_datetime or not return_datetime:
            raise ValueError("Required fields cannot be empty.")

        if datetime.strptime(departure_datetime, '%Y-%m-%d %H:%M') < datetime.now() or datetime.strptime(return_datetime, '%Y-%m-%d %H:%M') < datetime.now():
            raise ValueError("Departure or return date cannot be in the past.")

        if datetime.strptime(return_datetime, '%Y-%m-%d %H:%M') < datetime.strptime(departure_datetime, '%Y-%m-%d %H:%M'):
            raise ValueError("Return date cannot be before departure date.")

        # if datetimes are indeed in the correct format
        try:
            formatting_departure_datetime = datetime.strptime(
                departure_datetime, '%Y-%m-%d %H:%M')
            formatting_return_datetime = datetime.strptime(
                return_datetime, '%Y-%m-%d %H:%M')
        except ValueError:
            raise ValueError(
                "Departure and return dates must be in the format YYYY-MM-DD HH:MM.")

        # TODO: also check if employees being added are indeed employees, and if they are available when validationservice added
        if crew_members:
            crew_members_list = crew_members.split(",")
            for member in crew_members_list:
                if not self.employee_manager.is_employee(member):
                    raise ValueError(
                        f"Employee with ID {member} is not an employee.")
                elif not self.validate_employee_availability():
                    raise ValueError(
                        f"Employee with ID {member} is not available for this date.")

        if crew_members:
            if not isinstance(crew_members, str):
                raise ValueError("Crew members must be a string.")

        work_trip_id = self.generate_unique_work_trip_id()
        new_work_trip = WorkTrip(
            work_trip_id, destination, (departure_datetime), (return_datetime), crew_members)
        self.work_trip_data.add_work_trip(new_work_trip)

    def list_all_work_trips(self):
        """Returns a list of all work trips."""
        return self.work_trip_data.read_all_work_trips()

    def get_mock_destinations(self):
        return self.work_trip_data.get_mock_destinations()

    def add_crew_member(self, work_trip_id, employee_id):

        # check if employee is employee
        if not self.employee_manager.is_employee(employee_id):
            raise ValueError(
                f"Employee with ID {employee_id} is not an employee.")

        # check if employee is available
        if not self.validate_employee_availability():
            raise ValueError(
                f"Employee with ID {employee_id} is not available for this date.")

        all_work_trips = self.list_all_work_trips()
        trip_found = False  # to raise error if no trip with id
        all_work_trips_updated = []
        for trip in all_work_trips:
            if trip.id == work_trip_id:
                trip_found = True
                if trip.crew_members == "":
                    updated_crew = []
                else:
                    updated_crew = trip.crew_members.split(",")

                if employee_id not in updated_crew:
                    updated_crew.append(employee_id)

                trip.crew_members = ",".join(updated_crew)

            all_work_trips_updated.append(trip)

        if not trip_found:
            raise ValueError(
                f"WorkTrip with ID {work_trip_id} does not exist.")

        self.work_trip_data.update_work_trip_data(all_work_trips_updated)

    def validate_employee_availability(self):
        '''wait for ValidationService to be implemented'''
        return True

    def validate_trip_validity(self, work_trip):
        '''wait for ValidationService to be implemented'''
        # implement with import random 50 50 chance of returning true or false
        zero_to_one = randint(0, 1)
        if zero_to_one == 0:
            return False
        else:
            return True

    def work_trip_validity_period(self, weekly_or_daily, start_date):
        '''
        :param weekly_or_daily: weekly or daily validity period
        :param start_date: The start date of the period, in string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13"

        Returns, return: List of WorkTrip objects with additional field "validity" set to True or False.
        '''
        # should obtain weekly or daily work trips in a period, and uses the validation test to check if it is valid
        # now need to fetch all work trips in the period
        start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M')
        start_date = start_date.date()
        all_work_trips = self.list_all_work_trips()
        work_trips_in_period = []
        if weekly_or_daily.lower() == "weekly":
            end_date = start_date + timedelta(days=7)
            for trip in all_work_trips:
                if start_date <= trip.departure_datetime.date() < end_date:
                    trip.validity = self.validate_trip_validity(trip)
                    work_trips_in_period.append(trip)

        elif weekly_or_daily.lower() == "daily":
            for trip in all_work_trips:
                if trip.departure_datetime.date() == start_date:
                    trip.validity = self.validate_trip_validity(trip)
                    work_trips_in_period.append(trip)
        else:
            raise ValueError("Invalid input for weekly_or_daily")

        return work_trips_in_period

    def create_recurring_work_trips(self, work_trip_id, weekly_or_daily, number_of_recurrences):
        # takes in either weekly or daily, and number of recurrences and work trip to be repeated

        # need to first obtain dates to be repeated and then use timedelta to add 1 day to it or 7 days.

        # first need to find the corresponding trip id
        all_work_trips = self.list_all_work_trips()
        trip_found = False
        for trip in all_work_trips:
            if trip.id == work_trip_id:
                trip_found = True
                for i in range(number_of_recurrences):
                    # need to take out the seconds
                    if weekly_or_daily.lower() == "weekly":
                        new_departure_datetime = trip.departure_datetime + \
                            timedelta(days=7+7*i)
                        new_return_datetime = trip.return_datetime + \
                            timedelta(days=7+7*i)
                    elif weekly_or_daily.lower() == "daily":
                        new_departure_datetime = trip.departure_datetime + \
                            timedelta(days=1+1*i)
                        new_return_datetime = trip.return_datetime + \
                            timedelta(days=1+1*i)
                    else:
                        raise ValueError("Invalid input for weekly_or_daily")
                    self.add_work_trip(
                        trip.destination, self.correct_datetime_format(new_departure_datetime), self.correct_datetime_format(new_return_datetime))

        if not trip_found:
            raise ValueError(
                f"WorkTrip with ID {work_trip_id} not found in CSV")

    def correct_datetime_format(self, datetime_str):
        return datetime.strftime(datetime_str, '%Y-%m-%d %H:%M')
