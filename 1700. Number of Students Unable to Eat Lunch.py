class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        out = len(students)
        length = len(students) * 5
        i = 0
        while i < length and students:
            if students[0] == sandwiches[0]:
                out -= 1
                students.pop(0)
                sandwiches.pop(0)
            else:
                rotate = students.pop(0)
                students.append(rotate)
            i += 1

        return out
