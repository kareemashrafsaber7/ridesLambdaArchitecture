create table ridesstream.gold.dim_payment_method(
    payment_method_id int,
    payment_method string,
    is_card boolean,
    requires_auth boolean
);

insert into ridesstream.gold.dim_payment_method
values
(1, 'Credit Card', True, True),
(2, 'Debit Card', True, True),
(3, 'Digital Wallet', False, False),
(4, 'Cash', False, False);

create table ridesstream.gold.dim_ride_status(
    ride_status_id int,
    ride_status string,
    is_completed boolean
);

insert into ridesstream.gold.dim_ride_status
values
(1, 'Completed', True),
(2, 'Cancelled', False);

create table ridesstream.gold.dim_vehicle_make(
    vehicle_make_id int,
    vehicle_make string
);

insert into ridesstream.gold.dim_vehicle_make
values
(1, 'Toyota'),
(2, 'Honda'),
(3, 'Ford'),
(4, 'Chevrolet'),
(5, 'Nissan'),
(6, 'BMW'),
(7, 'Mercedes');

create table ridesstream.gold.dim_city(
    city_id int,
    city string,
    state string,
    region string
);

insert into ridesstream.gold.dim_city
values
(1, 'New York', 'NY', 'Northeast'),
(2, 'Los Angeles', 'CA', 'West'),
(3, 'Chicago', 'IL', 'Midwest'),
(4, 'Houston', 'TX', 'South'),
(5, 'Phoenix', 'AZ', 'Southwest'),
(6, 'Philadelphia', 'PA', 'Northeast'),
(7, 'San Antonio', 'TX', 'South'),
(8, 'San Diego', 'CA', 'West'),
(9, 'Dallas', 'TX', 'South'),
(10, 'San Jose', 'CA', 'West');

create table ridesstream.gold.dim_cancellation_reason(
    cancellation_reason_id int,
    cancellation_reason string
);

insert into ridesstream.gold.dim_cancellation_reason
values
(1, 'Driver cancelled'),
(2, 'Passenger cancelled'),
(3, 'No show'),
(4, null);

create table ridesstream.gold.dim_vehicle_type(
    vehicle_type_id int,
    vehicle_type string,
    description string,
    base_rate double,
    per_mile double,
    per_minute double 
);

insert into ridesstream.gold.dim_vehicle_type
values
(1, 'UberX', 'Standard', 2.50, 1.75, 0.35),
(2, 'UberXL', 'Extra Large', 3.50, 2.25, 0.45),
(3, 'UberPOOL', 'Shared Ride', 2.00, 1.50, 0.30),
(4, 'Uber Comfort' ,'Comfortable', 3.00, 2.00, 0.40),
(5, 'Uber Black', 'Premium', 5.00, 3.50, 0.60);