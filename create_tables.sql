create table new_cars
(
vehicle_id int primary key,
model varchar(10) not null,
company varchar(10) not null,
[year] int,
color varchar(10) not null,
price int not null,
);

create table used_cars
(
vehicle_id int primary key,
model varchar(10) not null,
company varchar(10) not null,
[year] int,
color varchar(10) not null,
price int not null,
seller_id int not null,
kilometer int not null
);

create table rental_cars
(
vehicle_id int primary key,
model varchar(10) not null,
company varchar(10) not null,
[year] int,
color varchar(10) not null,
price int not null,
daily_rate int not null
);

create table company
(
name varchar(10) primary key,
start_date date not null,
end_date date
);

alter table new_cars add constraint fk_new foreign key(company) references company(name);

create table customer
(
Ssn int primary key,
fname varchar(10) not null,
lname varchar(10) not null,
phone int
);

create table salesperson
(
Ssn int primary key,
fname varchar(10) not null,
lname varchar(10) not null,
phone int,
salary int
);

create table new_cars_deals
(
vehicle_id int primary key,
customer_id int not null,
salesperson_id int not null,
sale_price int not null,
deal_date date not null,

foreign key (vehicle_id) references new_cars(vehicle_id),
foreign key (customer_id) references customer(Ssn),
foreign key (salesperson_id) references salesperson(Ssn)
);

create table used_cars_deals
(
vehicle_id int primary key,
customer_id int not null,
salesperson_id int not null,
owner_id int not null,
sale_price int not null,
deal_date date not null,

foreign key (vehicle_id) references used_cars(vehicle_id),
foreign key (customer_id) references customer(Ssn),
foreign key (owner_id) references customer(Ssn),
foreign key (salesperson_id) references salesperson(Ssn)
);

create table rents
(
vehicle_id int primary key,
customer_id int not null,
start_date date not null,
end_date date not null,

foreign key (vehicle_id) references rental_cars(vehicle_id),
foreign key (customer_id) references customer(Ssn)
);

create table guarantee 
(
company varchar(10),
model varchar(10),
[year] int,
guarantee_duration int not null,
primary key (company,model,[year])
);