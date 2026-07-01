CREATE DATABASE intern_project0701;
GO

USE intern_project0701;
GO

CREATE TABLE users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    username NVARCHAR(50) NOT NULL UNIQUE,
    password NVARCHAR(255) NOT NULL,
    display_name NVARCHAR(50),
    department NVARCHAR(100),
    staff_id NVARCHAR(20),
    email NVARCHAR(100),
    system_role NVARCHAR(50)
);
GO

INSERT INTO users (username, password, display_name, department, staff_id, email, system_role) 
VALUES ('testuser', 'password123', N'陳佳君', N'醫學資訊學系', 'MI-2026', 'cjj91@example.com', '系統管理員');
GO