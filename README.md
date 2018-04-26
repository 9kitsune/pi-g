# pi-g
Luminaire vibration monitoring

0. set the rc.local so the service python script run on start up
A. The Service python script needs to be improved to do the following:
1. run the actual logging script for the specified time
2. save the actual recording files
3. restart the logging script for aforementioned period.
4. Monitor disk space and stop logging when freespace < 10% total disk space.

B. The logging python script needs to be refined so:
1. Data Sample Rate is quick as possible.
2. Logging duration needs to increase to 4 hours.
3. log all sensors.
