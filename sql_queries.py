# Вывести топ 5 самых коротких по длительности перелетов.
# Duration - разница между scheduled_arrival и scheduled_departure.
# В ответе должно быть 2 колонки [flight_no, duration]
TASK_1_QUERY = """
select flight_no, scheduled_arrival - scheduled_departure as duration
from flights order by duration limit 5;
"""


# Вывести топ 3 рейса по числу упоминаний в таблице flights
# количество упоминаний которых меньше 50
# В ответе должно быть 2 колонки [flight_no, count]
TASK_2_QUERY = """
select flight_no, count(*) from flights group by flight_no having count(*) < 50 order by count(*) desc limit 3;
"""
#  flight_no | count
# -----------+-------
#  PG0260    |    27
#  PG0371    |    27
#  PG0310    |    27

# Вывести число перелетов внутри одной таймзоны
# Нужно вывести 1 значение в колонке count
TASK_3_QUERY = """
select COUNT(*) from flights f join airports_data dep on f.departure_airport = dep.airport_code join airports_data arr on f.arrival_airport = arr.airport_code where dep.timezone = arr.timezone
"""
#  count
# --------
#  16824
