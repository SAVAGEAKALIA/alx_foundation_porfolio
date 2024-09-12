-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS blog_dev_db;
CREATE USER IF NOT EXISTS 'blog_dev'@'localhost' IDENTIFIED BY 'pwd';
GRANT ALL PRIVILEGES ON `blog_dev_db`.* TO 'blog_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'blog_dev'@'localhost';
FLUSH PRIVILEGES;