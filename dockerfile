FROM continuumio/anaconda3

# Copy your application code and requirements.txt
COPY . /app/

# Set the working directory
WORKDIR /app


# Install other Python packages from requirements.txt
RUN pip install -r requirements.txt

# Specify the command to run your application
CMD ["python", "app.py"]
