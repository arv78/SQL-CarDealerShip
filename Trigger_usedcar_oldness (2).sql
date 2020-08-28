create trigger check_oldness
on used_cars
after insert
as

if exists (select i.vehicle_id
			from inserted i
			where year(GETDATE())-i.year > 20)
begin
	raiserror ('Car is too old for selling!!',16,1);
	rollback transaction;
end;