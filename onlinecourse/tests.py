from django.test import TestCase
from django.contrib.auth.models import User
from onlinecourse.models import Instructor, Course, Lesson, Question, Choice
from datetime import date

class TestDataSetup(TestCase):

    def setUp(self):
        # Create admin user
        self.admin_user = User.objects.create_user(username='admin', password='P@ssword123')

        # Create Instructor
        self.instructor = Instructor.objects.create(user=self.admin_user)

        # Create Course
        self.course = Course.objects.create(
            name='Learning Django',
            description='Django is a fully featured server-side web framework.',
            pub_date=date.today()
        )
        self.course.instructors.add(self.instructor)

        # Create Lesson
        self.lesson = Lesson.objects.create(
            course=self.course,
            title='What is Django',
            order=0,
            content='Django is a high-level Python web framework that encourages rapid development...'
        )

        # Create Test Question
        self.question = Question.objects.create(
            course=self.course,
            content='Is Django a Python framework?',
            grade=100
        )
        Choice.objects.create(question=self.question, content='Yes', is_correct=True)
        Choice.objects.create(question=self.question, content='No', is_correct=False)

    def test_course_created(self):
        self.assertEqual(self.course.name, 'Learning Django')
        self.assertEqual(self.course.instructors.first(), self.instructor)

    def test_lesson_created(self):
        self.assertEqual(self.lesson.title, 'What is Django')
        self.assertEqual(self.lesson.course, self.course)

    def test_question_created(self):
        self.assertEqual(self.question.content, 'Is Django a Python framework?')
        self.assertEqual(self.question.choices.count(), 2)
