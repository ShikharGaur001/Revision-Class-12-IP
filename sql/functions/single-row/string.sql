--* CHAR() ... ek taraf se alu dalo doosri taraf se sona nikalo

SELECT CHAR(70, 65, 67, 69);
SELECT CHAR(65, 67.3, 69.3);
SELECT CHAR(83,72,73,75,72,65,82);

--* CONCAT() ... do alag alag strings ko jod rha h

USE p4;
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)

);

INSERT INTO students (name) VALUES
('John'),
('Jane'),
('Alex'),
('Ravi'),
('Sara');

SELECT 
    id,
    CONCAT('Student: ', name) AS formatted_name
FROM students;

--* LOWER/LCASE ... lowercase kardeta h uppercase ko

SELECT LOWER('MR. BiLlA');
SELECT LCASE('MR. BiLlA') AS lowercase;

--? Display names 'MR. OBAMA' and 'MS. GANDHI' into lowercase.

SELECT LOWER('MR. OBAMA') AS "LowerName1", LOWER('MS. GANDHI') AS "LowerName2";

--? agar pooche output kya hoga toh??

-- +-------------+-------------+
-- | LowerName1  | LowerName2  |
-- +-------------+-------------+
-- | mr. obama   | ms. gandhi  |
-- +-------------+-------------+

--* SUBSTR() ... chowmein se manchurian nikalo
--* SUBSTR(str, m, n)  m --> index without 0... n -->  kitne character churane... n can't be less than 1 if so... null is returned
SELECT SUBSTR('ABCDEFG', 3, 4) "Subs";
SELECT SUBSTR('ABCDEFG', -5, 4) "Subs";

--* UPPER/UCASE 

--* LTRIM & RTRIM

SELECT LTRIM('          HELLO CHURAN           ');
SELECT RTRIM('          HELLO CHURAN           ');

--* TRIM ... leading ---> left se and trailing ---> right se
--* TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM] str), TRIM([remstr FROM]str)
SELECT TRIM(trailing '' FROM '          HELLO CHURAN           ');
SELECT TRIM(both 'x' FROM 'xxxxxxxxxxxxxxPHYTONxxxxxxxxxxxx');

--* INSTR() ... ye batata h ki di hui string pehli wali strin me sabse pehle kitne no pr h ... ek baar hi dhundhta

SELECT INSTR('lolopolo', 'lo'); -- returns one
SELECT INSTR('lolopolo', 'po');--returns five
SELECT INSTR('lolopolo', 's'); -- if not found then gives 0

--* LENGTH()

--* LEFT() AND RIGHT()

SELECT LEFT('Govind Pandey', 4);

--* MID(str, start, no of characters)

SELECT MID('Hakla Yash', 4, 5); -- gap ko count karega... saath me