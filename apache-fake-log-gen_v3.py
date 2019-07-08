import time
import datetime
import numpy
import random
import argparse
import os
from faker import Faker
from tzlocal import get_localzone


parser = argparse.ArgumentParser(__file__, description="Fake Apache Log Generator")
parser.add_argument("--loc", "-l", dest='log_file_loc', help="Give the path to create the log file at a specifiic location")

args = parser.parse_args()

path_log_file = args.log_file_loc

local = get_localzone()
faker = Faker()
timestr = time.strftime("%Y%m%d-%H%M%S")
otime = datetime.datetime.now()


response=["200","404","500","301"]
verb=["GET","POST","DELETE","PUT"]
resources=["/list","/wp-content","/wp-admin","/explore","/search/tag/list","/app/main/posts","/posts/posts/explore","/apps/cart.jsp?appID="]
ualist = [faker.firefox, faker.chrome, faker.safari, faker.internet_explorer, faker.opera]

start_hour = otime.hour
flag = True

while(flag):
    current_time = datetime.datetime.now()
    i = random.randint(100,2000)
    time.sleep(random.randint(1,50))
    outFileName =  'Kafka_access_log_'+str(random.randint(1,150))+'_'+timestr+'.log'
    if (abs(start_hour - current_time.hour) > 0):
        flag =  False
    
    if args.log_file_loc:
        filepath = os.path.join(path_log_file,outFileName)
        print(filepath)
        f = open(filepath,'w')
    else:
        f = open(outFileName,'w')
   
    
    for i in range(random.randint(100,1000)):
        
        ip = faker.ipv4()
        dt = otime.strftime('%d/%b/%Y:%H:%M:%S')
        tz = datetime.datetime.now(local).strftime('%z')
        vrb = numpy.random.choice(verb,p=[0.6,0.1,0.1,0.2])
        otime += datetime.timedelta(seconds=random.randint(30, 300))
        
        uri = random.choice(resources)
        if uri.find("apps")>0:
            uri += str(random.randint(1000,10000))
        
        resp = numpy.random.choice(response,p=[0.9,0.04,0.02,0.04])
        byt = int(random.gauss(5000,50))
        referer = faker.uri()
        useragent = numpy.random.choice(ualist,p=[0.5,0.3,0.1,0.05,0.05] )()
        f.write('%s - - [%s %s] "%s %s HTTP/1.0" %s %s "%s" "%s"\n' % (ip,dt,tz,vrb,uri,resp,byt,referer,useragent))
        f.flush()
            
    f.close()
