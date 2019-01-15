FROM ubuntu

# install tools 
RUN apt-get update
RUN apt-get -y install curl gnupg python3.7
RUN apt-get -y install python3-pip

# Get driver for pyodbc https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN  apt-key --keyring /etc/apt/trusted.gpg.d/Microsoft.gpg adv --keyserver packages.microsoft.com --recv-keys BC528686B50D79E339D3721CEB3E94ADBE1229CF

# install driver odbc
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get -y install msodbcsql17
RUN apt-get -y install unixodbc-dev
# lib pour driver sql 17 sous ubuntu 
RUN apt install libssl1.0

#Install app and requirement 
RUN mkdir - p /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN  pip3 install --upgrade -r requirements.txt

EXPOSE 8000

RUN echo 'we are running some # of cool things'
# command to be run when container is started 
CMD python3 manage.py runserver 0.0.0.0:8000

# to create the docker image : docker build -f django-ubuntu.dockerfile -t mydjangoubuntu .
