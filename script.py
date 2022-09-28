from asyncio.windows_events import NULL
from distutils.command.config import config
from optparse import Values
import time
from random import seed, random

import random
import sys
import logging

import jaydebeapi
import logicmonitor_data_sdk
import logicmonitor_sdk


# LogicMonitor metric data model is as below
#
# Company
#  |--- Resource (like device/service. Ex: VM)
#  |--- Data Source   (Ex. CPU)
#         |--- Instance (of a Data Source on a resource. Ex. CPU-1)
#               |--- Data Point (the metric which is being monitored. Ex. %Used)
#                     |- <Time> : <Metric Value>
#                     |- <Time> : <Metric Value>
#                     |...
#
from logicmonitor_data_sdk.api.metrics import Metrics
from logicmonitor_data_sdk.api.response_interface import ResonseInterface
from logicmonitor_data_sdk.api_client import ApiClient
from logicmonitor_data_sdk.models import DataSource, \
    Resource, DataSourceInstance, DataPoint

# Configure SDK with Account and access information
# On your LogicMonitor portal, create API token (LMv1) for user and get
# Access Id and Access Key

print("sys.argv ", sys.argv)
configuration = logicmonitor_data_sdk.Configuration(company='lmcameroncompton',
                                                    id='x23Qv9Qz8Xbu2RL36ij9',
                                                    key='lma_83y^^)5~He2yC^P5u7ha)j5[8R=I%YPWD]6jGH_^_899[cBBx^26233_hQk_LYTRiODIwMzMtZjYyZC00MjAxLWJhZTgtMmI3NTdiYjNlMTZkL43DKZk')

# how long instnace need to be retained , updated ?
# get to compare instance
# 2nd script to remove instances over data retention time range Check ilp to see if date is greater Reduces the api call
hostname = "172.31.15.51"
datasource_name = "SampleDS2"


logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
# create file handler which logs even debug messages


# deviceID 753

# datasource ID? 15142329
# hdsid 9276
# https://lmcameroncompton.logicmonitor.com/santaba/rest/device/devices/753/devicedatasources/9276?_=1662613258964

conn = jaydebeapi.connect("com.mysql.cj.jdbc.Driver", "jdbc:mysql://localhost:3306/testdb2", [
                          "root", "football12"], "C:\\Users\\Administrator\\Downloads\\New folder\\mysql-connector-java-8.0.30.jar")
curs = conn.cursor()

curs.execute("SELECT * FROM testtable ORDER BY sum_time DESC LIMIT 10")
data = curs.fetchall()
curs.close()
conn.close()
configuration2 = logicmonitor_sdk.Configuration()
configuration2.company = 'lmcameroncompton'
configuration2.access_id = 'x23Qv9Qz8Xbu2RL36ij9'
configuration2.access_key = 'lma_83y^^)5~He2yC^P5u7ha)j5[8R=I%YPWD]6jGH_^_899[cBBx^26233_hQk_LYTRiODIwMzMtZjYyZC00MjAxLWJhZTgtMmI3NTdiYjNlMTZkL43DKZk'

# configuration.api_key='lma_83y^^)5~He2yC^P5u7ha)j5[8R=I%YPWD]6jGH_^_899[cBBx^26233_hQk_LYTRiODIwMzMtZjYyZC00MjAxLWJhZTgtMmI3NTdiYjNlMTZkL43DKZk'
lmapi = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration2))

instancesListFromQuery = []
# 1 is the the first in the order form the query, 5 is the digest text.
# print(data[1][5])


class instanceData(object):
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value


for i in range(1, 10):
    instancesListFromQuery.append(instanceData(data[i][5], data[i][10]))

for x in range(len(instancesListFromQuery)):
    print(instancesListFromQuery[x].name)
    print(instancesListFromQuery[x].value)
    print('\n')


def get_instances_wildvalues_from_api(deviceID, hdsID):

    response = lmapi.get_device_datasource_instance_list(deviceID, hdsID)
    print(response)
    instancesListFromApi = []
    for item in response.items:
        # print(item.wild_value)
        instancesListFromApi.append(item.wild_value)
        return instancesListFromApi


