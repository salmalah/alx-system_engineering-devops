# Distributed web infrastructure:
![img](1-distributed_web_infrastructure.drawio.png)
## Element:
* Web Servers (Nginx):
We include two web servers running Nginx to handle user requests.
* Load Balancer (HAproxy):
  We add a load balancer to distribute incoming user requests across multiple web servers
* Application Serve:
  We have one application server to host the application code base and process dynamic content
* Database (MySQL):
    We set up a Primary-Replica cluster for the database. This configuration includes one primary (master) database server and one or more replica (slave) database servers. The primary server handles read-write operations
* Application Files:
    The application files contain the website's codebase, including HTML, CSS These files are stored on the application server and are utilized to generate dynamic web content
##  about the Infrastructure:
* The load balancer is added to distribute incoming user requests across the two web servers. It uses a Round Robin distribution algorithm by defaul
* In this infrastructure, we are using an Active-Active setup both web servers are actively serving traffic simultaneously. an Active-Passive setup involves one server actively serving traffic while the other remains in standby mode, only taking over if the active server fails
* Primary-Replica cluster, the primary database server is responsible for handling write operations and maintaining the most up-to-date data
* The application communicates with the primary node of the database for write operations as only the primary is allowed to modify the data either the primary or any of the replica nodes since the replicas have a read-only copy of the data
