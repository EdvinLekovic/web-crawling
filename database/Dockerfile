FROM postgres

ENV POSTGRES_HOST='db'
ENV POSTGRES_USER='postgres'
ENV POSTGRES_PASSWORD='postgres'
ENV POSTGRES_DB='apartmentsDB'
ENV POSTGRES_PORT='5432'

COPY create_table.sql /docker-entrypoint-initdb.d/create_table.sql