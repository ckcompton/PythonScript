import time
from random import seed, random
import jaydebeapi 
import random


import logicmonitor_data_sdk





# LogicMonitor metric data model is as below
#
#Company
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
configuration = logicmonitor_data_sdk.Configuration(company='lmcameroncompton',
                                                    id='x23Qv9Qz8Xbu2RL36ij9',
                                                    key='lma_83y^^)5~He2yC^P5u7ha)j5[8R=I%YPWD]6jGH_^_899[cBBx^26233_hQk_LYTRiODIwMzMtZjYyZC00MjAxLWJhZTgtMmI3NTdiYjNlMTZkL43DKZk')
configuration.debug="true"

conn = jaydebeapi.connect("com.mysql.cj.jdbc.Driver","jdbc:mysql://localhost:3306/testdb",["root", "football12"], "C:\\Users\\Administrator\\Downloads\\New folder\\mysql-connector-java-8.0.30.jar")
#conn=jaydebeapi.connect("org.mariadb.jdbc.Driver","jdbc:mariadb://localhost:3306/testdb",["root", "football12"],"C:\\Users\\Administrator\\Downloads\\New folder\\mariadb-java-client-3.0.7.jar")
curs = conn.cursor()

curs.execute("SELECT * FROM recipes")
data = curs.fetchall()
curs.close()
conn.close()


randnumber = random.randint(0,9)
print(data[randnumber][0])
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
api_client = ApiClient(configuration=configuration)
metric_api = Metrics(batch=False,interval=10,response_callback=MyResponse(),api_client=api_client)
return_val = metric_api.send_metrics(
               resource=Resource(
                   ids={"system.hostname": "172.31.15.51"}), 
               datasource=DataSource(
                   name="SampleDS2"),                         #Name of data source is must. Rest optional
               instance=DataSourceInstance(
                   name="TestInstance"),                   #Name of instance is must. Rest optional
               datapoint=DataPoint(
                  name="SampleDataPoint2"),                  #The metric
               values={str(int(time.time())): 12} #Values at specific time(s)
)
print("Return Value = ",return_val)
