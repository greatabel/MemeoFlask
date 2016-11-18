use sharingan;
SET FOREIGN_KEY_CHECKS = 0; 
truncate table  patient_users;
truncate table  patients;
truncate table  users;
SET FOREIGN_KEY_CHECKS = 1;

insert into users(`name`,`birthday`,`created_date`) VALUES('putao_abel',now(),now());
insert patients(name,sex,birthday,created_date) values('小明',0,now(),(now() - INTERVAL 2 YEAR)  );
insert patients(name,sex,birthday,created_date) values('小红',1,now(),(now() - INTERVAL 2 YEAR)  );
insert patient_users(patient_id, user_id) values(1,1);
insert patient_users(patient_id, user_id) values(2,1);