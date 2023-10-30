-- 1. Basic statement
select * from demographic

select * from demographic where gender = 'Nữ'

-- null 
select * from demographic where gender is null

select * from demographic where gender = 'Nữ'
order by date_of_birth

select * from demographic where gender = 'Nữ'
order by date_of_birth limit 20