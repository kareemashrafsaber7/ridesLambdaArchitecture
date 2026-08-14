import random
import uuid
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()


# ============================================================
# STATIC REFERENCE MAPPINGS
# ============================================================

VEHICLE_TYPE_MAPPING = [
    {
        "vehicle_type_id": 1,
        "vehicle_type": "UberX",
        "description": "Standard",
        "base_rate": 2.50,
        "per_mile": 1.75,
        "per_minute": 0.35
    },
    {
        "vehicle_type_id": 2,
        "vehicle_type": "UberXL",
        "description": "Extra Large",
        "base_rate": 3.50,
        "per_mile": 2.25,
        "per_minute": 0.45
    },
    {
        "vehicle_type_id": 3,
        "vehicle_type": "UberPOOL",
        "description": "Shared Ride",
        "base_rate": 2.00,
        "per_mile": 1.50,
        "per_minute": 0.30
    },
    {
        "vehicle_type_id": 4,
        "vehicle_type": "Uber Comfort",
        "description": "Comfortable",
        "base_rate": 3.00,
        "per_mile": 2.00,
        "per_minute": 0.40
    },
    {
        "vehicle_type_id": 5,
        "vehicle_type": "Uber Black",
        "description": "Premium",
        "base_rate": 5.00,
        "per_mile": 3.50,
        "per_minute": 0.60
    }
]


PAYMENT_METHOD_MAPPING = [
    {
        "payment_method_id": 1,
        "payment_method": "Credit Card",
        "is_card": True,
        "requires_auth": True
    },
    {
        "payment_method_id": 2,
        "payment_method": "Debit Card",
        "is_card": True,
        "requires_auth": True
    },
    {
        "payment_method_id": 3,
        "payment_method": "Digital Wallet",
        "is_card": False,
        "requires_auth": False
    },
    {
        "payment_method_id": 4,
        "payment_method": "Cash",
        "is_card": False,
        "requires_auth": False
    }
]


RIDE_STATUS_MAPPING = [
    {
        "ride_status_id": 1,
        "ride_status": "Completed",
        "is_completed": True
    },
    {
        "ride_status_id": 2,
        "ride_status": "Cancelled",
        "is_completed": False
    }
]


VEHICLE_MAKE_MAPPING = [
    {"vehicle_make_id": 1, "vehicle_make": "Toyota"},
    {"vehicle_make_id": 2, "vehicle_make": "Honda"},
    {"vehicle_make_id": 3, "vehicle_make": "Ford"},
    {"vehicle_make_id": 4, "vehicle_make": "Chevrolet"},
    {"vehicle_make_id": 5, "vehicle_make": "Nissan"},
    {"vehicle_make_id": 6, "vehicle_make": "BMW"},
    {"vehicle_make_id": 7, "vehicle_make": "Mercedes"}
]


CITY_MAPPING = [
    {"city_id": 1, "city": "New York", "state": "NY", "region": "Northeast"},
    {"city_id": 2, "city": "Los Angeles", "state": "CA", "region": "West"},
    {"city_id": 3, "city": "Chicago", "state": "IL", "region": "Midwest"},
    {"city_id": 4, "city": "Houston", "state": "TX", "region": "South"},
    {"city_id": 5, "city": "Phoenix", "state": "AZ", "region": "Southwest"},
    {"city_id": 6, "city": "Philadelphia", "state": "PA", "region": "Northeast"},
    {"city_id": 7, "city": "San Antonio", "state": "TX", "region": "South"},
    {"city_id": 8, "city": "San Diego", "state": "CA", "region": "West"},
    {"city_id": 9, "city": "Dallas", "state": "TX", "region": "South"},
    {"city_id": 10, "city": "San Jose", "state": "CA", "region": "West"}
]


CANCELLATION_REASON_MAPPING = [
    {
        "cancellation_reason_id": 1,
        "cancellation_reason": "Driver cancelled"
    },
    {
        "cancellation_reason_id": 2,
        "cancellation_reason": "Passenger cancelled"
    },
    {
        "cancellation_reason_id": 3,
        "cancellation_reason": "No show"
    },
    {
        "cancellation_reason_id": 4,
        "cancellation_reason": None
    }
]


