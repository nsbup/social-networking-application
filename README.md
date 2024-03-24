# social-networking-application
RUN Commands

  

   docker build -t django-social-app .

   docker network create my-django-postgres-network

   docker run --name django-social-app-c1 -p 8000:8000 --network my-django-postgres-network -d django-social-app


   ---------------------------------------------------------------------------------

   

   
