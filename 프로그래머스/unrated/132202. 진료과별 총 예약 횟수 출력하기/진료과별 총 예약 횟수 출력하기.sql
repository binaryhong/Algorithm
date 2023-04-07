SELECT MCDP_CD as "진료과코드", count(APNT_YMD) as "5월예약건수" 
from APPOINTMENT 
where MONTH(APNT_YMD) = 05
group by MCDP_CD
order by count(APNT_NO) ASC, MCDP_CD ASC