

CREATE DATABASE Hostelacc;
USE HostelAccommodation;

-- Hostel Table
CREATE TABLE Hostel (
    Hostel_ID INT PRIMARY KEY AUTO_INCREMENT,
    Hostel_Name VARCHAR(100) NOT NULL,
    Gender_Type ENUM('Male', 'Female') NOT NULL,
    Address VARCHAR(200),
    Total_Rooms INT DEFAULT 300,
    Rent DECIMAL(10,2) NOT NULL
);


-- Room Table
CREATE TABLE Room (
    Room_ID INT PRIMARY KEY,
    Hostel_ID INT,
    Room_No VARCHAR(10),
    Room_Type ENUM('Single', 'Double', 'Triple') NOT NULL,
    Availability_Status ENUM('Available', 'Occupied') DEFAULT 'Available',
    FOREIGN KEY (Hostel_ID) REFERENCES Hostel(Hostel_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Student Table
CREATE TABLE Student (
    Student_ID INT PRIMARY KEY AUTO_INCREMENT,
    Student_Name VARCHAR(100),
    Gender ENUM('Male', 'Female'),
    Contact_No VARCHAR(15),
    Email VARCHAR(100),
    Hostel_ID INT,
    Room_ID INT,
    FOREIGN KEY (Hostel_ID) REFERENCES Hostel(Hostel_ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (Room_ID) REFERENCES Room(Room_ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Booking Table
CREATE TABLE Booking (
    Booking_ID INT PRIMARY KEY AUTO_INCREMENT,
    Student_ID INT,
    Room_ID INT,
    CheckIn_Date DATE,
    CheckOut_Date DATE,
    Status ENUM('Active', 'Cancelled', 'Completed'),
    FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (Room_ID) REFERENCES Room(Room_ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Payment Table
CREATE TABLE Payment (
    Payment_ID INT PRIMARY KEY AUTO_INCREMENT,
    Booking_ID INT,
    Amount DECIMAL(10,2),
    Payment_Date DATE,
    Mode ENUM('Online', 'Cash', 'UPI'),
    FOREIGN KEY (Booking_ID) REFERENCES Booking(Booking_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Complaint Table
CREATE TABLE Complaint (
    Complaint_ID INT PRIMARY KEY AUTO_INCREMENT,
    Student_ID INT,
    Room_ID INT,
    Description VARCHAR(255),
    Status ENUM('Pending', 'Resolved') DEFAULT 'Pending',
    FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (Room_ID) REFERENCES Room(Room_ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);


UPDATE Hostel SET Rent = 15000;

ALTER TABLE Payment 
ADD Month_Year VARCHAR(7) AFTER Payment_Date;





USE Hostelacc;
SET FOREIGN_KEY_CHECKS = 0;

-- Insert Hostels
INSERT INTO Hostel (Hostel_ID, Hostel_Name, Gender_Type, Address, Total_Rooms, Rent)
VALUES
(1, 'PESU Boys Hostel', 'Male', 'PES University EC Campus, Hosur Road, Bangalore', 300, 100000.00),
(2, 'Amaatra Girls Hostel', 'Female', 'Amaatra Campus, Electronic City, Bangalore', 300, 90000.00);



--  Insert rooms
INSERT INTO Room (Room_ID, Hostel_ID, Room_No, Room_Type, Availability_Status)
VALUES
--  Boys Hostel (Hostel_ID = 1)
(101, 1, 'B101', 'Double', 'Available'),
(102, 1, 'B102', 'Double', 'Available'),
(103, 1, 'B103', 'Double', 'Available'),
(104, 1, 'B104', 'Double', 'Available'),
(105, 1, 'B105', 'Double', 'Available'),
(106, 1, 'B106', 'Double', 'Available'),
(107, 1, 'B107', 'Double', 'Available'),
(108, 1, 'B108', 'Double', 'Available'),
(109, 1, 'B109', 'Double', 'Available'),
(110, 1, 'B110', 'Double', 'Available'),
(111, 1, 'B111', 'Double', 'Available'),
(112, 1, 'B112', 'Double', 'Available'),
(113, 1, 'B113', 'Double', 'Available'),
(114, 1, 'B114', 'Double', 'Available'),
(115, 1, 'B115', 'Double', 'Available'),
(116, 1, 'B116', 'Double', 'Available'),
(117, 1, 'B117', 'Double', 'Available'),
(118, 1, 'B118', 'Double', 'Available'),
(119, 1, 'B119', 'Double', 'Available'),
(120, 1, 'B120', 'Double', 'Available'),

-- 2nd Floor Boys Hostel
(121, 1, 'B201', 'Double', 'Available'),
(122, 1, 'B202', 'Double', 'Available'),
(123, 1, 'B203', 'Double', 'Available'),
(124, 1, 'B204', 'Double', 'Available'),
(125, 1, 'B205', 'Double', 'Available'),
(126, 1, 'B206', 'Double', 'Available'),
(127, 1, 'B207', 'Double', 'Available'),
(128, 1, 'B208', 'Double', 'Available'),
(129, 1, 'B209', 'Double', 'Available'),
(130, 1, 'B210', 'Double', 'Available'),
(131, 1, 'B211', 'Double', 'Available'),
(132, 1, 'B212', 'Double', 'Available'),
(133, 1, 'B213', 'Double', 'Available'),
(134, 1, 'B214', 'Double', 'Available'),
(135, 1, 'B215', 'Double', 'Available'),
(136, 1, 'B216', 'Double', 'Available'),
(137, 1, 'B217', 'Double', 'Available'),
(138, 1, 'B218', 'Double', 'Available'),
(139, 1, 'B219', 'Double', 'Available'),
(140, 1, 'B220', 'Double', 'Available'),

-- 3rd Floor Boys Hostel
(141, 1, 'B301', 'Double', 'Available'),
(142, 1, 'B302', 'Double', 'Available'),
(143, 1, 'B303', 'Double', 'Available'),
(144, 1, 'B304', 'Double', 'Available'),
(145, 1, 'B305', 'Double', 'Available'),
(146, 1, 'B306', 'Double', 'Available'),
(147, 1, 'B307', 'Double', 'Available'),
(148, 1, 'B308', 'Double', 'Available'),
(149, 1, 'B309', 'Double', 'Available'),
(150, 1, 'B310', 'Double', 'Available'),
(151, 1, 'B311', 'Double', 'Available'),
(152, 1, 'B312', 'Double', 'Available'),
(153, 1, 'B313', 'Double', 'Available'),
(154, 1, 'B314', 'Double', 'Available'),
(155, 1, 'B315', 'Double', 'Available'),
(156, 1, 'B316', 'Double', 'Available'),
(157, 1, 'B317', 'Double', 'Available'),
(158, 1, 'B318', 'Double', 'Available'),
(159, 1, 'B319', 'Double', 'Available'),
(160, 1, 'B320', 'Double', 'Available'),

--  Girls Hostel (Hostel_ID = 2)
(204, 2, 'G101', 'Double', 'Available'),
(205, 2, 'G102', 'Double', 'Available'),
(206, 2, 'G103', 'Double', 'Available'),
(207, 2, 'G104', 'Double', 'Available'),
(208, 2, 'G105', 'Double', 'Available'),
(209, 2, 'G106', 'Double', 'Available'),
(210, 2, 'G107', 'Double', 'Available'),
(211, 2, 'G108', 'Double', 'Available'),
(212, 2, 'G109', 'Double', 'Available'),
(213, 2, 'G110', 'Double', 'Available'),
(214, 2, 'G111', 'Double', 'Available'),
(215, 2, 'G112', 'Double', 'Available'),
(216, 2, 'G113', 'Double', 'Available'),
(217, 2, 'G114', 'Double', 'Available'),
(218, 2, 'G115', 'Double', 'Available'),
(219, 2, 'G116', 'Double', 'Available'),
(220, 2, 'G117', 'Double', 'Available'),
(221, 2, 'G118', 'Double', 'Available'),
(222, 2, 'G119', 'Double', 'Available'),
(223, 2, 'G120', 'Double', 'Available'),

-- 2nd Floor Girls Hostel 
(201, 2, 'G201', 'Double', 'Occupied'),
(202, 2, 'G202', 'Double', 'Available'),
(203, 2, 'G203', 'Double', 'Available'),
(224, 2, 'G204', 'Double', 'Available'),
(225, 2, 'G205', 'Double', 'Available'),
(226, 2, 'G206', 'Double', 'Available'),
(227, 2, 'G207', 'Double', 'Available'),
(228, 2, 'G208', 'Double', 'Available'),
(229, 2, 'G209', 'Double', 'Available'),
(230, 2, 'G210', 'Double', 'Available'),
(231, 2, 'G211', 'Double', 'Available'),
(232, 2, 'G212', 'Double', 'Available'),
(233, 2, 'G213', 'Double', 'Available'),
(234, 2, 'G214', 'Double', 'Available'),
(235, 2, 'G215', 'Double', 'Available'),
(236, 2, 'G216', 'Double', 'Available'),
(237, 2, 'G217', 'Double', 'Available'),
(238, 2, 'G218', 'Double', 'Available'),
(239, 2, 'G219', 'Double', 'Available'),
(240, 2, 'G220', 'Double', 'Available'),

-- 3rd Floor Girls Hostel
(241, 2, 'G301', 'Double', 'Available'),
(242, 2, 'G302', 'Double', 'Available'),
(243, 2, 'G303', 'Double', 'Available'),
(244, 2, 'G304', 'Double', 'Available'),
(245, 2, 'G305', 'Double', 'Available'),
(246, 2, 'G306', 'Double', 'Available'),
(247, 2, 'G307', 'Double', 'Available'),
(248, 2, 'G308', 'Double', 'Available'),
(249, 2, 'G309', 'Double', 'Available'),
(250, 2, 'G310', 'Double', 'Available'),
(251, 2, 'G311', 'Double', 'Available'),
(252, 2, 'G312', 'Double', 'Available'),
(253, 2, 'G313', 'Double', 'Available'),
(254, 2, 'G314', 'Double', 'Available'),
(255, 2, 'G315', 'Double', 'Available'),
(256, 2, 'G316', 'Double', 'Available'),
(257, 2, 'G317', 'Double', 'Available'),
(258, 2, 'G318', 'Double', 'Available'),
(259, 2, 'G319', 'Double', 'Available'),
(260, 2, 'G320', 'Double', 'Available');





SET FOREIGN_KEY_CHECKS = 1;





-- Trigger: When a booking is created → mark room as Occupied
DELIMITER $$

CREATE TRIGGER after_booking_insert
AFTER INSERT ON Booking
FOR EACH ROW
BEGIN
    UPDATE Room
    SET Availability_Status = 'Occupied'
    WHERE Room_ID = NEW.Room_ID;
END $$

DELIMITER ;



-- Trigger: When booking is Cancelled → make room Available
DELIMITER $$
CREATE TRIGGER after_booking_update
AFTER UPDATE ON Booking
FOR EACH ROW
BEGIN
    IF NEW.Status = 'Cancelled' THEN
        UPDATE Room
        SET Availability_Status = 'Available'
        WHERE Room_ID = NEW.Room_ID;
    END IF;
END;
DELIMITER ;



-- Trigger: When student is assigned a room → mark room Occupied
DELIMITER $$
CREATE TRIGGER after_student_update
AFTER UPDATE ON Student
FOR EACH ROW
BEGIN
    IF NEW.Room_ID IS NOT NULL THEN
        UPDATE Room SET Availability_Status='Occupied'
        WHERE Room_ID = NEW.Room_ID;
    END IF;
END;
DELIMITER ;




-- Stored FUNCTION to Calculate Total Rent for Booking
DELIMITER $$

CREATE FUNCTION calculate_rent(roomId INT, days INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE room_rent DECIMAL(10,2);

    SELECT Rent INTO room_rent
    FROM Hostel
    JOIN Room ON Room.Hostel_ID = Hostel.Hostel_ID
    WHERE Room.Room_ID = roomId;

    RETURN room_rent * days;
END $$

DELIMITER ;




-- Stored PROCEDURE to Create Booking Safely
DELIMITER $$

CREATE PROCEDURE create_booking(
    IN p_student INT,
    IN p_room INT,
    IN p_checkin DATE,
    IN p_checkout DATE
)
BEGIN
    INSERT INTO Booking(Student_ID, Room_ID, CheckIn_Date, CheckOut_Date, Status)
    VALUES(p_student, p_room, p_checkin, p_checkout, 'Active');
END $$

DELIMITER ;





-- Stored PROCEDURE to Delete Student + Auto Update Room
DELIMITER $$

CREATE PROCEDURE delete_student(IN p_studentId INT)
BEGIN
    DECLARE r INT;

    -- Get room
    SELECT Room_ID INTO r FROM Student WHERE Student_ID = p_studentId;

    -- Delete student
    DELETE FROM Student WHERE Student_ID = p_studentId;

    -- Make room available
    UPDATE Room SET Availability_Status='Available' WHERE Room_ID=r;
END $$

DELIMITER ;




-- Procedures for UI Add Complaint
DELIMITER $$
CREATE PROCEDURE add_complaint(p_student INT, p_room INT, p_desc VARCHAR(255))
BEGIN
    INSERT INTO Complaint(Student_ID, Room_ID, Description)
    VALUES(p_student, p_room, p_desc);
END;
DELIMITER ;



-- Procedure for marking complaint as resolved
DELIMITER $$

CREATE PROCEDURE resolve_complaint(p_id INT)
BEGIN
    UPDATE Complaint 
    SET Status='Resolved'
    WHERE Complaint_ID = p_id;
END $$

DELIMITER ;







-- VIEW: Students with Room + Hostel Info
CREATE OR REPLACE VIEW view_students AS
SELECT 
    s.Student_ID,
    s.Student_Name,
    s.Gender,
    s.Contact_No,
    s.Email,
    s.Hostel_ID,
    h.Hostel_Name,
    h.Gender_Type AS Hostel_Gender,
    s.Room_ID,
    r.Room_No,
    r.Room_Type,
    r.Availability_Status
FROM Student s
LEFT JOIN Hostel h ON s.Hostel_ID = h.Hostel_ID
LEFT JOIN Room r ON s.Room_ID = r.Room_ID;








-- VIEW: Booking Info (Student + Room + Hostel)
CREATE OR REPLACE VIEW view_bookings AS
SELECT 
    b.Booking_ID,
    b.Student_ID,
    s.Student_Name,
    b.Room_ID,
    r.Room_No,
    r.Room_Type,
    h.Hostel_Name,
    b.CheckIn_Date,
    b.CheckOut_Date,
    b.Status
FROM Booking b
LEFT JOIN Student s ON b.Student_ID = s.Student_ID
LEFT JOIN Room r ON b.Room_ID = r.Room_ID
LEFT JOIN Hostel h ON r.Hostel_ID = h.Hostel_ID;







-- VIEW: Payments with Booking + Student
CREATE OR REPLACE VIEW view_payments AS
SELECT
    p.Payment_ID,
    p.Booking_ID,
    s.Student_Name,
    r.Room_No,
    p.Amount,
    p.Payment_Date,
    p.Mode
FROM Payment p
LEFT JOIN Booking b ON p.Booking_ID = b.Booking_ID
LEFT JOIN Student s ON b.Student_ID = s.Student_ID
LEFT JOIN Room r ON b.Room_ID = r.Room_ID;






-- VIEW: Complaints with Student + Room
CREATE OR REPLACE VIEW view_complaints AS
SELECT
    c.Complaint_ID,
    s.Student_Name,
    c.Room_ID,
    r.Room_No,
    c.Description,
    c.Status
FROM Complaint c
LEFT JOIN Student s ON c.Student_ID = s.Student_ID
LEFT JOIN Room r ON c.Room_ID = r.Room_ID;



-- view for pending payments
CREATE OR REPLACE VIEW view_pending_dues AS
SELECT 
    s.Student_ID,
    s.Student_Name,
    b.Booking_ID,
    h.Rent AS Monthly_Rent,
    DATE_FORMAT(CURDATE(), '%Y-%m') AS Current_Month
FROM Student s
JOIN Booking b ON s.Student_ID = b.Student_ID AND b.Status = 'Active'
JOIN Hostel h ON s.Hostel_ID = h.Hostel_ID
WHERE NOT EXISTS (
    SELECT 1 FROM Payment p
    WHERE p.Booking_ID = b.Booking_ID
      AND p.Month_Year = DATE_FORMAT(CURDATE(), '%Y-%m')
);