# ============================================================
# LOOKUP DICTIONARIES
# ============================================================

VEHICLE_MAKES_LIST = [
    item["vehicle_make"]
    for item in VEHICLE_MAKE_MAPPING
]

VEHICLE_MAKE_ID_MAP = {
    item["vehicle_make"]: item["vehicle_make_id"]
    for item in VEHICLE_MAKE_MAPPING
}


VEHICLE_TYPES_LIST = [
    item["vehicle_type"]
    for item in VEHICLE_TYPE_MAPPING
]

VEHICLE_TYPE_ID_MAP = {
    item["vehicle_type"]: item["vehicle_type_id"]
    for item in VEHICLE_TYPE_MAPPING
}


PAYMENT_METHODS_LIST = [
    item["payment_method"]
    for item in PAYMENT_METHOD_MAPPING
]

PAYMENT_METHOD_ID_MAP = {
    item["payment_method"]: item["payment_method_id"]
    for item in PAYMENT_METHOD_MAPPING
}


RIDE_STATUS_ID_MAP = {
    item["ride_status"]: item["ride_status_id"]
    for item in RIDE_STATUS_MAPPING
}


CITY_LIST = [
    item["city"]
    for item in CITY_MAPPING
]

CITY_ID_MAP = {
    item["city"]: item["city_id"]
    for item in CITY_MAPPING
}


CANCELLATION_REASON_ID_MAP = {
    item["cancellation_reason"]: item["cancellation_reason_id"]
    for item in CANCELLATION_REASON_MAPPING
}


# ============================================================
# ENTITY POOLS
# ============================================================

PASSENGER_POOL = []
DRIVER_POOL = []
VEHICLE_POOL = []


# ============================================================
# ENTITY CREATION
# ============================================================

def create_passenger():

    return {
        "passenger_id": str(uuid.uuid4()),
        "passenger_name": fake.name(),
        "passenger_email": fake.email(),
        "passenger_phone": fake.phone_number(),
        "updated_at": datetime.now().isoformat()
    }


def create_driver():

    return {
        "driver_id": str(uuid.uuid4()),
        "driver_name": fake.name(),
        "driver_rating": round(random.uniform(4.0, 5.0), 2),
        "driver_phone": fake.phone_number(),
        "driver_license": fake.bothify("??-???-#######"),
        "updated_at": datetime.now().isoformat()
    }


def create_vehicle():

    vehicle_make = random.choice(VEHICLE_MAKES_LIST)

    return {
        "vehicle_id": str(uuid.uuid4()),
        "vehicle_make_id": VEHICLE_MAKE_ID_MAP[vehicle_make],
        "vehicle_make": vehicle_make,
        "vehicle_model": fake.word().capitalize(),
        "vehicle_color": random.choice(
            [
                "Black",
                "White",
                "Gray",
                "Silver",
                "Blue",
                "Red"
            ]
        ),
        "license_plate": fake.bothify("???-####"),
        "updated_at": datetime.now().isoformat()
    }


# ============================================================
# INITIAL ENTITY POOLS
# ============================================================

def initialize_entity_pools():

    for _ in range(100):
        PASSENGER_POOL.append(create_passenger())

    for _ in range(50):
        DRIVER_POOL.append(create_driver())

    for _ in range(50):
        VEHICLE_POOL.append(create_vehicle())


initialize_entity_pools()


# ============================================================
# ENTITY SELECTION
# ============================================================

def get_passenger():

    # 5% chance of creating a completely new passenger
    if random.random() < 0.05:

        passenger = create_passenger()

        PASSENGER_POOL.append(passenger)

        return passenger.copy(), "INSERT"

    passenger = random.choice(PASSENGER_POOL)

    # 5% chance of changing an existing passenger
    if random.random() < 0.05:

        passenger["passenger_email"] = fake.email()
        passenger["passenger_phone"] = fake.phone_number()

        # ONLY change updated_at when the entity changes
        passenger["updated_at"] = datetime.now().isoformat()

        return passenger.copy(), "UPDATE"

    # No change:
    # keep the existing updated_at
    return passenger.copy(), "NO_CHANGE"


