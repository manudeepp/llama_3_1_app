from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory
import subprocess
import logging
import os
import markdown

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Global variable to store conversation history
conversation_history = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global conversation_history
    if request.method == 'POST':
        user_input = request.json['text']
        conversation_history.append(f"User: {user_input}")
        
        # Construct the prompt with the conversation history
        prompt = "\n".join(conversation_history)
        app.logger.debug(f"Constructed prompt: {prompt}")

        # Call the Ollama command
        process = subprocess.Popen(['ollama', 'run', 'llama3.1'], 
                                   stdin=subprocess.PIPE, 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE, 
                                   text=True)
        
        # Send the prompt to the process
        stdout, stderr = process.communicate(input=prompt)
        
        # Process the model's response
        output = stdout.strip()
        app.logger.debug(f"Output from model: {output}")

        # Append the model's response to the conversation history
        conversation_history.append(f"Llama: {output}")

        if stderr:
            app.logger.error(f"Error from model: {stderr}")

        # Convert Markdown to HTML
        formatted_output = markdown.markdown(output)
        return jsonify(prediction=formatted_output)
    
    return render_template('index.html', conversation_history=conversation_history)

@app.route('/clear', methods=['POST'])
def clear():
    global conversation_history
    conversation_history = []
    return redirect(url_for('index'))

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
