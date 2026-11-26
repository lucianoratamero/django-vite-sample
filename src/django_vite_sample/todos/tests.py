from django.test import TestCase
from rest_framework.test import APITestCase

from .models import Todo


class TodoAPITests(APITestCase):
    def test_crud(self):
        todo = self.client.post("/api/todos/", {"text": "  Write tests  "}, format="json").json()
        self.assertEqual(todo, {"id": todo["id"], "text": "Write tests", "done": False})

        self.client.patch(f"/api/todos/{todo['id']}/", {"done": True}, format="json")
        self.assertEqual(self.client.get("/api/todos/").json(), [{**todo, "done": True}])

        self.assertEqual(self.client.delete(f"/api/todos/{todo['id']}/").status_code, 204)
        self.assertEqual(self.client.get("/api/todos/").json(), [])

    def test_rejects_blank_text(self):
        response = self.client.post("/api/todos/", {"text": "   "}, format="json")
        self.assertEqual(response.status_code, 400)


class TodoPageTests(TestCase):
    def test_add_mark_done_delete(self):
        self.assertRedirects(self.client.post("/", {"text": "  Write tests  "}), "/")
        todo = Todo.objects.get()
        self.assertEqual(todo.text, "Write tests")
        self.assertContains(self.client.get("/"), "Write tests")
        self.assertContains(self.client.get("/"), "1 of 1 left to do")

        for done in [True, False]:
            self.client.post(f"/{todo.pk}/done/", {"done": str(done).lower()})
            todo.refresh_from_db()
            self.assertEqual(todo.done, done)

        self.assertRedirects(self.client.post(f"/{todo.pk}/delete/"), "/")
        self.assertFalse(Todo.objects.exists())

    def test_rejects_blank_text(self):
        self.assertContains(self.client.post("/", {"text": "   "}), "This field is required.")
        self.assertFalse(Todo.objects.exists())

    def test_actions_need_post(self):
        todo = Todo.objects.create(text="Keep me")
        self.assertEqual(self.client.get(f"/{todo.pk}/delete/").status_code, 405)
        self.assertTrue(Todo.objects.exists())

    def test_about(self):
        self.assertContains(self.client.get("/about/"), "rendered by Django templates")