def get_driver():

    # 5% chance of creating a completely new driver
    if random.random() < 0.05:

        driver = create_driver()

        DRIVER_POOL.append(driver)

        return driver.copy(), "INSERT"

    driver = random.choice(DRIVER_POOL)

    # 5% chance of changing an existing driver
    if random.random() < 0.05:

        driver["driver_rating"] = round(
            random.uniform(4.0, 5.0),
            2
        )

        # ONLY change updated_at when the entity changes
        driver["updated_at"] = datetime.now().isoformat()

        return driver.copy(), "UPDATE"

    return driver.copy(), "NO_CHANGE"


def get_vehicle():

    # 5% chance of creating a completely new vehicle
    if random.random() < 0.05:

        vehicle = create_vehicle()

        VEHICLE_POOL.append(vehicle)

        return vehicle.copy(), "INSERT"

    vehicle = random.choice(VEHICLE_POOL)

    # 5% chance of changing an existing vehicle
    if random.random() < 0.05:

        vehicle["vehicle_color"] = random.choice(
            [
                "Black",
                "White",
                "Gray",
                "Silver",
                "Blue",
                "Red"
            ]
        )

        # ONLY change updated_at when the entity changes
        vehicle["updated_at"] = datetime.now().isoformat()

        return vehicle.copy(), "UPDATE"

    return vehicle.copy(), "NO_CHANGE"


# ============================================================
# RIDE GENERATOR
# ============================================================

