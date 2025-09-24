from flask import request, jsonify, render_template
from models import db, Empresa

def setup_routes(app):

    @app.route("/")
    def home():
        return "🚀 MANY-ULTRA está vivo y listo para monetizar en modo Ultra!"

    # Ruta para mostrar formulario web
    @app.route("/agregar_empresa_form")
    def agregar_empresa_form():
        return render_template("agregar_empresa.html")

    # Ruta para agregar empresa vía API
    @app.route("/agregar_empresa", methods=["POST"])
    def agregar_empresa():
        data = request.get_json()
        nueva = Empresa(
            nombre=data["nombre"],
            email=data["email"],
            categoria=data.get("categoria"),
            url=data.get("url"),
            monetizando=data.get("monetizando", False)
        )
        db.session.add(nueva)
        db.session.commit()
        return jsonify({"mensaje": "Empresa agregada correctamente!"})

    # Listar todas las empresas
    @app.route("/empresas")
    def listar_empresas():
        empresas = Empresa.query.all()
        return jsonify([e.to_dict() for e in empresas])

    # Listar solo empresas que están monetizando
    @app.route("/empresas_monetizando")
    def empresas_monetizando():
        empresas = Empresa.query.filter_by(monetizando=True).all()
        return jsonify([e.to_dict() for e in empresas])
