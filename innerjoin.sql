create database mysql_1;

use mysql_1;

show databases

create table giver_table
(
	giver_id varchar(6),
	first_name varchar(50),
	last_name varchar(50),
	city varchar(10),
	mobile_number varchar(10),
	constraint giver_table_giver_id_pk primary key(giver_id)
	);

describe giver_table;

create table giver_acc_table
(
	giver_acc_no varchar(15),
    giver_id varchar(6),
    opening_bal varchar(7),
    giver_acc_type varchar(10),
    giver_acc_status varchar(10),
    constraint giver_acc_table_giver_acc_no_pk primary key(giver_acc_no),
    constraint giver_acc_table_giver_id_fk foreign key (giver_id) references giver_table(giver_id)
    );

insert into giver_table(giver_id,first_name,last_name,city,mobile_number) 
values('a004c1','Lokesh','Madam','Anantapur','8073519246');
insert into giver_table(giver_id,first_name,last_name,city,mobile_number) 
values('b23d4r','Chalapathi','Surname','Bangalore','8792803145');
insert into giver_table(giver_id,first_name,last_name,city,mobile_number) 
values('c345fe','Sailaja','Name','Chennai','7337804689');
insert into giver_table(giver_id,first_name,last_name,city,mobile_number) 
values('der345','Jayachandra','Nese','Bangalore','7895648227');
insert into giver_table(giver_id,first_name,last_name,city,mobile_number) 
values('345rtg','Ranjith','Reddy','Anantapur','7845962135');
insert into giver_table(giver_id,first_name,last_name,city,mobile_number) 
values('de345q','Punith','Jamba','Peenya','9945845484');

select * from giver_acc_table;

insert into giver_acc_table(giver_acc_no,giver_id,opening_bal,giver_acc_type,giver_acc_status) 
values('3636652478','a004c1','10000','Savings','Active');
insert into giver_acc_table(giver_acc_no,giver_id,opening_bal,giver_acc_type,giver_acc_status) 
values('3835642488','b23d4r','1000000','Savings','Active');
insert into giver_acc_table(giver_acc_no,giver_id,opening_bal,giver_acc_type,giver_acc_status) 
values('3838956728','c345fe','100000','Savings','Active');
insert into giver_acc_table(giver_acc_no,giver_id,opening_bal,giver_acc_type,giver_acc_status) 
values('3835656775','der345','1000','Savings','Active');
insert into giver_acc_table(giver_acc_no,giver_id,opening_bal,giver_acc_type,giver_acc_status) 
values('3835657890','345rtg','100000','Savings','Active');
insert into giver_acc_table(giver_acc_no,giver_id,opening_bal,giver_acc_type,giver_acc_status) 
values('3835652478','de345q','10','Savings','Inactive');

select first_name,giver_acc_no from giver_table inner join giver_acc_table on giver_table.giver_id = giver_acc_table.giver_id;

select first_name,giver_acc_no,opening_bal from giver_table inner join giver_acc_table on giver_table.giver_id = giver_acc_table.giver_id;

show databases;
