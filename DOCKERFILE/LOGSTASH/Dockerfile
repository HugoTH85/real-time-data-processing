FROM docker.elastic.co/logstash/logstash:7.10.1

RUN bin/logstash-plugin install logstash-input-mongodb
COPY ../../Services/logstash/conf/mongodb.conf /usr/share/logstash/pipeline/logstash.conf