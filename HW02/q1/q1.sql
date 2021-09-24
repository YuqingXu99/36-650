CREATE TABLE RDATA(
	id SERIAL PRIMARY KEY,
	a TEXT CHECK (char_length(b)<=5),
	b TEXT CHECK (char_length(b)<=5),
	moment DATE,
	x NUMERIC(5,2)
);

SELECT * FROM RDATA;
