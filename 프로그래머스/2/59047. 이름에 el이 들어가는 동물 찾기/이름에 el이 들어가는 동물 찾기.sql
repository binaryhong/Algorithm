-- 코드를 입력하세요
SELECT animal_id, name
from animal_ins
where ANIMAL_TYPE = 'DOG'
and (name like '%EL%' 
or name like '%El%'
or name like '%el%'
or name like '%eL%')
order by name asc