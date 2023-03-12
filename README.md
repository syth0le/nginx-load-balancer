# nginx-load-balancer
this repo was created for learning main features of nginx+docker

for run execute command:
```shell
docker-compose up -d --build --scale app=3
```

after that execute this command 10 times:
```shell
curl localhost
```
You will get different outputs each time:
```shell
> curl localhost
--- {"message":"Hello, this is container: b1f0411005e9"}
> curl localhost
--- {"message":"Hello, this is container: 5f119e8a9667"}
> curl localhost
--- {"message":"Hello, this is container: b1f0411005e9"}
> curl localhost
--- {"message":"Hello, this is container: 3674815eaa4c"}
...
```
