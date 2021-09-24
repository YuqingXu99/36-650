INSERT INTO RDATA (a, b, x) VALUES
('hw06a', 'hw06b', 95.5),
('hw06c', 'hw06d', 45.5);

UPDATE RDATA
SET moment = '2020-03-28'
WHERE X = 45.5 OR x = 55.5;
	
	
SELECT * FROM RDATA;