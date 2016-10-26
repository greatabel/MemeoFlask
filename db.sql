use sharingan_ali;

CREATE TABLE IF NOT EXISTS User (
     userid int NOT NULL AUTO_INCREMENT,
     name VARCHAR(100),
     sex boolean not null default 0,
     birthday datetime,
     mobilephone  VARCHAR(20),
     email VARCHAR(20),
     picture BLOB,
     roleid int,

     putao_token_uid VARCHAR(100),
     putao_name VARCHAR(100),

     putao_birthday datetime,

     authtype int,
     createdate TIMESTAMP,
     PRIMARY KEY (userid)
     );

CREATE TABLE IF NOT EXISTS Measure (
     measureid int NOT NULL AUTO_INCREMENT,
     rawdataid int,
     data VARCHAR(100),
     deviceid VARCHAR(100),
     createdate TIMESTAMP,
     PRIMARY KEY (measureid)
     );

CREATE TABLE IF NOT EXISTS MeasureRaw  (
     rawdataid int NOT NULL AUTO_INCREMENT,
     rawdata VARCHAR(100),
     patientid int,
     whicheye  boolean not null default 0,
     isbaseline  boolean not null default 0,
     createdate TIMESTAMP,
     PRIMARY KEY (rawdataid)
     );

CREATE TABLE IF NOT EXISTS Patient  (
     patientid int NOT NULL AUTO_INCREMENT,
     name VARCHAR(100),
     sex  boolean not null default 0,
     birthday datetime,
     picture  BLOB, 
     createdate TIMESTAMP,
     PRIMARY KEY (patientid)
     );

CREATE TABLE IF NOT EXISTS Patient_User   (
     patientid int ,
     userid int,
      createdate TIMESTAMP,
     PRIMARY KEY (patientid, userid)
     );

CREATE TABLE IF NOT EXISTS MeasureBaseline   (
     baselineid int NOT NULL AUTO_INCREMENT,
     patientid int,
     data VARCHAR(100),
     createdate TIMESTAMP,
     PRIMARY KEY (baselineid)
     ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/* 
#insert test data:
INSERT INTO User(`roleid`,`putao_token_uid`,`putao_name`,`putao_birthday`,`authtype`,`createdate`) 
VALUES(1,'0870111b0ea9f317465b209071305916e3080cce','putao_abel',now(),1,now());

insert Measure(rawdataid, data, deviceid,createdate) values(0,'250,151,152,153','88DAC8E9-08E5-81E5-D7AB-182B79D30698', now());
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('250,151,152,153',0, false, now());
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('251,151,152,153',0, true, now());
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('252,151,152,153',1, false, now());
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('253,151,152,153',1, true, now());
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('254,151,152,153',2, false, now());
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('255,151,152,153',2, true, now());
insert Patient_User(patientid, userid, createdate) values(1,0,now());
insert Patient_User(patientid, userid, createdate) values(2,0,now());
insert Patient_User(patientid, userid, createdate) values(3,0,now());
insert Patient(name,sex,birthday, picture,createdate) values('小明',0,now(),LOAD_FILE('/Users/wanchang/Downloads/AbelProject/MeomoFlask/Abc.jpg'), (now() - INTERVAL 2 YEAR)  );
insert Patient(name,sex,birthday, picture,createdate) values('小红',1,now(),LOAD_FILE('/Users/wanchang/Downloads/AbelProject/MeomoFlask/Abc.jpg'), (now() - INTERVAL 3 YEAR)  );
insert MeasureBaseline(patientid, data, createdate) values(1,150,now());
insert MeasureBaseline(patientid, data, createdate) values(1,151,now());

*/


