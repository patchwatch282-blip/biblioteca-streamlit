import streamlit as st

# Inicializar los datos en la memoria de la sesión web
if "usuarios" not in st.session_state:
    st.session_state.usuarios = [
        {"nombre": "Usuario 1/ Neithan Durant", "codigo": "1234", "telefono": "99999999"},
        {"nombre": "Usuario 2/ Jose Carranza", "codigo": "1010", "telefono": "88888888"},
    ]
if "libros" not in st.session_state:
    st.session_state.libros = [
        "Batman: Year One", "Resident Evil Archives", "El arte de crear",
        "El Principito", "El Arte de la Guerra", "Cien Años de Soledad",
        "Don Quijote", "1984", "Fahrenheit 451", "Dracula"
    ]
if "stock" not in st.session_state:
    st.session_state.stock = [2] * 10
if "prestamos" not in st.session_state:
    st.session_state.prestamos = []
if "logged_user" not in st.session_state:
    st.session_state.logged_user = None

st.title("📚 Sistema de Gestión de Biblioteca")

# ----------------- ACCESO / LOGIN -----------------
if not st.session_state.logged_user:
    st.subheader("Acceso de Usuario")
    codigo = st.text_input("Ingrese su código de usuario (Ej: 1234 o 1010):")
    
    if st.button("Iniciar Sesión"):
        usuario_valido = next((u for u in st.session_state.usuarios if u["codigo"] == codigo), None)
        if usuario_valido:
            st.session_state.logged_user = codigo
            st.success(f"¡Acceso correcto! Bienvenido/a, {usuario_valido['nombre']}")
            st.rerun()
        else:
            st.error("El código no está registrado.")

# ----------------- MENU PRINCIPAL (SI HAY SESION) -----------------
else:
    st.sidebar.success(f"Sesión activa: {st.session_state.logged_user}")
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state.logged_user = None
        st.rerun()

    menu = st.sidebar.selectbox("Menú de Opciones", [
        "Ver catálogo", 
        "Solicitar préstamo", 
        "Ver usuarios", 
        "Devolver libro", 
        "Ver alertas"
    ])

    # 1. Ver Catálogo
    if menu == "Ver catálogo":
        st.header("📖 Catálogo de Libros")
        for i in range(10):
            disp = st.session_state.stock[i]
            if disp > 0:
                st.write(f"*{i + 1}. {st.session_state.libros[i]}* — Disponibles: {disp}")
            else:
                st.write(f"*{i + 1}. {st.session_state.libros[i]}* — ❌ *NO DISPONIBLE*")

    # 2. Solicitar Préstamo
    elif menu == "Solicitar préstamo":
        st.header("📝 Solicitar Préstamo")
        lib_id = st.selectbox("Seleccione el libro:", range(1, 11), format_func=lambda x: f"{x}. {st.session_state.libros[x-1]}")
        
        if st.button("Confirmar Préstamo"):
            idx = lib_id - 1
            if st.session_state.stock[idx] > 0:
                st.session_state.stock[idx] -= 1
                st.session_state.prestamos.append({
                    "usuario": st.session_state.logged_user,
                    "libro": lib_id,
                    "estado": "PRESTADO"
                })
                st.success("¡Préstamo registrado con éxito!")
            else:
                st.error("No hay ejemplares disponibles de este libro.")

    # 3. Ver Usuarios
    elif menu == "Ver usuarios":
        st.header("👥 Usuarios Registrados")
        for u in st.session_state.usuarios:
            st.write(f"- *{u['nombre']}* | Código: {u['codigo']} | Tel: {u['telefono']}")

    # 4. Devolver Libro
    elif menu == "Devolver libro":
        st.header("🔄 Devolución de Libros")
        mis_prestamos = [p for p in st.session_state.prestamos if p["usuario"] == st.session_state.logged_user and p["estado"] == "PRESTADO"]
        
        if mis_prestamos:
            lib_dev = st.selectbox("Seleccione el libro a devolver:", [p["libro"] for p in mis_prestamos], format_func=lambda x: st.session_state.libros[x-1])
            if st.button("Procesar Devolución"):
                for p in st.session_state.prestamos:
                    if p["usuario"] == st.session_state.logged_user and p["libro"] == lib_dev and p["estado"] == "PRESTADO":
                        p["estado"] = "DEVUELTO"
                        st.session_state.stock[lib_dev - 1] += 1
                        st.success("¡Devolución completada con éxito!")
                        st.rerun()
        else:
            st.info("No tienes préstamos activos en este momento.")

    # 5. Ver Alertas
    elif menu == "Ver alertas":
        st.header("🚨 Alertas de Préstamos Activos")
        activos = [p for p in st.session_state.prestamos if p["estado"] == "PRESTADO"]
        if activos:
            for p in activos:
                st.write(f"- El usuario {p['usuario']} tiene prestado el libro: *{st.session_state.libros[p['libro']-1]}*")
        else:
            st.info("No existen préstamos activos actualmente.")
