import django_setup
from project.models import Student, Subject, Class, Teacher

studs = Student.objects.all()

if __name__ == "__main__":
    for s in studs:
        print(f"{s}")