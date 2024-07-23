FROM dpage/pgadmin4:latest

# Change ownership of the /var/lib/pgadmin directory to pgadmin user
USER root
RUN chown -R 5050:5050 /var/lib/pgadmin

# Expose the necessary ports
EXPOSE 80

# Entrypoint and CMD are inherited from the base image
