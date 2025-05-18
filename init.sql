CREATE USER iot_user WITH PASSWORD 'iot_pass';
CREATE DATABASE iot_data_db OWNER iot_user;
    CREATE TABLE IF NOT EXISTS sensor_readings (
        id INT PRIMARY KEY,
        temperature FLOAT NOT NULL,
        humidity FLOAT NOT NULL
    );
