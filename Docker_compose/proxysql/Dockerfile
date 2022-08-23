FROM debian:11

MAINTAINER Rene Cannao <rene@proxysql.com>

RUN apt-get update && apt-get install -y wget lsb-release gnupg apt-transport-https ca-certificates && wget -O - 'https://repo.proxysql.com/ProxySQL/repo_pub_key' | apt-key add - && echo deb https://repo.proxysql.com/ProxySQL/proxysql-2.3.x/$(lsb_release -sc)/ ./ | tee /etc/apt/sources.list.d/proxysql.list && apt-get update && apt-get install proxysql && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["proxysql", "-f", "--idle-threads", "-D", "/var/lib/proxysql"]