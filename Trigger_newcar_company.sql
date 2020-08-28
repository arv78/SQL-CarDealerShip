create trigger check_company
on new_cars
after insert
as
IF  NOT EXISTS (select i.company
           from inserted i
           INNER JOIN company c 
              on i.company = c.[name]    
			)
begin
	raiserror ('This company is not supported!!',16,1);
	rollback transaction;
end;