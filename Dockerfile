# Menggunakan base image yang mengandung Python
FROM python:3

# Install dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# Menetapkan working directory di dalam container
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt requirements.txt

# Menginstall dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin seluruh file proyek ke dalam container
COPY . .

# Menjalankan aplikasi menggunakan Gunicorn dengan WSGI
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]