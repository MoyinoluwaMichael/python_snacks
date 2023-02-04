from unittest import TestCase

from python_assignments.diary.diary import Diary


class DiaryTest(TestCase):

    def setUp(self) -> None:
        self.dear_diary: Diary = Diary()
        self.dear_diary.create_entry("Summary of Life", "Dear diary, could you believe the bug I told you about "
                                                        "that I had with my code since last week is yet unresolved? "
                                                        "I'm finally fed up and I think it's high time I end this."
                                                        "At the time of writing this, I'd already taken "
                                                        "snipe...fvf..gvj3...094....")

    def test_that_entry_can_be_created(self):
        self.assertEqual(1, self.dear_diary.get_number_of_entries_created())

    def test_entry_in_a_diary_can_be_viewed_after_creation(self):
        expected: str = f"""
        ========================================================================================================================
        TITLE: Summary of Life
        ID: 1
        Date: 29-1-2023
        Time: 1:21 AM
        ========================================================================================================================
        Body:
        Dear diary, could you believe the bug I told you about that I had with my code since last week is yet unresolved? I'm finally fed up and I think it's high time I end this.At the time of writing this, I'd already taken snipe...fvf..gvj3...094....
        ========================================================================================================================
        """
        self.assertEqual(expected, self.dear_diary.view_entry_at(1))

    def test_entry_that_does_not_exist_raises_exception(self):
        with self.assertRaises(ValueError):
            self.dear_diary.view_entry_at(5)

    def test_entry_in_a_diary_can_be_deleted_after_creation(self):
        self.dear_diary.delete_entry_at(1)
        self.assertEqual(0, self.dear_diary.get_number_of_entries_created())

    def test_entries_in_a_diary_can_be_counted(self):
        self.dear_diary.create_entry("Summary of Life 2", "Life is a spoon")
        self.dear_diary.delete_entry_at(1)
        self.assertEqual(1, self.dear_diary.get_number_of_entries_created())

    def test_content_of_an_entry_can_be_edited(self):
        entry_body: str = "Dear diary, could you believe the bug I told you about "\
                          "that I had with my code since last week is yet unresolved? I'm finally fed up and I think it's high time I end this. " \
                          "At the time of writing this, I'd already taken sniper but I think my creator does not want me dead"
        self.dear_diary.edit_entry_at(1, entry_body)
        expected: str = """
        ========================================================================================================================
        TITLE: Summary of Life
        ID: 1
        Date: 29-1-2023
        Time: 1:26 AM
        ========================================================================================================================
        Body:
        Dear diary, could you believe the bug I told you about that I had with my code since last week is yet unresolved? I'm finally fed up and I think it's high time I end this. At the time of writing this, I'd already taken sniper but I think my creator does not want me dead
        ========================================================================================================================
        """
        self.assertEqual(expected, self.dear_diary.view_entry_at(1))
