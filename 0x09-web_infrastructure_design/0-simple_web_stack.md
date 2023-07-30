# Simple web stack

[URL](https://drive.google.com/file/d/13zyK7LcRsUGSqxmNp2l3c3JdYqO1U5bF/view?usp=sharing)
![img](https://github.com/salmalah/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack.drawio.png)
## server:
is a computer system or a software program that provides services or resources to other computers on a network in our case server has an IP address of 8.8.8.8
## Domain name role:
The domain name system (DNS) is responsible for translating domain names into IP addresses in our case domain name (foobar.com) it gets directed to the server with IP 8.8.8.8
## Type of DNS record www is in www.foobar.com:
The "www" is a subdomain
## The role of the web server:
is to handle incoming HTTP requests from users web browsers and respond with the requested web pages. in our case we use Nginx is a popular web server software
## The role of the application server:
hosts the website's application code base. It processes dynamic content and generates web pages to be served by the web server
## The role of the database:
stores and manages the website's data, such as user information, content, and other application-related data. in our case we use MySQL is a relational database management system (RDBMS) known for its reliability and scalability
## The server using to communicate with the computer of the user requesting the website
The web server (Nginx) receives this request, and if the content is static, it can directly serve it back to the user's browser
