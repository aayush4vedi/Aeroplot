from crontab import CronTab

my_cron = CronTab(user='aayushchaturvedi')

for job in my_cron:
    print(job)