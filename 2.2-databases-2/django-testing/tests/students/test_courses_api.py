from random import randint

import pytest
import json
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

"""проверка получения 1го курса"""
@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    courses_count = randint(1, 10)
    course = course_factory(_quantity=courses_count)
    course_id = course[0].id
    url = f'/api/v1/courses/{course_id}/'
    resp = client.get(url)
    assert resp.status_code == 200
    data = resp.json()
    assert data['id'] == course_id

"""проверка получения списка курсов"""
@pytest.mark.django_db
def test_get_courses_list(course_factory, client):
    courses_count = randint(1, 10)
    courses_list = course_factory(_quantity=courses_count)
    url = '/api/v1/courses/'
    resp = client.get(url)
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == len(courses_list)

"""проверка фильтрации списка курсов по id"""
@pytest.mark.django_db
def test_filter_course_id(course_factory, client):
    courses_count = randint(1, 10)
    courses_list = course_factory(_quantity=courses_count)
    course_id = courses_list[courses_count-1].id
    url = f'/api/v1/courses/?id={course_id}'
    resp = client.get(url)
    assert resp.status_code == 200
    data = resp.json()
    for course in data:
        assert course['id'] == course_id

"""проверка фильтрации списка курсов по name"""
@pytest.mark.django_db
def test_filter_course_name(course_factory, client):
    courses_count = randint(1, 10)
    courses_list = course_factory(_quantity=courses_count)
    course_name = courses_list[courses_count-1].name
    url = f'/api/v1/courses/?name={course_name}'
    resp = client.get(url)
    assert resp.status_code == 200
    data = resp.json()
    for course in data:
        assert course['name'] == course_name

"""тест успешного создания курса"""
@pytest.mark.django_db
def test_post_course(client):
    courses_count = Course.objects.count()
    resp = client.post('/api/v1/courses/', data={'name': 'test_post_course'})
    assert resp.status_code == 201
    assert Course.objects.count() == courses_count + 1

"""тест успешного обновления курса"""
@pytest.mark.django_db
def test_path_course(course_factory, client):
    courses_count = randint(1, 10)
    courses_list = course_factory(_quantity=courses_count)
    course_id = courses_list[0].id
    url = f'/api/v1/courses/{course_id}/'
    data = json.dumps({'name': 'test_patch_name'})
    resp = client.patch(url, data, content_type='application/json')
    assert resp.status_code == 200

"""тест успешного удаления курса"""
@pytest.mark.django_db
def test_delete_course(course_factory, client):
    courses_count = randint(1, 10)
    courses_list = course_factory(_quantity=courses_count)
    course_id = courses_list[courses_count - 1].id
    url = f'/api/v1/courses/{course_id}/'
    courses_count = Course.objects.count()
    resp = client.delete(url)
    assert resp.status_code == 204
    assert Course.objects.count() == courses_count - 1
