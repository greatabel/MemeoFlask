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
insert MeasureBaseline(patientid, data,whicheye,createdate) values(1,300,0,now());
insert MeasureBaseline(patientid, data,whicheye,createdate) values(1,301,0,now());
insert MeasureBaseline(patientid, data,whicheye,createdate) values(1,302,0,now());
insert MeasureBaseline(patientid, data,whicheye,createdate) values(1,303,0,now());
insert MeasureBaseline(patientid, data,whicheye,createdate) values(1,304,0,now());
insert MeasureBaseline(patientid, data, whicheye, createdate) values(1,255,1,now());
insert MeasureBaseline(patientid, data, whicheye, createdate) values(1,256,1,now());
insert MeasureBaseline(patientid, data, whicheye, createdate) values(1,257,1,now());
insert MeasureBaseline(patientid, data, whicheye, createdate) values(1,258,1,now());
insert MeasureBaseline(patientid, data, whicheye, createdate) values(1,279,1,now());
delete from MeasureRaw;
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('250',1, false, now());
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('260',1, false, now() - interval 1 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('270',1, false, now() - interval 2 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('265',1, false, now() - interval 3 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('275',1, false, now() - interval 4 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('275',1, false, now() - interval 5 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('251',1, false, now() - interval 6 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('262',1, false, now() - interval 7 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('273',1, false, now() - interval 8 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('265',1, false, now() - interval 9 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('276',1, false, now() - interval 10 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('277',1, false, now() - interval 11 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('310',1, true, now() - interval 1 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('305',1, true, now() - interval 2 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('285',1, true, now() - interval 3 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('315',1, true, now() - interval 4 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('325',1, true, now() - interval 5 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('305',1, true, now() - interval 6 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('311',1, true, now() - interval 7 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('302',1, true, now() - interval 8 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('283',1, true, now() - interval 9 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('314',1, true, now() - interval 10 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('325',1, true, now() - interval 11 day);
insert MeasureRaw(rawdata, patientid, whicheye,createdate) values('306',1, true, now() - interval 12 day);

