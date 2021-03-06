/* insert 10 people
 *
 */
INSERT INTO people VALUES
(736391576000000,'Steven',170.00,180.00,'red','blue','78 tuscany hills rd NW calgary ab','m',TO_DATE('1960-07-06','YYYY-MM-DD'));
INSERT INTO people VALUES
(585115484000000,'Alcuin',160.00,180.00,'red','blue','10615 47 Ave NW Edmonton, AB','m',TO_DATE('1960-12-06','YYYY-MM-DD'));
INSERT INTO people VALUES
(140505185000000,'Muqtada',200.00,180.00,'red','blue','8379 103 St NW Edmonton, AB T6E','f',TO_DATE('1960-01-06','YYYY-MM-DD'));
INSERT INTO people VALUES
(334415374000000,'Muhammad',099.99,180.00,'red','blue','10824 97 St NW Edmonton, AB T5H 2M3','f',TO_DATE('1960-02-06','YYYY-MM-DD'));
INSERT INTO people VALUES
(897817901000000,'Agnes',100.99,180.00,'red','blue','4336 Macleod Trail Calgary, AB T2G 0A4','m',TO_DATE('1960-03-06','YYYY-MM-DD'));
INSERT INTO people VALUES
(798634968000000,'Theodor',150.99,180.00,'red','blue','2000 Airport Rd NE, Calgary, AB T2E 6Z8','m',TO_DATE('1960-04-06','YYYY-MM-DD'));
INSERT INTO people VALUES
(498934133000000,'Akinola',100.99,180.00,'red','blue','2500 University Dr NW, Calgary, AB T2N 1N4','f',TO_DATE('1960-05-06','YYYY-MM-DD'));
INSERT INTO people VALUES
(400993097000000,'Peter',150.99,180.00,'red','blue','150 Ambrose Cir SW, Calgary, AB T3H 0L5','m',TO_DATE('1960-06-06','YYYY-MM-DD'));
INSERT INTO people VALUES
(234131347000000,'Jasper',101.10,180.00,'red','blue','116 St 85 Ave, Edmonton, AB T6G 2R3','f',TO_DATE('1960-09-06','YYYY-MM-DD'));
INSERT INTO people VALUES
(394391576000000,'Jessica',170.00,180.00,'red','blue','9105 116 St NW, Edmonton, AB T6G 2W2','f',TO_DATE('1960-10-06','YYYY-MM-DD'));


INSERT INTO drive_licence VALUES
(000736391576000,736391576000000,'classA', null,TO_DATE('1960-07-06','YYYY-MM-DD'),TO_DATE('1960-07-06','YYYY-MM-DD'));
INSERT INTO drive_licence VALUES
(000585115484000,585115484000000,'classA', null,TO_DATE('1960-07-06','YYYY-MM-DD'),TO_DATE('1960-07-06','YYYY-MM-DD'));
INSERT INTO drive_licence VALUES
(000140505185000,140505185000000,'nondriving', null,TO_DATE('1960-07-06','YYYY-MM-DD'),TO_DATE('1960-07-06','YYYY-MM-DD'));
INSERT INTO drive_licence VALUES
(000334415374000,334415374000000,'nondriving', null,TO_DATE('1960-07-06','YYYY-MM-DD'),TO_DATE('1960-07-06','YYYY-MM-DD'));
INSERT INTO drive_licence VALUES
(000897817901000,897817901000000,'classA', null,TO_DATE('1960-07-06','YYYY-MM-DD'),TO_DATE('1960-07-06','YYYY-MM-DD'));

/*
 *
 *INSERT INTO driving_condition VALUES()
 *INSERT INTO restriction VALUES()
 */

INSERT INTO vehicle_type VALUES(1,'sedan');
INSERT INTO vehicle_type VALUES(2,'SUV');
INSERT INTO vehicle_type VALUES(3,'van');
INSERT INTO vehicle_type VALUES(4,'semi-truck');
INSERT INTO vehicle_type VALUES(5,'bus');
INSERT INTO vehicle_type VALUES(6,'truck');
INSERT INTO vehicle_type VALUES(7,'bi');
INSERT INTO vehicle_type VALUES(8,'last');




INSERT INTO vehicle VALUES(100000736391576,'ford','calg',1994,'red',2);
INSERT INTO vehicle VALUES(100000736391577,'ford','calg',1994,'red',2);
INSERT INTO vehicle VALUES(100000736391578,'ford','calg',1994,'red',2);
INSERT INTO vehicle VALUES(100000736391579,'ford','calg',1994,'red',2);

INSERT INTO vehicle VALUES(100000585115484,'ford','edmon',1994,'red',1);
INSERT INTO vehicle VALUES(100000585115485,'ford','edmon',1994,'blue',1);

INSERT INTO owner VALUES(736391576000000,100000736391576,'y');
INSERT INTO owner VALUES(736391576000000,100000736391577,'y');
INSERT INTO owner VALUES(736391576000000,100000736391578,'y');
INSERT INTO owner VALUES(736391576000000,100000736391579,'y');

INSERT INTO owner VALUES(585115484000000,100000585115484,'y');
INSERT INTO owner VALUES(585115484000000,100000585115485,'n');


/*
 *INSERT INTO auto_sale VALUES();
 *INSERT INTO ticket_type VALUES()
 *INSERT INTO ticket VALUES()
 */