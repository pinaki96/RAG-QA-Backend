from flask import Blueprint, request, jsonify
from service.qa_service import QAService

qa_controller = Blueprint('qa_controller', __name__)


@qa_controller.route('/ask', methods=['POST'])
def ask_question():
    """Handles API requests for Q&A."""
    data = request.json
    question = data.get('question')
    document_ids = data.get('document_ids', [])  # Optional filter for specific documents

    if not question:
        return jsonify({'error': 'Question is required'}), 400

    result = QAService.process_question(question, document_ids)
    return jsonify(result)
