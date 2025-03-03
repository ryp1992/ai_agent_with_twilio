from database import booking_collection
import uuid
from bson import Binary


def create_booking_uuid(passenger_name, destination, date):
    # Combine passenger info with flight details to create a unique booking ID
    unique_data = f"{passenger_name}_{destination}_{date}"

    # Generate a UUID from the unique data (using a namespace or random method)
    booking_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, unique_data)
    bson_uuid = Binary.from_uuid(booking_uuid)
    return bson_uuid


async def book_flight(**kwargs):
    passenger_name = kwargs["passenger_name"]
    from_location = kwargs["from_location"]
    to_location = kwargs["to_location"]
    date = kwargs["date"]

    booking_id = create_booking_uuid(passenger_name, destination=to_location, date=date)  # Generate a unique Booking ID

    booking_val = {
        "passenger": passenger_name,
        "from": from_location,
        "to": to_location,
        "date": date,
        "status": "Confirmed",
        "booking_id": booking_id
    }
    booking_collection.insert_document(booking_val)
    id = uuid.UUID(bytes=booking_id)
    print(f"Booking a flight for {passenger_name}, {from_location}, {to_location}, {date}")
    return f"Ticket for {passenger_name} from {from_location}, to {to_location}, on {date}, booking_id : {str(id)}"

