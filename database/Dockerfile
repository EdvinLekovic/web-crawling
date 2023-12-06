FROM postgres

ENV POSTGRES_HOST='db'
ENV POSTGRES_USER='postgres'
ENV POSTGRES_PASSWORD='postgres'
ENV POSTGRES_DB='apartmentsDB'

COPY create_table.sql /docker-entrypoint-initdb.d/create_table.sql