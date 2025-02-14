from flask import Blueprint, request, jsonify
import os
from werkzeug.utils import secure_filename
from service.document_service import create_document, list_documents, get_document, update_document, \
    delete_document, extract_text_from_file

document_controller = Blueprint('document_controller', __name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@document_controller.route('/upload', methods=['POST'])
def upload_document():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    extracted_text = extract_text_from_file(file_path)
    if not extracted_text:
        return jsonify({'error': 'Failed to extract text from file'}), 500

    document = create_document(filename, extracted_text)
    print('document')
    print(document)
    print('document')
    return jsonify({'message': 'Document uploaded and processed successfully', 'document': document.serialize}), 201


@document_controller.route('/list', methods=['GET'])
def list_docs():
    return jsonify({'documents': list_documents()})


@document_controller.route('/get/<int:doc_id>', methods=['GET'])
def get_doc(doc_id):
    document = get_document(doc_id)
    if document:
        return jsonify({'document': document})
    return jsonify({'error': 'Document not found'}), 404


@document_controller.route('/update/<int:doc_id>', methods=['PUT'])
def update_doc(doc_id):
    data = request.json
    name = data.get('name')
    content = data.get('content')

    if not name or not content:
        return jsonify({'error': 'Name and content are required'}), 400

    if update_document(doc_id, name, content):
        return jsonify({'message': 'Document updated successfully'})
    return jsonify({'error': 'Document not found'}), 404


@document_controller.route('/delete/<int:doc_id>', methods=['DELETE'])
def delete_doc(doc_id):
    if delete_document(doc_id):
        return jsonify({'message': 'Document deleted successfully'})
    return jsonify({'error': 'Document not found'}), 404
