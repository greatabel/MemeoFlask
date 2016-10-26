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
insert MeasureBaseline(patientid, data,whicheye,createdate) values(1,150,0,now());
insert MeasureBaseline(patientid, data,whicheye,createdate) values(1,151,0,now());
insert MeasureBaseline(patientid, data, whicheye, createdate) values(1,152,1,now());
     