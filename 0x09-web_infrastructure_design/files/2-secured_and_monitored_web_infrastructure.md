# Secured and monitored web infrastructure
![img](2-secured_and_monitored_web_infrastructure.drawio.png)
* Firewalls:
Three firewalls are added to the infrastructure to protect the servers from unauthorized access and potential security threats. They act as a security perimeter and control incoming and outgoing traffic based on predefined rules.
* SSL Certificate for HTTPS:
  The SSL certificate allows the website to serve encrypted traffic (HTTPS) to users, ensuring data confidentiality and integrity during transmission.
  ## Specifics about the Infrastructure:
  * Firewalls are added to enhance security by controlling network traffic. They filter incoming and outgoing traffic based on predefined rules, protecting the servers from unauthorized access and potential attacks.
  * Serving traffic over HTTPS ensures that data transmitted between users and the website is encrypted, protecting sensitive information such as login credentials and payment details from eavesdropping and tampering
  * Monitoring is used to track the health, performance, and security of the infrastructure. It helps in identifying issues proactively, optimizing resource usage, and detecting potential security threats.
  * Monitoring clients (data collectors) are installed on each server. These agents collect various metrics, such as CPU usage, memory usage, network traffic, and application logs
  * the monitoring tool would collect and analyze web server access logs. The logs can be parsed to count the number of incoming requests per second, helping to understand the server's load and identify any potential performance bottlenecks.
## Issues with this Infrastructure:
* Terminating SSL at the load balancer means that decrypted traffic is passed to the web servers internally
* Having only one MySQL server capable of accepting writes creates a single point of failure for write operations
* Uniformity across all servers might lead to homogeneous failure modes
