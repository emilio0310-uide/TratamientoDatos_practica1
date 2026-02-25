from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from pydantic import BaseModel, Field, ValidationError
from ipaddress import ip_address
import logging

# ---------------- CONFIGURACIÓN ----------------
app = Flask(__name__)
auth = HTTPBasicAuth()

USERS = {
    "admin": "admin123",
    "security": "securepass"
}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger("security-api")

# ---------------- MODELO ----------------
class AccessRequest(BaseModel):
    user_id: str = Field(..., min_length=3)
    ip_address: str
    success: bool

    def validate_ip(self):
        ip_address(self.ip_address)

# ---------------- AUTENTICACIÓN ----------------
@auth.verify_password
def verify_password(username, password):
    return USERS.get(username) == password

# ---------------- SCORING ----------------
def calculate_risk(success: bool, ip: str) -> int:
    score = 0

    if not success:
        score += 60

    if ip.startswith("192.168") or ip.startswith("10."):
        score += 10
    else:
        score += 30

    return min(score, 100)

# ---------------- ENDPOINTS ----------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/access", methods=["POST"])
@auth.login_required
def access():
    try:
        data = AccessRequest(**request.json)
        data.validate_ip()
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    risk = calculate_risk(data.success, data.ip_address)

    logger.info(
        f"user={data.user_id} ip={data.ip_address} risk={risk}"
    )

    return jsonify({
        "user": data.user_id,
        "risk_score": risk,
        "classification": "HIGH RISK" if risk >= 70 else "LOW RISK"
    })

# ---------------- MAIN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)