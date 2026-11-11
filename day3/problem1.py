#Write a function evaluate_credit(age: int, income: float, score: int) -> str 
#returning loan approval status based on Boolean criteria.

def evaluate_credit(age: int, income: float, score: int) -> str:
    if age >= 18 and income >= 50000.0 and score >= 600:
        return 'Approved'
    elif age >= 18 and income >= 50000.0 and score <= 600:
        return 'Approved with conditions'
    else:
        return 'Denied'

    
status = evaluate_credit(20, 70000.0, 700)
if status == 'Approved':
    print(f'congratulations your loan has been {status}')
elif status == 'Approved with conditions':
    print('your loan has been approved but you might face some restrictions')
else:
    print('sorry you have been denied')        
                
