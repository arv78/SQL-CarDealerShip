alter table guarantee add constraint guarantee_company foreign key (company) references company(name);

insert into guarantee values 
('Audi', 'A3',2018,18),
('Audi', 'R3',2019,20),
('BMW', 'Z4',2018,24),
('BMW', 'X5',2019,12),
('BMW', 'X1',2019,30),
('Benz', 'A class',2017,48),
('Benz', 'C class',2018,24),
('Benz', 'CLA',2019,21),
('Audi', 'S3',2018,36),
('Porche', '911',2019,21),
('Porche', '911',2018,15),
('Porche', '911',2017,12),
('Infinity', 'Q50',2019,25),
('Infinity', 'Q60',2019,30),
('Infinity', 'Q70',2019,35);