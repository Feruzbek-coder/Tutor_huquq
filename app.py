# ====================================
# HUQUQ O'RGANISH DASturni
# Local Offline Mode | Flask Backend
# ====================================

from flask import Flask, render_template, request, jsonify, send_from_directory
import json
import os
from datetime import datetime
import random

app = Flask(__name__)

# ====================================
# GLOBAL VARIABLES
# ====================================

DATA_FOLDER = 'data'
USERS_FILE = os.path.join(DATA_FOLDER, 'users.json')
QUESTIONS_FILE = os.path.join(DATA_FOLDER, 'questions.json')

# ====================================
# HELPER FUNCTIONS - DATA MANAGEMENT
# ====================================

def load_json(filepath):
    """JSON faylni o'qish"""
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_json(filepath, data):
    """JSON faylga saqlash"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_user(username):
    """Foydalanuvchini topish"""
    users = load_json(USERS_FILE)
    return users.get(username, None)

def create_user(username):
    """Yangi foydalanuvchi yaratish"""
    users = load_json(USERS_FILE)
    if username not in users:
        users[username] = {
            'name': username,
            'score': 0,
            'total_questions': 0,
            'created_at': datetime.now().isoformat(),
            'results': []
        }
        save_json(USERS_FILE, users)
    return users[username]

def update_user_score(username, score_delta):
    """Foydalanuvchining ballini yangilash"""
    users = load_json(USERS_FILE)
    if username in users:
        users[username]['score'] += score_delta
        users[username]['total_questions'] += 1
        save_json(USERS_FILE, users)


def save_test_result(username, correct, total):
    """Test natijalarini saqlash"""
    users = load_json(USERS_FILE)
    if username in users:
        result = {
            'date': datetime.now().isoformat(),
            'correct': int(correct),
            'total': int(total),
            'percentage': round((int(correct) / int(total)) * 100, 2) if total else 0
        }
        users[username].setdefault('results', []).append(result)
        save_json(USERS_FILE, users)

# ====================================
# ROUTES - ASOSIY SAHIFALAR
# ====================================

@app.route('/')
def index():
    """Bosh sahifa - Foydalanuvchi kiritish"""
    return render_template('index.html')

@app.route('/menu')
def menu():
    """Menyu sahifasi"""
    username = request.args.get('username', 'Guest')
    user = get_user(username)
    return render_template('menu.html', username=username, user=user)

@app.route('/vocabulary')
def vocabulary():
    """Darslar bo'limi"""
    username = request.args.get('username', 'Guest')
    return render_template('vocabulary.html', username=username)

@app.route('/grammar')
def grammar():
    """Mavzular va nazariya bo'limi"""
    username = request.args.get('username', 'Guest')
    return render_template('grammar.html', username=username)

@app.route('/practice')
def practice():
    """Practice (mashq) rejimi"""
    username = request.args.get('username', 'Guest')
    return render_template('practice.html', username=username)

@app.route('/test')
def test():
    """Test rejimi - 20 savol"""
    username = request.args.get('username', 'Guest')
    # Pass questions into template as fallback to avoid client-side fetch issues
    questions = load_json(QUESTIONS_FILE).get('questions', [])
    return render_template('test.html', username=username, questions=questions)

@app.route('/statistics')
def statistics():
    """Statistika sahifasi"""
    username = request.args.get('username', 'Guest')
    user = get_user(username)
    return render_template('statistics.html', username=username, user=user)

# ====================================
# API ENDPOINTS - DATA FOR FRONTEND
# ====================================

@app.route('/api/user/create', methods=['POST'])
def api_create_user():
    """Foydalanuvchi yaratish (API)"""
    data = request.get_json()
    username = data.get('username', '').strip()
    
    if not username:
        return jsonify({'success': False, 'message': 'Ism bo\'sh bo\'lishi mumkin emas'}), 400
    
    user = create_user(username)
    return jsonify({'success': True, 'user': user})

@app.route('/api/user/<username>', methods=['GET'])
def api_get_user(username):
    """Foydalanuvchi ma'lumotini olish (API)"""
    user = get_user(username)
    if user:
        return jsonify({'success': True, 'user': user})
    return jsonify({'success': False, 'message': 'Foydalanuvchi topilmadi'}), 404

@app.route('/api/questions', methods=['GET'])
def api_get_questions():
    """Barcha savollarni olish (API)"""
    questions = load_json(QUESTIONS_FILE)
    response = jsonify({'success': True, 'questions': questions.get('questions', [])})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

@app.route('/api/check-answer', methods=['POST'])
def api_check_answer():
    """Javobni tekshirish (API)"""
    data = request.get_json()
    question_id = data.get('question_id')
    user_answer = data.get('answer')
    username = data.get('username')
    
    questions = load_json(QUESTIONS_FILE)
    question = None
    
    for q in questions.get('questions', []):
        if q.get('id') == question_id:
            question = q
            break
    
    if not question:
        return jsonify({'success': False, 'message': 'Savol topilmadi'}), 404
    
    correct_answer = question.get('correct_answer', '')
    correct_option = ''
    is_correct = False
    
    if question.get('type') == 'multiple_choice':
        options = question.get('options', [])
        if isinstance(user_answer, int) or (isinstance(user_answer, str) and str(user_answer).isdigit()):
            is_correct = str(user_answer) == str(correct_answer)
            if isinstance(correct_answer, str) and correct_answer.isdigit():
                idx = int(correct_answer)
                if 0 <= idx < len(options):
                    correct_option = options[idx]
        else:
            if isinstance(correct_answer, str) and correct_answer.isdigit():
                idx = int(correct_answer)
                if 0 <= idx < len(options):
                    correct_option = options[idx]
            is_correct = str(user_answer).strip().lower() == str(correct_option).strip().lower()
    else:
        is_correct = str(user_answer).strip().lower() == str(correct_answer).strip().lower()
        correct_option = correct_answer
    
    if username:
        update_user_score(username, 1 if is_correct else -1)
    
    return jsonify({
        'success': True,
        'is_correct': is_correct,
        'correct_answer': correct_option if correct_option else correct_answer,
        'explanation': question.get('explanation', '')
    })

# ====================================
# TEST RESULT SAVE

@app.route('/api/test/result', methods=['POST'])
def api_save_test_result():
    data = request.get_json()
    username = data.get('username')
    correct = data.get('correct', 0)
    total = data.get('total', 0)

    if not username:
        return jsonify({'success': False, 'message': 'Foydalanuvchi nomi kerak'}), 400
    try:
        save_test_result(username, int(correct), int(total))
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

    return jsonify({'success': True})

# ====================================
# STATIC FILES
# ====================================

@app.route('/static/<path:filename>')
def static_files(filename):
    """Statik fayllarni xizmat qilish"""
    return send_from_directory('static', filename)

# ====================================
# ERROR HANDLERS
# ====================================

@app.errorhandler(404)
def page_not_found(error):
    """404 xatosi"""
    return render_template('error.html', message='Sahifa topilmadi'), 404

# ====================================
# MAIN
# ====================================

if __name__ == '__main__':
    # Veb-brauzer orqali 192.168.x.x:5005 manzilida ishlaydigan server
    app.run(host='0.0.0.0', port=5005, debug=True)
