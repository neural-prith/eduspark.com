@app.route("/api/multimodal-chat", methods=["POST"])
def multimodal_chat():
    try:
        print("Test")
        return jsonify({})
    except Exception as e:
        print(str(e))
        return jsonify({"error": str(e)})
