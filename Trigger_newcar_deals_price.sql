create trigger check_price
on new_cars_deals
after insert
as
if  EXISTS (select i.sale_price
           from inserted i
           INNER JOIN new_cars nc 
              on i.vehicle_id = nc.vehicle_id
			  where i.sale_price < nc.price
			)
begin
	raiserror ('The sale_price should be higher than the price of the car!!',16,1);
	rollback transaction;
end;