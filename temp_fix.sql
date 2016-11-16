use sharingan_ali;
-- DROP TABLE `sharingan_ali`.`MeasureBaseline`;
-- CREATE TABLE IF NOT EXISTS MeasureBaseline   (
--      baselineid int NOT NULL AUTO_INCREMENT,
--      patientid int,
--      data VARCHAR(100),
--      whicheye  boolean not null default 0,
--      createdate TIMESTAMP,
--      PRIMARY KEY (baselineid)
--      )
delete from MeasureBaseline;
insert MeasureBaseline(patientid, data,whicheye,createdate) values(1,-50,1,now());
insert MeasureBaseline(patientid, data,whicheye,createdate) values(1,-51,1,now());
insert MeasureBaseline(patientid, data,whicheye,createdate) values(1,-52,1,now());
insert MeasureBaseline(patientid, data,whicheye,createdate) values(1,-53,1,now());
insert MeasureBaseline(patientid, data,whicheye,createdate) values(1,-54,1,now());

insert MeasureBaseline(patientid, data, whicheye, createdate) values(1,-105,0,now());
insert MeasureBaseline(patientid, data, whicheye, createdate) values(1,-106,0,now());
insert MeasureBaseline(patientid, data, whicheye, createdate) values(1,-107,0,now());
insert MeasureBaseline(patientid, data, whicheye, createdate) values(1,-108,0,now());
insert MeasureBaseline(patientid, data, whicheye, createdate) values(1,-109,0,now());
delete from MeasureRaw;
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-50',1, false, now());
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-150',1, false, now() - interval 1 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-60',1, false, now() - interval 2 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-70',1, false, now() - interval 3 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-80',1, false, now() - interval 4 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-90',1, false, now() - interval 5 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-100',1, false, now() - interval 6 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-110',1, false, now() - interval 7 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-120',1, false, now() - interval 8 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-70',1, false, now() - interval 9 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-60',1, false, now() - interval 10 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-50',1, false, now() - interval 11 day);

insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-20',1, true, now() - interval 1 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-30',1, true, now() - interval 2 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-40',1, true, now() - interval 3 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-90',1, true, now() - interval 4 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('3',1, true, now() - interval 5 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-10',1, true, now() - interval 6 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-30',1, true, now() - interval 7 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-40',1, true, now() - interval 8 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-50',1, true, now() - interval 9 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-60',1, true, now() - interval 10 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-70',1, true, now() - interval 11 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('-50',1, true, now() - interval 12 day);

