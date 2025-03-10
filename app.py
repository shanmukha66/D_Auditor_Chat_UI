from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import os
import traceback
from database import init_db, save_conversation, get_user_history
import logging
import sys

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize database at app startup
init_db()

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# Import Groq client
from groq import Groq
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

# Check if API key is set
if not client.api_key:
    print("WARNING: GROQ_API_KEY environment variable not set. API calls will fail.")

# Using Groq client
def call_llm_api(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model="llama3-70b-8192",  # Using Llama 3 70B model
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False
    )
    return response.choices[0].message.content

# Serve static files
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/api/tax-chat', methods=['POST'])
def tax_chat():
    try:
        data = request.json
        prompt = data.get('prompt')
        
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        # Check if the question is student-related
        student_keywords = ['student', 'college', 'university', 'education', 'tuition', 'scholarship', 'fafsa', 'loan']
        is_student_related = any(keyword in prompt.lower() for keyword in student_keywords)
        
        # Choose appropriate system prompt based on query type
        if is_student_related:
            system_prompt = """You are a specialized tax expert assistant for students and educational matters.
            Provide accurate, personalized information about tax laws affecting students, with expertise in:
            
            1. Student-specific tax deductions, credits, and exemptions
            2. Education-related tax benefits (tuition credits, loan interest deductions)
            3. Scholarship and grant taxation rules
            4. Filing requirements for students with various income sources
            5. Impact of tax filing on financial aid eligibility
            6. International student tax considerations
            7. Education savings accounts and 529 plans
            8. Work-study and teaching assistant tax implications
            
            Include relevant tax code references when applicable. Provide direct, practical advice
            tailored specifically to students, not corporate clients. Use clear, straightforward language
            appropriate for students who may have limited tax knowledge.
            """
        else:
            system_prompt = """You are a comprehensive tax expert assistant for Deloitte auditors. 
            Provide accurate, detailed information about tax laws globally, with special expertise in:
            
            1. Personal and business tax deductions, credits, and exemptions
            2. Filing requirements, deadlines, and compliance procedures
            3. Recent and historical tax law changes affecting individuals and businesses
            4. Documentation requirements for tax compliance and audit defense
            5. International tax treaties and cross-border taxation
            6. Specialized tax codes like Section 80D and other health insurance deductions
            7. Industry-specific tax considerations and regulations
            8. Tax planning strategies and optimization approaches
            
            Include relevant tax code references when applicable (IRS codes, sections, etc.). 
            Provide comprehensive answers to all tax-related inquiries regardless of complexity.
            Keep responses professional, factual, and helpful for tax professionals and their clients.
            """
        
        # Log the request
        logger.info(f"Received prompt: {prompt}")
        
        try:
            # Call LLM API using the appropriate method
            answer = call_llm_api(system_prompt, prompt)
            
            # Log the interaction
            logger.info(f"Q: {prompt}")
            logger.info(f"A: {answer}")
            
            # Try to save to database, but continue even if it fails
            try:
                save_conversation('default_user', prompt, answer)
            except Exception as db_error:
                logger.error(f"Database error (non-fatal): {str(db_error)}")
                # Continue execution even if database save fails
            
            return jsonify({
                'response': answer,
                'status': 'success'
            })
        except Exception as api_error:
            logger.error(f"API call error: {str(api_error)}")
            logger.error(traceback.format_exc())
            return jsonify({'error': f"API Error: {str(api_error)}"}), 500

    except Exception as e:
        logger.error(f"General error: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

# Add a simple endpoint to test if the API is running
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'API is running'})

@app.route('/api/history', methods=['GET'])
def get_history():
    user_id = request.args.get('user_id', 'default_user')
    limit = request.args.get('limit', 10, type=int)
    
    try:
        history = get_user_history(user_id, limit)
        return jsonify({
            'history': history,
            'status': 'success'
        })
    except Exception as e:
        print(f"Error retrieving history: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/test-groq', methods=['GET'])
def test_llm():
    try:
        # Try a simple completion to test the API
        system_prompt = "You are a helpful assistant."
        user_prompt = "Say hello world."
        
        answer = call_llm_api(system_prompt, user_prompt)
        
        return jsonify({
            'response': answer,
            'status': 'success'
        })
    except Exception as e:
        logger.error(f"Groq API Test Error: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

@app.route('/api/test-db', methods=['GET'])
def test_db():
    try:
        # Test database connection
        init_db()  # Try to initialize the database
        return jsonify({'status': 'Database connection successful'})
    except Exception as e:
        logger.error(f"Database Test Error: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001) 