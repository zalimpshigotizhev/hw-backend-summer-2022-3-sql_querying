# INFO
# Вывести топ 5 самых коротких по длительности перелетов.
# Duration - разница между scheduled_arrival и scheduled_departure.
# В ответе должно быть 2 колонки [flight_no, duration]
TASK_1_QUERY = """
select flight_no,
       (flights.scheduled_arrival - flights.scheduled_departure) as duration
from flights
order by duration
limit 5;
"""
#  flight_no | duration
# -----------+----------
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00
#  PG0233    | 00:25:00
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00


# INFO
# Вывести топ 3 рейса по числу упоминаний в таблице flights
# количество упоминаний которых меньше 50
# В ответе должно быть 2 колонки [flight_no, count]
TASK_2_QUERY = """
select flight_no, count(1)
from flights
group by flight_no
having count(1) < 50
order by count(1) desc
limit 3;
"""
#  flight_no | count
# -----------+-------
#  PG0260    |    27
#  PG0371    |    27
#  PG0310    |    27

# INFO
# Вывести число перелетов внутри одной таймзоны
# Нужно вывести 1 значение в колонке count
TASK_3_QUERY = """
select count(case when ad_dep.timezone = ad_arr.timezone then 1 end)
from flights f
         left join airports_data ad_dep
                   on ad_dep.airport_code = f.departure_airport
         left join airports_data ad_arr
                   on ad_arr.airport_code = f.arrival_airport;
"""
#  count
# --------
#  16824
