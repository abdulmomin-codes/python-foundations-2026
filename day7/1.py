#Write a script that creates a sample access.log text file with various log levels 
#(e.g., INFO, ERROR, WARNING).
# Then, open it using with open(...), iterate line-by-line using a 
#memory-efficient for line in f: loop (avoiding .readlines()), 
#filter for lines containing "ERROR", and write them into errors.log.

sample_logs = """2026-11-11 10:01:12 INFO User login successful for user_id=402
2026-11-11 10:03:45 WARNING Disk usage reached 82'%' on /dev/sda1
2026-11-11 10:05:19 ERROR Database connection timed out after 30s
2026-11-11 10:08:02 INFO Scheduled backup completed
2026-11-11 10:12:33 ERROR Failed to process payment for order_id=8891
2026-11-11 10:15:10 WARNING High memory consumption detected
2026-11-11 10:18:44 INFO API request GET /api/v1/status 200 OK
2026-11-11 10:21:05 ERROR Unhandled exception in worker thread 4
"""

with open('access.log', 'w') as wf:
    wf.write(sample_logs)
with open('access.log', 'r') as rf:
    with open('errors.log', 'w') as ef:
        for line in rf:
           if 'ERROR' in line:
               ef.write(line) 
     