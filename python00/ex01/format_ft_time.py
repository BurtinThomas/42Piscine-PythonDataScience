from time import time
from datetime import datetime

linux_time = time()
formated_linux_time = "{:,.4f}".format(linux_time)
formated_scientifique_linux_time = "{:.2e}".format(linux_time)

date_now = datetime.now()
date_now_object = datetime.strptime(str(date_now), "%Y-%m-%d %H:%M:%S.%f")
formated_date_now = date_now_object.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {formated_linux_time} or {formated_scientifique_linux_time} in scientific notation")
print(formated_date_now)