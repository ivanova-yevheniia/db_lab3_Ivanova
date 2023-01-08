--select * from USA_State;
create table statecopy as select * from USA_State; 
--delete from statecopy;
--select * from statecopy;


DO $$
 DECLARE
     zipcode   statecopy.zipcode%TYPE;
     usa_state statecopy.usa_state%TYPE;

 BEGIN
     zipcode := 48001;
     usa_state := 'Michigan';
	 
     FOR counter IN 1..8
         LOOP
            INSERT INTO statecopy (zipcode, usa_state)
             VALUES (zipcode + counter, usa_state);
         END LOOP;
 END;
 $$