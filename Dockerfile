# To run app we need python3.14
FROM python:3.14

# creating working directory
WORKDIR /app

# Copy contents to container
COPY . /app

# Expose container port
EXPOSE 8000

# run requirement
RUN pip install -r requirements.txt

# run the script
CMD ["python","main.py"]
