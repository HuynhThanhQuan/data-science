-- 2. Join tables
-- Inner JOin
select * from demographic t1
join member t2
on t1.customer_id = t2.customer_id

-- Full outer join 
select * from demographic t1
full outer join member t2
on t1.customer_id = t2.customer_id

-- right join 
select * from demographic t1
right join member t2
on t1.customer_id = t2.customer_id

-- left join 
select * from demographic t1
left join member t2
on t1.customer_id = t2.customer_id

-- join demographic, member va txn table