def generate_uber_ride_confirmation():

    # --------------------------------------------------------
    # Get entities
    # --------------------------------------------------------

    passenger, passenger_operation = get_passenger()

    driver, driver_operation = get_driver()

    vehicle, vehicle_operation = get_vehicle()


    # --------------------------------------------------------
    # Ride timestamps
    # --------------------------------------------------------

    pickup_time = (
        datetime.now()
        - timedelta(
            days=random.randint(0, 30),
            hours=random.randint(0, 23)
        )
    )

    duration_minutes = random.randint(5, 120)

    dropoff_time = (
        pickup_time
        + timedelta(minutes=duration_minutes)
    )

    booking_time = (
        pickup_time
        - timedelta(minutes=random.randint(1, 10))
    )


    # --------------------------------------------------------
    # Distance
    # --------------------------------------------------------

    distance = round(
        random.uniform(0.5, 50),
        2
    )


    # --------------------------------------------------------
    # Pricing
    # --------------------------------------------------------

    base_fare = 2.50
    per_mile_rate = 1.75
    per_minute_rate = 0.35

    surge_multiplier = round(
        random.uniform(1.0, 2.5),
        2
    )

    distance_fare = round(
        distance * per_mile_rate,
        2
    )

    time_fare = round(
        duration_minutes * per_minute_rate,
        2
    )

    subtotal = round(
        (
            distance_fare
            + time_fare
            + base_fare
        ) * surge_multiplier,
        2
    )

    tip = round(
        random.choice(
            [
                0,
                0,
                0,
                1,
                2,
                3,
                5,
                random.uniform(1, 20)
            ]
        ),
        2
    )

    total_fare = round(
        subtotal + tip,
        2
    )


    # --------------------------------------------------------
    # Locations
    # --------------------------------------------------------

    pickup_address = fake.address().replace(
        "\n",
        ", "
    )

    dropoff_address = fake.address().replace(
        "\n",
        ", "
    )

    pickup_city = random.choice(CITY_LIST)
    dropoff_city = random.choice(CITY_LIST)

    pickup_city_id = CITY_ID_MAP[pickup_city]
    dropoff_city_id = CITY_ID_MAP[dropoff_city]


    # --------------------------------------------------------
    # Vehicle type
    # --------------------------------------------------------

    vehicle_type = random.choice(VEHICLE_TYPES_LIST)

    vehicle_type_id = VEHICLE_TYPE_ID_MAP[
        vehicle_type
    ]


    # --------------------------------------------------------
    # Payment method
    # --------------------------------------------------------

    payment_method = random.choice(
        PAYMENT_METHODS_LIST
    )

    payment_method_id = PAYMENT_METHOD_ID_MAP[
        payment_method
    ]


    # --------------------------------------------------------
    # Cancellation
    # --------------------------------------------------------

    is_cancelled = random.random() < 0.10

    cancellation_reason = None
    cancellation_reason_id = 4

    if is_cancelled:

        cancellation_reason = random.choice(
            [
                "Driver cancelled",
                "Passenger cancelled",
                "No show"
            ]
        )

        cancellation_reason_id = (
            CANCELLATION_REASON_ID_MAP[
                cancellation_reason
            ]
        )


    # --------------------------------------------------------
    # Ride status
    # --------------------------------------------------------

    ride_status = random.choice(
        [
            "Completed",
            "Completed",
            "Cancelled"
        ]
    )

    ride_status_id = RIDE_STATUS_ID_MAP[
        ride_status
    ]


    # --------------------------------------------------------
    # Event creation timestamp
    # --------------------------------------------------------

    event_timestamp = datetime.now().isoformat()


    # --------------------------------------------------------
    # Final event
    # --------------------------------------------------------

    ride_confirmation = {

        "ride_id": str(uuid.uuid4()),

        "confirmation_number": fake.bothify(
            "??#-####-??##"
        ),


        # ====================================================
        # PASSENGER
        # ====================================================

        "passenger": {
            **passenger,
            "operation": passenger_operation
        },


        # ====================================================
        # DRIVER
        # ====================================================

        "driver": {
            **driver,
            "operation": driver_operation
        },


        # ====================================================
        # VEHICLE
        # ====================================================

        "vehicle": {
            **vehicle,
            "operation": vehicle_operation
        },


        # ====================================================
        # REFERENCE IDS
        # ====================================================

        "vehicle_type_id": vehicle_type_id,

        "vehicle_make_id": vehicle["vehicle_make_id"],

        "payment_method_id": payment_method_id,

        "ride_status_id": ride_status_id,

        "pickup_city_id": pickup_city_id,

        "dropoff_city_id": dropoff_city_id,

        "cancellation_reason_id": cancellation_reason_id,


        # ====================================================
        # LOCATIONS
        # ====================================================

        "pickup_location_id": str(uuid.uuid4()),

        "dropoff_location_id": str(uuid.uuid4()),

        "pickup_address": pickup_address,

        "pickup_latitude": round(
            random.uniform(-90, 90),
            6
        ),

        "pickup_longitude": round(
            random.uniform(-180, 180),
            6
        ),

        "dropoff_address": dropoff_address,

        "dropoff_latitude": round(
            random.uniform(-90, 90),
            6
        ),

        "dropoff_longitude": round(
            random.uniform(-180, 180),
            6
        ),


        # ====================================================
        # RIDE DETAILS
        # ====================================================

        "distance_miles": distance,

        "duration_minutes": duration_minutes,

        "booking_timestamp": booking_time.isoformat(),

        "pickup_timestamp": pickup_time.isoformat(),

        "dropoff_timestamp": dropoff_time.isoformat(),


        # ====================================================
        # PRICING
        # ====================================================

        "base_fare": base_fare,

        "distance_fare": distance_fare,

        "time_fare": time_fare,

        "surge_multiplier": surge_multiplier,

        "subtotal": subtotal,

        "tip_amount": tip,

        "total_fare": total_fare,


        # ====================================================
        # RATING
        # ====================================================

        "rating": random.choice(
            [
                None,
                random.randint(1, 5)
            ]
        ),


        # ====================================================
        # EVENT TIMESTAMP
        # ====================================================

        "event_timestamp": event_timestamp
    }

    return ride_confirmation