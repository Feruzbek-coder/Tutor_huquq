from app import app
import json

c = app.test_client()

# Create test user
username = 'ci_test_user'
print('Creating user', username)
r = c.post('/api/user/create', json={'username': username})
print('create user status', r.status_code, r.get_json())

# Get questions
r = c.get('/api/questions')
qs = r.get_json().get('questions', [])
print('loaded questions:', len(qs))

tests = [q for q in qs if q.get('type') in ('multiple_choice','fill_blank')]
print('testable questions:', len(tests))

# Answer first 3 questions using stored correct_answer
correct_count = 0
for q in tests[:3]:
    ans = q.get('correct_answer')
    print('\nQuestion id', q.get('id'), 'type', q.get('type'))
    print('Correct answer (raw):', ans)
    payload = {'question_id': q.get('id'), 'answer': ans, 'username': username}
    resp = c.post('/api/check-answer', json=payload)
    print('response:', resp.status_code, resp.get_json())
    if resp.get_json().get('is_correct'):
        correct_count += 1

# Save result
print('\nSaving test result: {}/{}'.format(correct_count, min(3,len(tests))))
r = c.post('/api/test/result', json={'username': username, 'correct': correct_count, 'total': min(3,len(tests))})
print('save result status', r.status_code, r.get_json())

# Fetch user
r = c.get(f'/api/user/{username}')
print('\nUser record:')
print(json.dumps(r.get_json(), ensure_ascii=False, indent=2))
