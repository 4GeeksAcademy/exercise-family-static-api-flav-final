import os
from flask import Flask, jsonify, request
from datastructures import FamilyStructure
from flask_cors import CORS 
from utils import APIException, generate_sitemap 
import os

app = Flask(__name__)


jackson_family = FamilyStructure("Jackson")



@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200



@app.route('/members/<int:member_id>', methods=['GET'])
def get_one_member(member_id):
    member = jackson_family.get_member(member_id)
    
    if member is None:
        return jsonify({"error": "Member not found"}), 404
    
    return jsonify(member), 200


@app.route('/members', methods=['POST'])
def add_member():
    body = request.get_json()
    
   
    if body is None:
        return jsonify({"error": "Request body must be JSON"}), 400
    if "first_name" not in body or "age" not in body or "lucky_numbers" not in body:
        return jsonify({"error": "Missing required fields: first_name, age, lucky_numbers"}), 400
    
   
    if "last_name" not in body:
        body["last_name"] = "Jackson"
    
    new_member = jackson_family.add_member(body)
    return jsonify(new_member), 200



@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    success = jackson_family.delete_member(member_id)
    
    if not success:
        return jsonify({"error": "Member not found"}), 404
    
    return jsonify({"done": True}), 200



if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)