from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required
from app.services.report_service import ReportService
from app.services.base_service import BaseService

report_bp = Blueprint('reports', __name__)
report_service = ReportService()


@report_bp.route('/students', methods=['GET'])
@jwt_required()
@BaseService.require_roles('admin', 'teacher')
def generate_student_report():
    """Generate student report in PDF or Excel format"""
    report_format = request.args.get('format', 'pdf').lower()
    
    if report_format not in ['pdf', 'excel']:
        return jsonify({
            'status': 'error',
            'message': 'Invalid format. Use pdf or excel'
        }), 400
    
    # Optional filters
    gender = request.args.get('gender')
    search = request.args.get('search')
    
    filters = {}
    if gender:
        filters['gender'] = gender
    
    response, status_code = report_service.generate_student_report(
        format=report_format,
        search_term=search,
        **filters
    )
    
    if status_code == 200:
        # Return file for download
        return send_file(
            response['file_path'],
            as_attachment=True,
            download_name=response['filename']
        )
    else:
        return jsonify(response), status_code


@report_bp.route('/student/<int:student_id>', methods=['GET'])
@jwt_required()
def generate_student_profile():
    """Generate individual student profile report"""
    report_format = request.args.get('format', 'pdf').lower()
    
    if report_format not in ['pdf']:
        return jsonify({
            'status': 'error',
            'message': 'Invalid format. Only PDF is supported for individual profiles'
        }), 400
    
    response, status_code = report_service.generate_student_profile(
        student_id=student_id,
        format=report_format
    )
    
    if status_code == 200:
        return send_file(
            response['file_path'],
            as_attachment=True,
            download_name=response['filename']
        )
    else:
        return jsonify(response), status_code


@report_bp.route('/analytics', methods=['GET'])
@jwt_required()
@BaseService.require_roles('admin')
def get_analytics():
    """Get student analytics and statistics"""
    response, status_code = report_service.get_student_analytics()
    return jsonify(response), status_code