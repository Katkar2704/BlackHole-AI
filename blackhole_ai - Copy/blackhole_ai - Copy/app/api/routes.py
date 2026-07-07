from flask import Blueprint, render_template, request, jsonify
from app.llm.llm_registry import LLM_CATALOG
from app.routing.router import route_and_execute
import asyncio

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def index():
    # Pass the catalog to index.html so Jinja can build the dropdown
    return render_template('index.html', catalog=LLM_CATALOG)

@api_bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        result = loop.run_until_complete(route_and_execute(
            data.get('query'), 
            data.get('llm'), 
            data.get('history', [])
        ))
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        loop.close()