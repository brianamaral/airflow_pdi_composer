FROM openjdk:8

RUN curl https://ufpr.dl.sourceforge.net/project/pentaho/Pentaho%209.0/client-tools/pdi-ce-9.0.0.0-423.zip --output pdi.zip \
&& unzip pdi.zip
WORKDIR /data-integration
COPY ./configs/ .
CMD [ "./carte.sh", "config.xml" ]
EXPOSE 8080