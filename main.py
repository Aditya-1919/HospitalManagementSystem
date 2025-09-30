import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # default XAMPP password is empty
    database="hospital_db"
)

cursor = conn.cursor()
print("Connected to hospital_db successfully!")

cursor.close()
conn.close()

def add_patient(name, age, gender, contact):
    query = "INSERT INTO Patients (name, age, gender, contact) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, age, gender, contact))
    conn.commit()
    print("Patient added successfully!")

def add_doctor(name, specialization, contact):
    query = "INSERT INTO Doctors (name, specialization, contact) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, specialization, contact))
    conn.commit()
    print("Doctor added successfully!")

from prettytable import PrettyTable

def list_patients():
    cursor.execute("SELECT * FROM Patients")
    rows = cursor.fetchall()
    table = PrettyTable(["ID", "Name", "Age", "Gender", "Contact"])
    for row in rows:
        table.add_row(row)
    print(table)

def list_doctors():
    cursor.execute("SELECT * FROM Doctors")
    rows = cursor.fetchall()
    table = PrettyTable(["ID", "Name", "Specialization", "Contact"])
    for row in rows:
        table.add_row(row)
    print(table)



def schedule_appointment(patient_id, doctor_id, date, time):
    query = "INSERT INTO Appointments (patient_id, doctor_id, appointment_date, appointment_time) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (patient_id, doctor_id, date, time))
    conn.commit()
    print("Appointment scheduled successfully!")

def list_appointments():
    query = """SELECT a.appointment_id, p.name AS patient, d.name AS doctor, 
                      a.appointment_date, a.appointment_time
               FROM Appointments a
               JOIN Patients p ON a.patient_id = p.patient_id
               JOIN Doctors d ON a.doctor_id = d.doctor_id"""
    cursor.execute(query)
    rows = cursor.fetchall()

    table = PrettyTable(["ID", "Patient", "Doctor", "Date", "Time"])
    for row in rows:
        table.add_row(row)
    print(table)

def create_bill(appointment_id, amount, status="Unpaid"):
    query = "INSERT INTO Billing (appointment_id, amount, status) VALUES (%s, %s, %s)"
    cursor.execute(query, (appointment_id, amount, status))
    conn.commit()
    print("Bill generated successfully!")

def list_bills():
    query = """SELECT b.bill_id, p.name AS patient, d.name AS doctor, 
                      b.amount, b.status
               FROM Billing b
               JOIN Appointments a ON b.appointment_id = a.appointment_id
               JOIN Patients p ON a.patient_id = p.patient_id
               JOIN Doctors d ON a.doctor_id = d.doctor_id"""
    cursor.execute(query)
    rows = cursor.fetchall()

    table = PrettyTable(["Bill ID", "Patient", "Doctor", "Amount", "Status"])
    for row in rows:
        table.add_row(row)
    print(table)

def menu():
    while True:
        print("\n--- Hospital Management System ---")
        print("1. Add Patient")
        print("2. List Patients")
        print("3. Add Doctor")
        print("4. List Doctors")
        print("5. Schedule Appointment")
        print("6. List Appointments")
        print("7. Create Bill")
        print("8. List Bills")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Patient Name: ")
            age = int(input("Age: "))
            gender = input("Gender (Male/Female/Other): ")
            contact = input("Contact: ")
            add_patient(name, age, gender, contact)

        elif choice == '2':
            list_patients()

        elif choice == '3':
            name = input("Doctor Name: ")
            specialization = input("Specialization: ")
            contact = input("Contact: ")
            add_doctor(name, specialization, contact)

        elif choice == '4':
            list_doctors()

        elif choice == '5':
            patient_id = int(input("Patient ID: "))
            doctor_id = int(input("Doctor ID: "))
            date = input("Appointment Date (YYYY-MM-DD): ")
            time = input("Appointment Time (HH:MM:SS): ")
            schedule_appointment(patient_id, doctor_id, date, time)

        elif choice == '6':
            list_appointments()

        elif choice == '7':
            appointment_id = int(input("Appointment ID: "))
            amount = float(input("Amount: "))
            status = input("Status (Paid/Unpaid): ")
            create_bill(appointment_id, amount, status)

        elif choice == '8':
            list_bills()

        elif choice == '9':
            print("Exiting system...")
            break

        else:
            print("Invalid choice!")


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital_db"
)
cursor = conn.cursor()

menu()

cursor.close()
conn.close()
