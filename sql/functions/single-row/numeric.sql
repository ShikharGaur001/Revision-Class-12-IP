--* MOD(m,n) ... M%N remainder h

SELECT MOD(11, 4);
SELECT MOD(12, 4);

--* POWER/POW

SELECT POW(3,2) "Raised";

--* ROUND

SELECT ROUND(15.193, 1);
SELECT ROUND(15.193, -1);
SELECT ROUND(12.193, -1);
SELECT ROUND(12032.193, -2);

--* SIGN() signum function -ve toh -1, zero toh 0, +ve toh 1

--* SQRT()

--* TRUNCATE() ... ROUND me approx karke trim karte lekin isme bina approx ke hi trim kardete

SELECT TRUNCATE(15.193, 1);