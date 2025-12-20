from apscheduler.schedulers.blocking import BlockingScheduler
from main import run_agent
print(" Stock AI Agent started...")

run_agent()

scheduler = BlockingScheduler()
scheduler.add_job(run_agent, "interval", hours=1)
scheduler.start()
