from LogicLayer.LogicLayerAPI import LogicLayerAPI
from Models.WorkTrip import WorkTrip
from datetime import datetime, timedelta


def main():
    work_trip_logic = LogicLayerAPI()

    destinations = work_trip_logic.get_mock_destinations()

    for dest in destinations:
        print(dest)

    work_trip_logic.add_work_trip(
        destinations[0], '2032-11-14 14:32', '2032-11-14 17:32')

    work_trip_logic.add_work_trip(
        destinations[1], '2033-11-14 14:32', '2034-11-14 17:32', '001,002,003')

    work_trips = work_trip_logic.list_all_work_trips()

    for trip in work_trips:
        print(trip.__dict__)

    print('adding employee to worktrip')

    work_trip_logic.add_crew_member("001", "001")
    work_trip_logic.add_crew_member("001", "002")

    work_trips = work_trip_logic.list_all_work_trips()

    for trip in work_trips:
        print(trip.__dict__)

    # hopefully no problem regarding datetype
    print("testing creting reccurring worktrips daily for 15 days")
    work_trip_logic.create_recurring_work_trips("001", "daily", 15)

    print("\n lets see if it was created correctly")
    work_trips = work_trip_logic.list_all_work_trips()
    for trip in work_trips:
        print(trip.__dict__)

    print("\n testing checking validity of trips")
    work_trip_validity_test = work_trip_logic.work_trip_validity_period(
        "weekly", '2032-11-15 14:32')

    for trip in work_trip_validity_test:
        print(f"{trip.id} validity: {trip.validity}")


if __name__ == "__main__":
    main()