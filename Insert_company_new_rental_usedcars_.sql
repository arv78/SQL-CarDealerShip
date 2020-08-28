insert into company values
('BMW','2018-02-01','2020-02-01');
insert into company values
('Audi','2015-12-01','2020-12-01'),
('Benz','2008-12-01','2022-12-01'),
('Porche','2018-01-01','2024-01-01'),
('Infinity','2012-12-01','2020-12-01');


insert into new_cars values
(0001,'X1','BMW',2019,'Black',50000),
(0002,'Z4','BMW',2018,'Yellow',75000),
(0003,'X5','BMW',2019,'White',65000),
(0004,'A class','Benz',2017,'Blue',25000),
(0005,'C class','Benz',2018,'Black',60000),
(0006,'CLA','Benz',2019,'White',85000),
(0007,'A3','Audi',2018,'Black',60000),
(0008,'R3','Audi',2019,'Green',100000),
(0009,'S3','Audi',2018,'Black',40000),
(0010,'A3','Audi',2019,'Black',60000),
(0011,'911','Porche',2019,'Yellow',60000),
(0012,'911','Porche',2018,'Yellow',50000),
(0013,'911','Porche',2017,'Yellow',40000),
(0014,'Q50','Infinity',2019,'Brown',35000),
(0015,'Q60','Infinity',2019,'White',45000),
(0016,'Q70','Infinity',2019,'Black',55000);

Alter table used_cars add constraint Ssn_to_seller_id foreign key (seller_id) references customer(Ssn);

insert into used_cars values
(0001,'A63','Benz',2014,'Red',12000,2212,1600),
(0002,'Serato','Kia',2015,'Black',5000,2861,2000),
(0003,'Camery','Toyota',2016,'White',18000,3059,1000),
(0004,'Z1','BMW',2014,'Black',8000,2212,1900),
(0005,'S class','Benz',2014,'Blue',35000,8130,1600),
(0006,'A Class','Benz',2014,'Red',12000,2165,1600);

insert into rental_cars values
(0001,'Camery','Toyota',2012,'White',12000,20),
(0002,'Camery','Toyota',2012,'White',12000,20),
(0003,'Yaris','Toyota',2010,'Blue',10000,15),
(0004,'Sportage','Kia',2014,'Black',20000,40),
(0005,'GTR','nissan',2012,'Red',40000,60);
