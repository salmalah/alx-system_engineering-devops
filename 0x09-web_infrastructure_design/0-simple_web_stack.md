# Simple web stack

![img](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=0-simple_web_stack.drawio.png#R7VttU9s4EP41zLQf7PG7nY%2BQQHt3wNGGGe7uC6PYSqJiW0ZWSMKvP8mWHVsWSSgO0KF0ptir9332WWm15sgeJqsvBGTzCxzB%2BMgyotWRPTqyLNM0HfaLS9alxDONUjAjKBKVNoIxeoRCWFVboAjmrYoU45iirC0McZrCkLZkgBC8bFeb4rg9agZmsCMYhyDuSm9QROelNLD8jfwrRLN5NbLpDcqSBFSVxUryOYjwsiGyT4%2FsIcGYlk%2FJaghjrrxKL2W7sydK64kRmNJ9GlyOHsIhTPF4Hj9er9H4r1My1FwxN7quFgwjtn7xigmd4xlOQXy6kZ4QvEgjyHs12NumzjnGGROaTPgDUroWYIIFxUw0p0ksSrszF4vJ8YKEYh7frPUwO7YvzzG6uZyk9z%2BsP%2F7WRD0%2Bx0ZDsd4vECeQkjWrQGAMKHpoYwiEKczqenXTK4zYVCxDmO1AqEXYrOkY7R4oIDNIRaONytlDYxYbUQHEM0CphvuNSgsVu9KLgMWx3UPBsm2ZDyBeiCV0YGIcz%2Fhjsppxd6iHKA%2BxHuIkW1BI8luQRrcZJCibQwLiXI9BRjk8TRwyPn9ITh8YDrmQRSCf19hOURwPcYxJMaZt2F4w8Jk8pwTfwUbJtPipSyr%2FxfR78gAJRczLnYMJjK9wjijCKSubYEpx0qhwHKMZLyinCcRbCPkUuZ0taIxSNmjlfY1tlsQ7hautNiJKZagN8b7c%2BGCzcqzzhv%2F1jaetqmUPz%2BWkaXbAfi%2BczIaL1Z9gcvr95h6FPy58K7vXXouTptkGyh4czFVuW%2BY2TqKk2OJPQJ6VJjpFK45Jh3PFjN2TI3eksvQpTqnAyeQMEt2OUDJjM4%2FRhP0PHhcE8kWmkC4xuUMpLxtdjm%2F%2FwynM9fxh1g89PJkeXXYYCnbUwv7p4b0FPeAK0X%2FYs2bohhEIwb%2B8Pz0wqgqjlRigeFk3Xq6YJ2bL5%2FBu91tNtimXbw9eiW4y8JahW%2Fvtgp2%2Bal%2B56avdUbnqg51yzOBNTCZls65sxrYrSWk0buBVgo3VFG%2Fr5ttP2Y3afYnoqMRsW0W3bwPbl%2B5b5%2F1TfjdrqI%2BNxSI52NBoE6yOE65jKEM%2BFOUZCJm7vS7MwH7KP4dcNbcRImxGmOvhbAkntzkkzPX2553tQNoUbUt3ux7aVHlo29fdl4OmJJz1JkeYmnBmm2uOGbwy19x9uea8L665u7mW30EazoWKuoRTRBRPM6mBXTuiSNkZhgljKWSoydlXTCHHN4YZBKNyyq3gKslDAPWiVUZQDnWQZTHrnw8rON3HUcuVyGwpQxHdUZBZvjfozSasl5x735X%2FjQAFE5D3eji224iZyuDR0h
![img](https://drive.google.com/file/d/13zyK7LcRsUGSqxmNp2l3c3JdYqO1U5bF/view?usp=sharing)
>>>>>>> 55d196bca65fa57f5a70cbc58448a616bc671f90
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
