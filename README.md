 CREATE DATABASE testdb2;
 
  USE testdb2;
 
 CREATE TABLE testtable(hostgroup INT, schemaname VARCHAR(240) NOT NULL, username VARCHAR(240) NOT NULL, client_address VARCHAR(240), digest VARCHAR(255) NOT NULL, digest_text TEXT, count_star INT, first_seen INT, last_seen INT,sum_time INT, min_time INT, max_time INT);

 
 INSERT INTO testtable(hostgroup,schemaname,username,digest,digest_text,count_star,first_seen,last_seen,sum_time,min_time,max_time,client_address) VALUES (1,'myapps02','slv_sbx_asp1','0x8256945D6376D8D8','select tenant_id, type as message, status, count() as count from zb_job_state, where status in sent on group tenant',1,1663943165,1663943165,3260202,3260202,3260202,'');
  
  DROP TABLE testdb2.testtable;