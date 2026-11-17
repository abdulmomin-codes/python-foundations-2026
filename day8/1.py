
#Write a function calculate_average_score(scores_dict: dict, student_name: str) -> float
# that retrieves a student's scores list from a dictionary and 
#returns their average score. Safely handle KeyError (if the student is missing), 
#ZeroDivisionError (if the score list is empty), and TypeError 
#(if non-numeric values exist in the list), returning specific error messages for each.

def calculate_average_score(scores_dict: dict, student_name: str) -> float:
    try:
        scores = scores_dict[student_name]
        total = sum(scores)
        count =len(scores)
        return total / count
    except KeyError:
        return f"Error: Student '{student_name}' is not found."
    except ZeroDivisionError:
        return f"Error: No scores available for '{student_name}'."
    except TypeError:
        return f"Error: Non-numeric score found for '{student_name}'."        
    



student_scores = {
    "Alice": [88, 92, 85],
    "Bob": [76, 81, 79],
    "Charlie": [],
    "David": [95, "eighty-eight", 100]
}
names = ['Alice', 'Bob', 'Charlie', 'David', 'Evie']
for name in names:
    result = calculate_average_score(student_scores, name)
    print(f'{name}: {result}')