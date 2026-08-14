import json
import os

from dotenv import load_dotenv
from azure.eventhub import EventHubProducerClient, EventData

from data import generate_uber_ride_confirmation


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

CONNECTION_STRING = os.getenv("CONNECTION_STRING")
EVENT_HUBNAME = os.getenv("EVENT_HUBNAME")


# ============================================================
# SEND EVENT TO EVENT HUB
# ============================================================

def send_to_event_hub(ride_data=None):

    producer = None

    try:

        producer = EventHubProducerClient.from_connection_string(
            CONNECTION_STRING,
            eventhub_name=EVENT_HUBNAME
        )

        # Convert Python dictionary into JSON string
        ride_json = json.dumps(ride_data)

        # Create Event Hub batch
        event_batch = producer.create_batch()

        # Create Event Hub event
        event = EventData(ride_json)

        # Add event to batch
        event_batch.add(event)

        # Send event
        producer.send_batch(event_batch)

        return "Successfully sent to Event Hub"

    except Exception as e:

        print(
            f"Error sending data to Event Hub: {str(e)}"
        )

        return False

    finally:

        if producer:
            producer.close()


# ============================================================
# LOCAL TEST
# ============================================================

if __name__ == "__main__":

    print("=" * 80)
    print("GENERATING TEST RIDE")
    print("=" * 80)

    ride = generate_uber_ride_confirmation()

    print(
        json.dumps(
            ride,
            indent=2
        )
    )

    print("\n" + "=" * 80)
    print("SENDING TEST RIDE TO EVENT HUB")
    print("=" * 80)

    result = send_to_event_hub(ride)

    print(f"Result: {result}")