class MyResponse(ResonseInterface):
    """
    Sample callback to handle the response from the REST endpoints
    """

    def success_callback(self, request, response, status, request_id):
        #logging.info("%s: %s: %s", response, status, request_id)
        print(response, status, request_id)

    def error_callback(self, request, response, status, request_id, reason):
        #logging.error("%s: %s: %s %s", response, status, reason, request_id)
        print(response, status, reason, request_id)


# Create api handle for Metrics use case (we also support Logs)
# Tokenize the system.hostname value to send metrics
# For each hostname
# dict of instance create and epoch value
configuration.logger_file_handler = fh
configuration.logger_file = "C:\\Users\\Administrator\\Desktop\\Python\\spam2.log"
configuration.debug = True
configuration.temp_folder_path = "C:\\Users\\Administrator\\Desktop\\Python\\"
configuration.async_req = True

api_client = ApiClient(configuration=configuration)
metric_api = Metrics(batch=True, interval=10,
                     response_callback=MyResponse(), api_client=api_client)


# get instances, determine what needs to be deleted. If needed to be added wait for send_metrics to do that
#
reponse = ""

resource = Resource(ids={"system.hostname": hostname})
datasource = DataSource(name=datasource_name)
datapointName = DataPoint(name="SampleDataPoint2")
DatapointValues = {str(int(time.time())): random.randint(1, 1000)}
system_displayname = "PushMetrics-172.31.15.51"
instanceName = "testinstance5"
# instancesApi=get_instances_wildvalues_from_api(753,9276)

instances
   try:
        return_val = metric_api.send_metrics(
            resource=Resource(
                ids={"system.displayname": system_displayname}, create=True),
            datasource=DataSource(
                name="SampleDS2"),  # Name of data source is must. Rest optional
            instance=DataSourceInstance(
                name=, groupName='test', properties={'updateTime': str(time.time())}),  # Name of instance is must. Rest optional
            datapoint=DataPoint(
                name="max_time"),  # The metric
            # Values at specific time(s)
            values={str(int(time.time())): int(obj.value)}
        )
        logger.debug('Sent Metric')
        print('return val ', return_val)

    except:
        logger.debug('Failed to send metric '
                     )
        pass


"""
for item in data:
    #print(str(item[1]))
    if not str(item[1]) or str(item[1]) is not NULL or str(item[1]) != "None":
        try:
            return_val=metric_api.send_metrics(
                resource=Resource(
                    ids={"system.displayname": system_displayname},create=True), 
                datasource=DataSource(
                    name="SampleDS2"),                         #Name of data source is must. Rest optional
                instance=DataSourceInstance(
                    name=str(instanceName),groupName='test',properties={'updateTime':str(time.time())}),                   #Name of instance is must. Rest optional
                datapoint=DataPoint(
                    name="SampleDataPoint2"),                  #The metric
                values={str(int(time.time())): str("0")} #Values at specific time(s)
            )
            logger.debug('Sent Metric')
            print('return val ',return_val)
            
        except:
            logger.debug('Failed to send metric '
            )
            pass
        try:
            #print("hello")
            response2=metric_api.update_instance_property(
            resource_ids={'system.displayname': system_displayname},
            datasource='SampleDS2',
            instancename=str(item[1]),
            instance_properties={'updatedTime':(time.time()),'groupName':'test'},
            patch=False)
            logger.debug('%s Updated instance with time %s',str(item[1]),str((time.time())))
            
        except: 
            logger.debug('This is a log message, could not update instnace for %s ',system_displayname)
            pass
"""


# print(response)

   #metric_api.send_metrics(resource, datasource,instance=DataSourceInstance(name=item[0]),datapoint=datapointName,Values=DatapointValues)
   # metric_api.send_metrics(resource, datasource,instance=DataSourceInstance(name="testinstance"),datapoint="testdatapoint",values={"time":"5"})#Values at specific time(s)
# manipulate payload to remove instances that we need to delete
# instance=DataSourceInstance{name='aa'}
