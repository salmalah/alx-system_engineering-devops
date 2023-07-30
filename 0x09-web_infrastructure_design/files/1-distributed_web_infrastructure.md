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
