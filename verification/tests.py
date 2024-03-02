"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [tuple(), "name.txt"],
            "answer": "name.txt",
        },
        {
            "input": [("test.txt",), "name.txt"],
            "answer": "name.txt",
        },
        {
            "input": [("name.txt",), "name.txt"],
            "answer": "name(1).txt",
        },
        {
            "input": [("name(56).txt", "name(56)(1).txt", "name(56)(2).txt"), "name(56).txt"],
            "answer": "name(56)(3).txt",
        },
    ],
    "Extra": [
        {
            "input": [("name(56).txt", "name(56)(1).txt", "name(56)(3).txt"), "name(56).txt"],
            "answer": "name(56)(2).txt",
        },
        {
            "input": [("name(56).txt", "name(56)(1).txt", "name(56)(2).txt"), "name.txt"],
            "answer": "name.txt",
        },
        {
            "input": [("name(56)(1).txt", "name(56)(1)(2).txt", "name(56)(2).txt"), "name(56)(1).txt"],
            "answer": "name(56)(1)(1).txt",
        },
        {
            "input": [("name(56)(1).txt", "name(56)(1)(1).txt", "name(56).txt"), "name(56)(1).txt"],
            "answer": "name(56)(1)(2).txt",
        },
        {
            "input": [("name(56)(1).txt", "name(56)(1)(1).txt", "name(56).txt"), "name(56)(1)(1).txt"],
            "answer": "name(56)(1)(1)(1).txt",
        },
        {
            "input": [("name(56)(1).txt", "name(56)(1)(1).txt", "name(56).txt"), "name(56).txt"],
            "answer": "name(56)(2).txt",
        },
        {
            "input": [("file1(10).txt", "file1(10)(1).txt", "file1(10)(2).txt"), "file1(10).txt"],
            "answer": "file1(10)(3).txt",
        },
        {
            "input": [("data(42)(3).csv", "data(42)(3)(1).csv", "data(42)(3)(2).csv"), "data(42)(3).csv"],
            "answer": "data(42)(3)(3).csv",
        },
        {
            "input": [("document(7).pdf", "document(7)(1).pdf", "document(7)(2).pdf"), "document(7).pdf"],
            "answer": "document(7)(3).pdf",
        },
        {
            "input": [("report(25).docx", "report(25)(1).docx", "report(25)(2).docx"), "report(25).docx"],
            "answer": "report(25)(3).docx",
        },
        {
            "input": [("image(15)(2).png", "image(15)(2)(1).png", "image(15)(2)(2).png"), "image(15)(2).png"],
            "answer": "image(15)(2)(3).png",
        },
        {
            "input": [("code(5).py", "code(5)(1).py", "code(5)(2).py"), "code(5).py"],
            "answer": "code(5)(3).py",
        },
        {
            "input": [("log(8)(1).txt", "log(8)(1)(1).txt", "log(8)(1)(2).txt"), "log(8)(1).txt"],
            "answer": "log(8)(1)(3).txt",
        },
        {
            "input": [("example(12).html", "example(12)(1).html", "example(12)(2).html"), "example(12).html"],
            "answer": "example(12)(3).html",
        },
        {
            "input": [("backup(30).zip", "backup(30)(1).zip", "backup(30)(2).zip"), "backup(30).zip"],
            "answer": "backup(30)(3).zip",
        },
        {
            "input": [("test(3).txt", "test(3)(1).txt", "test(3)(2).txt"), "test(3).txt"],
            "answer": "test(3)(3).txt",
        },
    ]
}
