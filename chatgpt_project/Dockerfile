FROM python:3.8

# Set the working directory in the container to /app
WORKDIR /app

# Add current directory code to working directory in docker
ADD . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
#RUN source labot/bin/activate  # for Linux/Mac
RUN ls /app 
#RUN mkdir staticfiles

# Set the environment variable for Django
ENV DJANGO_SETTINGS_MODULE=chatgpt_project.settings

# Remove the STATIC_ROOT setting from the STATICFILES_DIRS list
RUN sed -i '/STATIC_ROOT =/d' chatgpt_project/settings.py


# Run Django migrations
RUN python manage.py migrate

RUN python manage.py collectstatic --noinput


# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the command to start uWSGI
CMD ["uwsgi", "--http", ":8000", "--module", "chatgpt_project.wsgi"]
