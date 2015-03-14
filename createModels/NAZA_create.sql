-- Created by Vertabelo (http://vertabelo.com)
-- Script type: create
-- Scope: [tables, references, sequences, views, procedures]
-- Generated at Sat Mar 14 05:40:31 UTC 2015



-- tables
-- Table: Attendance
CREATE TABLE Attendance (
    date datetime NOT NULL,
    session_schedule_id integer NOT NULL,
    attendance_status varchar(1) NOT NULL,
    student_id integer NOT NULL,
    attendance_comment varchar(255) NOT NULL,
    partner_id integer NOT NULL,
    CONSTRAINT Attendance_pk PRIMARY KEY (date,session_schedule_id,student_id),
    FOREIGN KEY (session_schedule_id) REFERENCES SessionSchedule (id),
    FOREIGN KEY (partner_id) REFERENCES EnhancementPartner (partner_id),
    FOREIGN KEY (student_id) REFERENCES Student (id)
);

-- Table: EnhancementPartner
CREATE TABLE EnhancementPartner (
    partner_id integer NOT NULL  PRIMARY KEY,
    partner_name varchar(100) NOT NULL
);

-- Table: EnhancementPartnerSchedule
CREATE TABLE EnhancementPartnerSchedule (
    partner_id integer NOT NULL,
    session_schedule_id integer NOT NULL,
    date date NOT NULL,
    comment varchar(255) NOT NULL,
    CONSTRAINT EnhancementPartnerSchedule_pk PRIMARY KEY (partner_id,session_schedule_id,date),
    FOREIGN KEY (partner_id) REFERENCES EnhancementPartner (partner_id),
    FOREIGN KEY (session_schedule_id) REFERENCES SessionSchedule (id)
);

-- Table: Program
CREATE TABLE Program (
    id integer NOT NULL  PRIMARY KEY,
    name varchar(50) NOT NULL,
    zone_id integer NOT NULL,
    program_description varchar(200) NOT NULL,
    Interval_code integer NOT NULL,
    FOREIGN KEY (zone_id) REFERENCES Zone (id)
);

-- Table: School
CREATE TABLE School (
    id integer NOT NULL  PRIMARY KEY,
    district_id integer NOT NULL,
    name varchar(50) NOT NULL
);

-- Table: Session
CREATE TABLE Session (
    id integer NOT NULL  PRIMARY KEY,
    name varchar(50) NOT NULL,
    program_id integer NOT NULL,
    session_description integer NOT NULL,
    FOREIGN KEY (program_id) REFERENCES Program (id)
);

-- Table: SessionCancelDate
CREATE TABLE SessionCancelDate (
    session_schedule_id integer NOT NULL,
    date datetime NOT NULL,
    comment varchar(255) NOT NULL,
    CONSTRAINT SessionCancelDate_pk PRIMARY KEY (session_schedule_id,date),
    FOREIGN KEY (session_schedule_id) REFERENCES SessionSchedule (id)
);

-- Table: SessionForStudent
CREATE TABLE SessionForStudent (
    id integer NOT NULL  PRIMARY KEY,
    session_schedule_id integer NOT NULL,
    Student_id integer NOT NULL,
    effective_date date NOT NULL,
    ending_date integer NOT NULL,
    date_stamp date NOT NULL,
    FOREIGN KEY (session_schedule_id) REFERENCES SessionSchedule (id),
    FOREIGN KEY (Student_id) REFERENCES Student (id)
);

-- Table: SessionSchedule
CREATE TABLE SessionSchedule (
    id integer NOT NULL  PRIMARY KEY,
    session_id integer NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL,
    school_year integer NOT NULL,
    comments varchar(255) NOT NULL,
    teacher_id integer NOT NULL,
    location varchar(200) NOT NULL,
    FOREIGN KEY (session_id) REFERENCES Session (id),
    FOREIGN KEY (teacher_id) REFERENCES Teacher (id)
);

-- Table: Student
CREATE TABLE Student (
    id integer NOT NULL  PRIMARY KEY,
    local_student_id integer NOT NULL,
    school_id integer NOT NULL,
    last_name varchar(35) NOT NULL,
    first_name varchar(35) NOT NULL,
    middle_name varchar(35) NOT NULL,
    DOB date NOT NULL,
    gender varchar(1) NOT NULL,
    grade_level varchar(2) NOT NULL,
    location_type_id varchar(10) NOT NULL,
    address varchar(100) NOT NULL,
    city varchar(30) NOT NULL,
    state varchar(2) NOT NULL,
    zip_code varchar(10) NOT NULL,
    phone_number varchar(15) NOT NULL,
    date_stamp datetime NOT NULL,
    FOREIGN KEY (school_id) REFERENCES School (id)
);

-- Table: Teacher
CREATE TABLE Teacher (
    id integer NOT NULL  PRIMARY KEY,
    last_name varchar(35) NOT NULL,
    first_name varchar(35) NOT NULL,
    DOB date NOT NULL,
    email varchar(100) NOT NULL,
    phone_number varchar(15) NOT NULL
);

-- Table: Zone
CREATE TABLE Zone (
    id integer NOT NULL  PRIMARY KEY,
    name varchar(50) NOT NULL,
    zone_description varchar(200) NOT NULL
);





-- End of file.

