# 1. Use an official, lightweight Python image
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file and install the libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy your production Python script into the container
COPY fendiline_optimization.py .

# 5. Command to run the script automatically
CMD ["python", "fendiline_optimization.py"]
