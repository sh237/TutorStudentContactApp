# TutorStudentContactApp

"TutorStudentContactApp" is a schedule sharing web application for tutors to facilitate schedule management with multiple students.

# DEMO

TutorStudentContactApp can be initiated by a student and a teacher each registering a new student and teacher and following each other.


https://user-images.githubusercontent.com/78858054/205973228-58eecfe6-b213-4180-8b9d-1485cb936220.mov


Once the student and teacher are linked, they can view and edit the appointments shared between them on the calendar.

# Features

Calendar operations using FullCalendar can be implemented in jQuery and Django can be integrated with it.
You can create stylish modals using SweetAlert2.

# Requirement

* Django==4.1.2
* django-bootstrap5==22.1

# Installation

Install with requirements.txt.

```bash
pip install -r requirements.txt
```

# Usage

The following commands are executed to make it work in localhost.

```bash
python manage.py createsuperuser
python manage.py runserver
```

You can access the admin site by creating a super user. On the Create New User screen, there is a field to select either Teacher or Student, and the user chooses one or the other. Then, after logging in, the student searches for a teacher and submits a request. By approving the request on the teacher's screen, the teacher can manage appointments with the student, and the student's screen after logging in will change to an appointment with the teacher.

# Note

The functions to delete users and change passwords are not implemented.

# Author

* Shunya Nagashima
* Twitter : -
* Email : syun864297531@gmail.com

# License

"TutorStudentContactApp" is under [MIT license].

Thank you!
