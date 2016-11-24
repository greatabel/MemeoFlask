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

update patients set picture = 
    x'89504E470D0A1A0A0000000D494844520000001000000010080200000090916836000000017352474200AECE1CE90000000467414D410000B18F0BFC6105000000097048597300000EC300000EC301C76FA8640000001E49444154384F6350DAE843126220493550F1A80662426C349406472801006AC91F1040F796BD0000000049454E44AE426082'